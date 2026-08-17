Company Policy RAG Assistant
AI-Powered Enterprise Knowledge Assistant using RAG, Gemini, ChromaDB & LangGraph

An end-to-end Retrieval-Augmented Generation (RAG) application that enables users to query company policy documents using natural language and receive context-aware, document-grounded responses.

📌 Overview

The Company Policy RAG Assistant is a Generative AI application designed to simplify access to company policy information.

Instead of manually searching through lengthy policy documents, users can ask questions in natural language. The system retrieves the most relevant information from the policy knowledge base and uses Google Gemini to generate a concise response based on the retrieved context.

The project demonstrates an end-to-end RAG + Agent workflow, from document ingestion and vector indexing to retrieval, LLM-based generation, and an interactive Streamlit interface.

🎯 Problem Statement

Organizations often maintain large collections of HR, compliance, and operational policy documents. Finding specific information manually can be time-consuming and inefficient.

This project addresses the problem by providing an AI-powered interface that allows employees to:

Search policy information using natural language
Retrieve relevant sections from policy documents
Get context-aware answers
Reduce manual document search effort
🏗️ Solution Architecture
                    ┌─────────────────────┐
                    │   Policy Documents  │
                    │        (PDF)        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   PDF Extraction    │
                    │       PyPDF         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Text Chunking     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Embeddings      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      ChromaDB       │
                    │    Vector Store     │
                    └──────────┬──────────┘
                               │
                               │
                    ┌──────────▼──────────┐
                    │     User Query      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Semantic Retrieval │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Relevant Context  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     LangGraph       │
                    │   Agent Workflow    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Google Gemini     │
                    │   LLM Generation    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Streamlit       │
                    │     Web App         │
                    └─────────────────────┘
🔄 RAG Workflow

The application follows this pipeline:

Documents → Extract → Chunk → Embed → Store → Retrieve → Generate → Display

1. Document Ingestion

Company policy PDFs are loaded and their content is extracted using PyPDF.

2. Text Chunking

Large documents are divided into smaller chunks to improve retrieval accuracy.

3. Embedding Generation

The document chunks are transformed into numerical vector representations using an embedding model.

4. Vector Storage

The generated embeddings are stored in ChromaDB, enabling semantic similarity search.

5. Query Retrieval

When a user submits a question, the system searches the vector database and retrieves the most relevant policy content.

6. Context Augmentation

The retrieved information is provided as context to the LLM.

7. Response Generation

Google Gemini generates the final response based on the retrieved policy context.

8. Agent Orchestration

LangGraph is used to structure and orchestrate the workflow.

9. Response Display

The generated response is presented through an interactive Streamlit interface.

✨ Key Features
📄 PDF document ingestion
🔍 Semantic document retrieval
🧠 Embedding-based search
🗄️ ChromaDB vector storage
🤖 Google Gemini LLM integration
🔄 LangGraph agent workflow
💬 Natural-language question answering
🖥️ Streamlit interactive interface
🔐 Environment-based API key management
🛠️ Technology Stack
Technology	Purpose
Python	Application development
Google Gemini	LLM-based response generation
LangGraph	Agent workflow orchestration
ChromaDB	Vector database
PyPDF	PDF document processing
Embeddings	Semantic representation
Streamlit	Web application interface
python-dotenv	Environment configuration
Git & GitHub	Version control
📁 Project Structure
company-policy-rag-assistant/
│
├── 📁 documents/
│   └── Company policy documents
│
├── 📁 src/
│   ├── read_pdf.py
│   ├── chunk_pdf.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── ingest.py
│   ├── rag.py
│   ├── agent.py
│   ├── test_key.py
│   └── test_gemini.py
│
├── 📄 app.py
├── 📄 requirements.txt
├── 📄 README.md
└── 📄 .gitignore
🚀 Getting Started
Prerequisites
Python 3.10+
Google Gemini API key
Git
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/company-policy-rag-assistant.git
cd company-policy-rag-assistant
2. Create a Virtual Environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
🔐 Environment Configuration

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

The application reads the API key from the environment instead of hard-coding credentials.

Never upload .env or expose your API key publicly.

▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

💬 Example Queries

Users can ask questions such as:

What is the company's leave policy?


What is the work-from-home policy?


What are the employee reimbursement rules?


What is the attendance policy?


How many annual leave days are available?
🎯 Business Applications

The architecture can be extended to build:

HR Policy Assistants
Enterprise Knowledge Assistants
Compliance Knowledge Systems
Internal Documentation Search
Employee Self-Service Assistants
Customer Support Knowledge Bases
🔮 Future Enhancements
 Multi-document knowledge base
 Source citations for retrieved information
 Conversation memory
 RAG evaluation and benchmarking
 Response quality monitoring
 Authentication and role-based access
 Document upload through Streamlit
 Cloud deployment
 Production monitoring and observability
🧠 Skills Demonstrated

Generative AI • Retrieval-Augmented Generation • Agentic AI • Python • LLMs • LangGraph • Google Gemini • ChromaDB • Vector Search • Embeddings • NLP • Streamlit • Git • GitHub

👩‍💻 Author

Ayushi Jain

Senior Analyst | Data Science | Machine Learning | Generative AI | Agentic AI

⭐ Project

If you find this project useful, consider giving the repository a star ⭐.
