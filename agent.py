import os
from pathlib import Path
from typing import TypedDict

import chromadb
from dotenv import load_dotenv
from google import genai

from langgraph.graph import StateGraph, START, END


# =====================================================
# 1. PROJECT PATH
# =====================================================

project_folder = Path(__file__).resolve().parent.parent

db_folder = project_folder / "chroma_db"


# =====================================================
# 2. LOAD GEMINI API KEY
# =====================================================

load_dotenv(project_folder / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )


# =====================================================
# 3. CREATE GEMINI CLIENT
# =====================================================

client = genai.Client(
    api_key=api_key
)


# =====================================================
# 4. CONNECT TO CHROMADB
# =====================================================

chroma_client = chromadb.PersistentClient(
    path=str(db_folder)
)


collection = chroma_client.get_collection(
    name="company_policy"
)


# =====================================================
# 5. DEFINE AGENT STATE
# =====================================================

class AgentState(TypedDict):

    question: str

    context: str

    answer: str

    chat_history: str

    sources: list


# =====================================================
# 6. RETRIEVAL NODE
# =====================================================

def retrieve_information(state: AgentState):

    question = state["question"]


    # -------------------------------------------------
    # Create embedding for user question
    # -------------------------------------------------

    result = client.models.embed_content(

        model="gemini-embedding-001",

        contents=question

    )


    question_embedding = (
        result.embeddings[0].values
    )


    # -------------------------------------------------
    # Search ChromaDB
    # -------------------------------------------------

    results = collection.query(

        query_embeddings=[
            question_embedding
        ],

        n_results=3

    )


    # -------------------------------------------------
    # Get retrieved documents
    # -------------------------------------------------

    retrieved_chunks = results["documents"][0]


    # -------------------------------------------------
    # Get metadata
    # -------------------------------------------------

    retrieved_metadatas = (
        results["metadatas"][0]
    )


    # -------------------------------------------------
    # Combine chunks
    # -------------------------------------------------

    context = "\n\n".join(

        retrieved_chunks

    )


    # -------------------------------------------------
    # Create source list
    # -------------------------------------------------

    sources = []


    for metadata in retrieved_metadatas:

        source = (

            f"📄 {metadata['source']} "
            f"— Page {metadata['page']}"

        )

        sources.append(source)


    # -------------------------------------------------
    # Return retrieval result
    # -------------------------------------------------

    return {

        "context": context,

        "sources": sources

    }


# =====================================================
# 7. GENERATION NODE
# =====================================================

def generate_answer(state: AgentState):

    question = state["question"]

    context = state["context"]

    chat_history = state.get(
        "chat_history",
        ""
    )


    # -------------------------------------------------
    # Prompt
    # -------------------------------------------------

    prompt = f"""
You are a company policy assistant.

Your job is to answer questions about the
Venus company policy.

IMPORTANT RULES:

1. Answer ONLY using the information
   provided in the company policy context.

2. Do NOT invent information.

3. If the answer is not available in the
   context, say exactly:

"I could not find this information in the
company policy."

4. Keep the answer short and clear.

5. Use previous conversation only when it
   helps understand the current question.

----------------------------------------
PREVIOUS CONVERSATION
----------------------------------------

{chat_history}

----------------------------------------
COMPANY POLICY CONTEXT
----------------------------------------

{context}

----------------------------------------
USER QUESTION
----------------------------------------

{question}

----------------------------------------
ANSWER
----------------------------------------
"""


    # -------------------------------------------------
    # Generate response
    # -------------------------------------------------

    response = client.models.generate_content(

        model="gemini-3.6-flash",

        contents=prompt

    )


    return {

        "answer": response.text

    }


# =====================================================
# 8. CREATE LANGGRAPH
# =====================================================

graph_builder = StateGraph(
    AgentState
)


# =====================================================
# 9. ADD NODES
# =====================================================

graph_builder.add_node(

    "retrieve",

    retrieve_information

)


graph_builder.add_node(

    "generate",

    generate_answer

)


# =====================================================
# 10. CREATE EDGES
# =====================================================

graph_builder.add_edge(

    START,

    "retrieve"

)


graph_builder.add_edge(

    "retrieve",

    "generate"

)


graph_builder.add_edge(

    "generate",

    END

)


# =====================================================
# 11. COMPILE AGENT
# =====================================================

agent = graph_builder.compile() 