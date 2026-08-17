import os
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader


# =====================================================
# 1. PROJECT PATH
# =====================================================

project_folder = Path(__file__).resolve().parent.parent

documents_folder = project_folder / "documents"

db_folder = project_folder / "chroma_db"


# =====================================================
# 2. LOAD GEMINI API KEY
# =====================================================

load_dotenv(project_folder / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env"
    )


# =====================================================
# 3. CREATE GEMINI CLIENT
# =====================================================

client = genai.Client(
    api_key=api_key
)


# =====================================================
# 4. FIND ALL PDF FILES
# =====================================================

pdf_files = list(
    documents_folder.glob("*.pdf")
)

if not pdf_files:

    raise FileNotFoundError(
        "No PDF files found in documents folder."
    )


print("\n================================")
print("📚 PDF DOCUMENTS FOUND")
print("================================")

for pdf_file in pdf_files:

    print(
        f"📄 {pdf_file.name}"
    )


# =====================================================
# 5. CREATE CHUNKS
# =====================================================

all_chunks = []

all_metadatas = []


for pdf_file in pdf_files:

    print("\n================================")
    print(
        f"📄 PROCESSING: {pdf_file.name}"
    )
    print("================================")


    # -------------------------------------------------
    # Read PDF
    # -------------------------------------------------

    reader = PdfReader(
        str(pdf_file)
    )


    print(
        f"Number of pages: {len(reader.pages)}"
    )


    # -------------------------------------------------
    # Process every page
    # -------------------------------------------------

    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):

        text = page.extract_text()


        # Skip empty pages
        if not text or not text.strip():

            print(
                f"Page {page_number}: No text"
            )

            continue


        # -------------------------------------------------
        # Simple chunking
        # -------------------------------------------------

        words = text.split()

        chunk_size = 150


        for i in range(
            0,
            len(words),
            chunk_size
        ):

            chunk_words = words[
                i:i + chunk_size
            ]


            chunk = " ".join(
                chunk_words
            )


            if not chunk.strip():

                continue


            # -------------------------------------------------
            # Store chunk
            # -------------------------------------------------

            all_chunks.append(
                chunk
            )


            # -------------------------------------------------
            # Store metadata
            # -------------------------------------------------

            all_metadatas.append({

                "source": pdf_file.name,

                "page": page_number

            })


print("\n================================")
print("📦 CHUNKING COMPLETED")
print("================================")

print(
    f"Total chunks: {len(all_chunks)}"
)


# =====================================================
# 6. CREATE EMBEDDINGS
# =====================================================

print("\n================================")
print("🧠 CREATING EMBEDDINGS")
print("================================")


all_embeddings = []


for index, chunk in enumerate(
    all_chunks
):

    print(
        f"Embedding chunk "
        f"{index + 1}/{len(all_chunks)}"
    )


    result = client.models.embed_content(

        model="gemini-embedding-001",

        contents=chunk

    )


    embedding = (
        result.embeddings[0].values
    )


    all_embeddings.append(
        embedding
    )


# =====================================================
# 7. CONNECT TO CHROMADB
# =====================================================

print("\n================================")
print("🗄️ CONNECTING TO CHROMADB")
print("================================")


chroma_client = chromadb.PersistentClient(

    path=str(db_folder)

)


# =====================================================
# 8. RECREATE COLLECTION
# =====================================================

try:

    chroma_client.delete_collection(
        name="company_policy"
    )

    print(
        "Old collection deleted."
    )

except Exception:

    print(
        "No previous collection found."
    )


collection = chroma_client.create_collection(

    name="company_policy"

)


# =====================================================
# 9. CREATE UNIQUE IDS
# =====================================================

ids = [

    f"chunk_{i}"

    for i in range(
        len(all_chunks)
    )

]


# =====================================================
# 10. STORE EVERYTHING IN CHROMADB
# =====================================================

collection.add(

    ids=ids,

    documents=all_chunks,

    embeddings=all_embeddings,

    metadatas=all_metadatas

)


# =====================================================
# 11. SUCCESS MESSAGE
# =====================================================

print("\n================================")
print("🎉 RAG DATABASE READY")
print("================================")

print(
    f"📄 PDF files: {len(pdf_files)}"
)

print(
    f"🧩 Total chunks: {len(all_chunks)}"
)

print(
    "🧠 Embeddings created"
)

print(
    "🗄️ ChromaDB updated"
)

print(
    "📑 Page metadata stored"
)

print("================================")