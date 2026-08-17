import os
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from google import genai


# ==========================================
# 1. PROJECT PATH
# ==========================================

project_folder = Path(__file__).resolve().parent.parent

db_folder = project_folder / "chroma_db"


# ==========================================
# 2. LOAD GEMINI API KEY
# ==========================================

load_dotenv(project_folder / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")


# ==========================================
# 3. CREATE GEMINI CLIENT
# ==========================================

client = genai.Client(api_key=api_key)


# ==========================================
# 4. CONNECT TO CHROMADB
# ==========================================

chroma_client = chromadb.PersistentClient(
    path=str(db_folder)
)

collection = chroma_client.get_collection(
    name="company_policy"
)

print("Connected to ChromaDB")


# ==========================================
# 5. ASK USER QUESTION
# ==========================================

question = input("\nAsk a question about the company policy: ")

print("\nYour question:")
print(question)


# ==========================================
# 6. CREATE EMBEDDING FOR QUESTION
# ==========================================

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=question
)

question_embedding = result.embeddings[0].values


# ==========================================
# 7. SEARCH CHROMADB
# ==========================================

results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)


# ==========================================
# 8. GET RELEVANT CHUNKS
# ==========================================

retrieved_chunks = results["documents"][0]

print("\n================================")
print("RETRIEVED INFORMATION")
print("================================")

for i, chunk in enumerate(retrieved_chunks):

    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)


# ==========================================
# 9. COMBINE CHUNKS
# ==========================================

context = "\n\n".join(retrieved_chunks)


# ==========================================
# 10. CREATE RAG PROMPT
# ==========================================

prompt = f"""
You are a company policy assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not present in the context,
say: "I could not find this information in the company policy."

Context:
{context}

User Question:
{question}

Give a clear and concise answer.
"""


# ==========================================
# 11. SEND TO GEMINI
# ==========================================

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)


# ==========================================
# 12. DISPLAY FINAL ANSWER
# ==========================================

print("\n================================")
print("RAG ANSWER")
print("================================")

print(response.text)