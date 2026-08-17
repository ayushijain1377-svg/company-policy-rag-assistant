import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Load API key
project_folder = Path(__file__).resolve().parent.parent
load_dotenv(project_folder / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")


# Create Gemini client
client = genai.Client(api_key=api_key)


# Find PDF
documents_folder = project_folder / "documents"
pdf_files = list(documents_folder.glob("*.pdf"))

if not pdf_files:
    raise FileNotFoundError("No PDF found in documents folder")

pdf_path = pdf_files[0]

print("PDF found:", pdf_path)


# Read PDF
reader = PdfReader(pdf_path)

full_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        full_text += text + "\n"


# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_text(full_text)

print("Number of chunks:", len(chunks))


# Create embedding for first chunk
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=chunks[0]
)

embedding = result.embeddings[0].values

print("Embedding created successfully!")
print("Embedding dimensions:", len(embedding))
print("First 10 values:", embedding[:10])