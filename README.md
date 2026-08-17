# 🤖 Company Policy AI Assistant

An AI-powered **Company Policy Assistant** that allows users to ask questions about company policies and receive answers based on the organization's uploaded policy documents.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from company policy PDFs before generating an answer using Google's Gemini LLM.

The project also uses **LangGraph** to implement an agentic workflow and **Streamlit** to provide an interactive web interface.

---

## 📌 Project Overview

Employees often need to search through lengthy company policy documents to find answers to questions such as:

* What is the company's leave policy?
* How many annual leaves are allowed?
* What is the work-from-home policy?
* What is the reimbursement policy?
* What are the travel guidelines?
* What is the notice period policy?

Instead of manually searching through PDFs, this application allows users to ask questions in natural language.

### Example

**User:**

> How many days of annual leave can an employee take?

**AI Assistant:**

> According to the company policy, employees are entitled to ...

The answer is generated using information retrieved from the uploaded company policy documents.

---

# 🎯 Project Objectives

The main objectives of this project are:

1. Read company policy PDF documents.
2. Extract text from the PDFs.
3. Split large documents into smaller chunks.
4. Convert text chunks into vector embeddings.
5. Store embeddings in a vector database.
6. Retrieve relevant chunks based on the user's question.
7. Send the retrieved context to Gemini.
8. Generate a grounded response.
9. Use an agentic workflow to manage the question-answering process.
10. Provide an easy-to-use Streamlit interface.

---

# 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │   Company Policy PDF  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     read_pdf.py       │
                    │  Extract PDF Text     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    chunk_pdf.py      │
                    │   Split into Chunks  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    embeddings.py     │
                    │ Generate Embeddings  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   vector_store.py    │
                    │       ChromaDB       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       User Query     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       rag.py         │
                    │ Retrieve Relevant    │
                    │      Context         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       agent.py       │
                    │    LangGraph Agent   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Gemini LLM        │
                    │   Gemini Flash       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Streamlit UI      │
                    │     app.py           │
                    └──────────────────────┘
```

---

# 🔄 End-to-End Workflow

The complete project workflow is:

```text
PDF
 ↓
Text Extraction
 ↓
Text Cleaning
 ↓
Chunking
 ↓
Embedding Generation
 ↓
Vector Database
 ↓
User Question
 ↓
Question Embedding
 ↓
Similarity Search
 ↓
Relevant Document Chunks
 ↓
Context + Question
 ↓
Gemini LLM
 ↓
Agent Workflow
 ↓
Final Answer
 ↓
Streamlit UI
```

---

# 📂 Project Structure

```text
company-policy-ai-assistant/
│
├── documents/
│   └── company_policy.pdf
│
├── src/
│   ├── read_pdf.py
│   ├── chunk_pdf.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── ingest.py
│   ├── rag.py
│   ├── agent.py
│   └── app.py
│
├── .env
├── test_key.py
├── test_gemini.py
├── requirements.txt
├── README.md
└── .gitignore
```

> **Important:** Never upload `.env` or your Gemini API key to GitHub.

---

# 🛠️ Technologies Used

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Core programming language       |
| Gemini        | Large Language Model            |
| Google GenAI  | Gemini API integration          |
| python-dotenv | Environment variable management |
| PyPDF         | PDF text extraction             |
| ChromaDB      | Vector database                 |
| LangChain     | LLM/RAG components              |
| LangGraph     | Agentic workflow                |
| Streamlit     | Web application                 |
| VS Code       | Development environment         |
| Pylance       | Python development support      |

---

# 1️⃣ Create the Project

The project was created on the D drive.

Example:

```text
D:\
└── company-policy-ai-assistant
```

Open the project folder in VS Code.

---

# 2️⃣ Create a Virtual Environment

Open the VS Code terminal:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

After activation, the terminal should show something similar to:

```text
(venv) D:\company-policy-ai-assistant>
```

### Why use a virtual environment?

A virtual environment isolates the project's Python dependencies from other Python projects on the computer.

This prevents dependency conflicts.

---

# 3️⃣ Create Gemini API Key

The application uses Google's Gemini API.

Create an API key through Google AI Studio.

The API key should **never be hard-coded inside Python files**.

Instead, create:

```text
.env
```

Example:

```text
GEMINI_API_KEY=your_api_key_here
```

The actual API key should not be committed to GitHub.

Add `.env` to `.gitignore`.

Example:

```text
.env
venv/
__pycache__/
*.pyc
chroma_db/
```

---

# 4️⃣ Test the API Key

Two Python files were created:

```text
test_key.py
test_gemini.py
```

### test_key.py

This file verifies that the environment variable containing the API key can be loaded successfully.

Conceptually:

```text
.env
 ↓
