import os
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ==========================================
# 1. PROJECT PATH
# ==========================================

project_folder = Path(__file__).resolve().parent.parent

documents_folder = project_folder / "documents"

db_folder = project_folder / "chroma_db"


# ==========================================
# 2. LOAD GEMINI API KEY
# ==========================================

load_dotenv(project_folder / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")


client = genai.Client(api_key=api_key)


# ==========================================
# 3. FIND PDF
# ==========================================

pdf_files = list(documents_folder.glob("*.pdf"))

if not pdf_files:
    raise FileNotFoundError(
        "No PDF found inside documents folder"
    )

pdf_path = pdf_files[0]

print("PDF found:", pdf_path)


# ==========================================
# 4. READ PDF
# ==========================================

reader = PdfReader(pdf_path)

full_text = ""

for page in reader.pages:

    text = page.extract_text()

    if text:
        full_text += text + "\n"


# ==========================================
# 5. CREATE CHUNKS
# ==========================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_text(full_text)

print("Number of chunks:", len(chunks))


# ==========================================
# 6. CREATE CHROMADB
# ==========================================

chroma_client = chromadb.PersistentClient(
    path=str(db_folder)
)

collection = chroma_client.get_or_create_collection(
    name="company_policy"
)

print("ChromaDB collection created")


# ==========================================
# 7. CREATE EMBEDDINGS
# ==========================================

embeddings = []

for i, chunk in enumerate(chunks):

    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=chunk
    )

    vector = result.embeddings[0].values

    embeddings.append(vector)

    print(f"Embedded chunk {i + 1}/{len(chunks)}")


# ==========================================
# 8. STORE IN CHROMADB
# ==========================================

ids = [f"chunk_{i}" for i in range(len(chunks))]

collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings
)


print("\n================================")
print("SUCCESS!")
print("================================")

print("Chunks stored:", len(chunks))
print("Database location:", db_folder)