python-dotenv
 ↓
Environment Variable
 ↓
GEMINI_API_KEY
```

### test_gemini.py

This file verifies that the application can successfully communicate with the Gemini API.

Testing the API before building the complete application is useful because it separates API configuration problems from RAG/application problems.

---

# 5️⃣ Install Required Libraries

The required dependencies were installed inside the virtual environment.

```bash
pip install streamlit
pip install google-genai
pip install python-dotenv
pip install pypdf
pip install chromadb
pip install langgraph
pip install langchain
```

The project dependencies were then stored in:

```text
requirements.txt
```

You can generate the file with:

```bash
pip freeze > requirements.txt
```

Another developer can then install the dependencies using:

```bash
pip install -r requirements.txt
```

---

# 6️⃣ Create the Documents Folder

A folder named:

```text
documents/
```

was created.

The company policy PDF is stored inside it:

```text
documents/
└── company_policy.pdf
```

This PDF becomes the knowledge source for the RAG system.

---

# 7️⃣ PDF Text Extraction — read_pdf.py

The first processing step is reading the PDF.

The purpose of `read_pdf.py` is:

```text
PDF
 ↓
PDF Reader
 ↓
Pages
 ↓
Extracted Text
```

The application uses **PyPDF** to read the PDF and extract text from each page.

The extracted text becomes the raw input for the next stage.

---

# 8️⃣ Document Chunking — chunk_pdf.py

A complete company policy document may contain hundreds of pages.

Sending the entire PDF to an LLM for every question is inefficient.

Therefore, the extracted text is divided into smaller pieces called **chunks**.

```text
Large PDF
     ↓
Extracted Text
     ↓
Chunking
     ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
...
```

For example:

```text
Company Policy
       ↓
 ┌─────────────┐
 │ Leave Policy│
 └─────────────┘

 ┌─────────────┐
 │ Travel      │
 │ Policy      │
 └─────────────┘

 ┌─────────────┐
 │ WFH Policy  │
 └─────────────┘
```

Chunking improves retrieval because the vector database can identify the smaller section most relevant to a question.

---

# 9️⃣ Embeddings — embeddings.py

The next step is converting text into numerical vectors.

An embedding represents the semantic meaning of text.

For example:

```text
"What is the leave policy?"
```

is converted into something conceptually like:

```text
[0.12, -0.42, 0.73, 0.19, ...]
```

The same process is performed for document chunks.

```text
Document Chunk
      ↓
Embedding Model
      ↓
Vector
```

The important idea is:

> Similar meanings should have similar vector representations.

This allows the system to perform semantic search.

---

# 🔟 Vector Database — vector_store.py

The generated embeddings are stored in **ChromaDB**.

The process is:

```text
Document Chunks
      ↓
Embeddings
      ↓
ChromaDB
```

ChromaDB acts as the vector store.

When the user asks a question, the question is also converted into an embedding.

The system then compares the question vector with stored document vectors.

Conceptually:

```text
User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Most Relevant Chunks
```

---

# 1️⃣1️⃣ Data Ingestion — ingest.py

`ingest.py` connects the document-processing pipeline together.

The ingestion pipeline is:

```text
PDF
 ↓
Read PDF
 ↓
Extract Text
 ↓
Create Chunks
 ↓
Generate Embeddings
 ↓
Store in ChromaDB
```

This is normally performed when the documents are added or updated.

It creates the searchable knowledge base used by the RAG application.

---

# 1️⃣2️⃣ RAG Pipeline — rag.py

RAG stands for:

**Retrieval-Augmented Generation**

Instead of asking Gemini to answer purely from its internal knowledge, the application first retrieves relevant information from the company policy.

The process is:

```text
User Question
      ↓
Retriever
      ↓
ChromaDB
      ↓
Relevant Policy Chunks
      ↓
Context
      ↓
Gemini
      ↓
Answer
```

For example:

**Question:**

```text
What is the work from home policy?
```

The retriever searches the company policy database and retrieves the chunks related to work-from-home rules.

Those chunks are then provided to Gemini as context.

---

# 1️⃣3️⃣ Agentic Workflow — agent.py

The project also uses **LangGraph** to create an agentic workflow.

The agent controls the sequence of operations.

A simplified workflow is:

```text
User Question
      ↓
Agent
      ↓
Understand Question
      ↓
Retrieve Information
      ↓
Check Context
      ↓
Generate Answer
      ↓
Return Response
```

The key difference is:

### Traditional LLM application

```text
Question → LLM → Answer
```

### RAG application

```text
Question → Retrieval → Context → LLM → Answer
```

### Agentic RAG application

```text
Question
   ↓
Agent
   ↓
Decide/Execute Steps
   ↓
Retrieve
   ↓
Use Context
   ↓
LLM
   ↓
Answer
```

This is where the project moves from a basic chatbot toward an **agentic AI workflow**.

---

# 1️⃣4️⃣ Gemini LLM

The project uses Google's Gemini model as the LLM.

The LLM is responsible for generating the final natural-language response using the retrieved company policy context.

The overall architecture is therefore:

```text
Company Policy
      ↓
ChromaDB
      ↓
Retriever
      ↓
Relevant Context
      ↓
Gemini
      ↓
Final Answer
```

> **Model note:** Make sure the exact Gemini model name configured in your code is currently available for your API account. Model availability and API naming can change over time, so it is better to keep the model name configurable rather than hard-code an obsolete model name.

---

# 1️⃣5️⃣ Streamlit Application — app.py

`app.py` creates the user interface.

Streamlit provides a simple web interface where users can enter questions.

Example:

```text
┌───────────────────────────────────────────────┐
│        Company Policy AI Assistant            │
│                                               │
│ Ask your question:                           │
│                                               │
│ [ What is the leave policy?                ] │
│                                               │
│              [ Ask ]                          │
│                                               │
│ Assistant:                                    │
│ According to the company policy...            │
│                                               │
└───────────────────────────────────────────────┘
```

The Streamlit application connects the UI with the RAG/agent pipeline.

---

# 1️⃣6️⃣ Running the Application

After completing the project setup, run:

```bash
streamlit run src/app.py
```

If `app.py` is located in the project root, use:

```bash
streamlit run app.py
```

Streamlit starts a local web server and provides a local URL.

The application opens in the browser.

---

# 🔄 Complete Project Execution

The entire project can be understood in two major phases.

## Phase 1 — Knowledge Base Creation

```text
Company Policy PDF
       ↓
read_pdf.py
       ↓
Extract Text
       ↓
chunk_pdf.py
       ↓
Create Chunks
       ↓
embeddings.py
       ↓
Generate Embeddings
       ↓
vector_store.py
       ↓
Store in ChromaDB
```

This creates the searchable company-policy knowledge base.

---

## Phase 2 — Question Answering

```text
User
 ↓
Streamlit UI
 ↓
app.py
 ↓
agent.py
 ↓
rag.py
 ↓
Convert Question to Embedding
 ↓
Search ChromaDB
 ↓
Retrieve Relevant Chunks
 ↓
Create Context
 ↓
Gemini LLM
 ↓
Generate Answer
 ↓
Streamlit
 ↓
User
```

---

# 🧠 Why RAG Is Used

A normal LLM does not automatically know the private content of your company's internal policy documents.

RAG solves this problem.

Instead of trying to train the LLM on the company policy, we:

1. Store the documents externally.
2. Convert them into embeddings.
3. Store them in a vector database.
4. Retrieve relevant information when a question is asked.
5. Give that information to the LLM.
6. Generate the answer using the retrieved context.

This is generally cheaper and easier to update than fine-tuning an LLM whenever company policies change.

---

# 🔐 Security

The Gemini API key is stored in:

```text
.env
```

Example:

```text
GEMINI_API_KEY=********
```

The `.env` file should never be committed to GitHub.

The `.gitignore` file should contain:

```text
.env
venv/
__pycache__/
*.pyc
chroma_db/
```

---

# 📊 Technical Architecture

```text
                    USER
                     │
                     ▼
              ┌─────────────┐
              │  Streamlit  │
              │    app.py   │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │  LangGraph  │
              │   Agent     │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │     RAG     │
              │   rag.py    │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │  ChromaDB   │
              │Vector Search│
              └──────┬──────┘
                     │
                     ▼
              Relevant Context
                     │
                     ▼
              ┌─────────────┐
              │   Gemini    │
              │     LLM     │
              └──────┬──────┘
                     │
                     ▼
                  ANSWER
```

---

# 🗂️ File Responsibilities

| File               | Responsibility                            |
| ------------------ | ----------------------------------------- |
| `read_pdf.py`      | Reads PDF and extracts text               |
| `chunk_pdf.py`     | Splits extracted text into chunks         |
| `embeddings.py`    | Creates vector embeddings                 |
| `vector_store.py`  | Stores/searches embeddings in ChromaDB    |
| `ingest.py`        | Runs document ingestion pipeline          |
| `rag.py`           | Implements retrieval-augmented generation |
| `agent.py`         | Implements LangGraph agent workflow       |
| `app.py`           | Streamlit user interface                  |
| `test_key.py`      | Tests environment/API key configuration   |
| `test_gemini.py`   | Tests Gemini API connectivity             |
| `.env`             | Stores secret API configuration           |
| `requirements.txt` | Stores Python dependencies                |

---

# 🚀 How to Run the Project

## Step 1 — Clone the Repository

```bash
git clone <your-github-repository-url>
cd company-policy-ai-assistant
```

## Step 2 — Create Virtual Environment

```bash
python -m venv venv
```

## Step 3 — Activate Environment

Windows:

```bash
venv\Scripts\activate
```

## Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 5 — Configure Environment Variables

Create:

```text
.env
```

Add:

```text
GEMINI_API_KEY=your_api_key
```

## Step 6 — Add Company Policy

Place the PDF inside:

```text
documents/
```

## Step 7 — Run Ingestion

```bash
python src/ingest.py
```

This processes the PDF and creates the vector database.

## Step 8 — Start Streamlit

```bash
streamlit run src/app.py
```

---

# 🧪 Example Questions

After starting the application, users can ask questions such as:

```text
What is the annual leave policy?
```

```text
What is the work from home policy?
```

```text
What are the employee reimbursement rules?
```

```text
How many sick leaves are allowed?
```

```text
What is the company's travel policy?
```

The assistant retrieves the relevant policy information and generates an answer.

---

# ⚠️ Hallucination Prevention

The RAG system is designed to reduce hallucinations by grounding the response in retrieved company-policy content.

The LLM should be instructed to:

```text
Answer using the provided company policy context.

If the information is not available in the provided context,
do not invent an answer.
```

This makes the application more suitable for enterprise policy-related use cases.

---

# 🔮 Future Improvements

Possible production-level improvements include:

* Document metadata filtering
* Page-level citations
* Source references in responses
* Better chunking strategies
* Hybrid search
* Reranking
* Conversation memory
* Multiple document support
* Role-based access control
* Authentication
* Evaluation framework
* RAG quality evaluation
* LangSmith/observability
* Logging and monitoring
* Cloud deployment
* Dockerization
* CI/CD
* Automated document ingestion
* Enterprise vector databases
* Guardrails
* Human-in-the-loop approval
* LLM evaluation and monitoring

---

# 💼 Business Value

This solution can help organizations reduce the time employees spend searching through policy documents.

Potential applications include:

* HR Policy Assistant
* Employee Handbook Assistant
* Compliance Assistant
* Legal Document Assistant
* Banking Policy Assistant
* Insurance Policy Assistant
* IT Policy Assistant
* Knowledge Management Assistant

---

# 🎤 Interview Explanation

A concise way to explain this project in an interview:

> "I built a Company Policy AI Assistant using a RAG-based architecture. I started by extracting text from company policy PDFs using PyPDF, then split the documents into smaller chunks and generated embeddings for those chunks. I stored the embeddings in ChromaDB to enable semantic similarity search. When a user asks a question, the application converts the query into an embedding and retrieves the most relevant policy chunks. Those chunks are then provided as context to the Gemini LLM to generate a grounded response. I used LangGraph to structure the agentic workflow and Streamlit to build the user-facing application. I also separated the document ingestion pipeline from the query-time RAG pipeline so documents can be processed independently and queried efficiently."

---

# ⭐ Key Concepts Demonstrated

This project demonstrates practical experience with:

**Generative AI**

```text
Gemini LLM
Prompting
LLM Application Development
```

**RAG**

```text
Document Loading
Chunking
Embeddings
Vector Database
Retrieval
Context Augmentation
Generation
```

**Agentic AI**

```text
LangGraph
Agent Workflow
State/Workflow Management
Tool/Step Orchestration
```

**Application Development**

```text
Python
Streamlit
Environment Variables
API Integration
```

**Vector Search**

```text
Embeddings
Semantic Search
ChromaDB
Similarity Retrieval
```

---

# 📌 Project Summary

```text
Company Policy PDF
        ↓
   PDF Extraction
        ↓
      Chunking
        ↓
     Embeddings
        ↓
      ChromaDB
        ↓
    User Question
        ↓
      Retrieval
        ↓
 Relevant Context
        ↓
   LangGraph Agent
        ↓
     Gemini LLM
        ↓
    Final Answer
        ↓
    Streamlit UI
```

This project demonstrates an end-to-end implementation of a **production-oriented GenAI/RAG application**, from document ingestion and vector search to agent orchestration and user-facing deployment.
