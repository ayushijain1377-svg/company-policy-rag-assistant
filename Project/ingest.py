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


# =====================================================
# 5. GET OR CREATE COLLECTION
# =====================================================

collection = chroma_client.get_or_create_collection(

    name="company_policy"

)


# =====================================================
# 6. INGEST PDF FUNCTION
# =====================================================

def ingest_pdf(pdf_path):

    pdf_path = Path(pdf_path)

    print(
        f"\n📄 Processing: {pdf_path.name}"
    )


    # -------------------------------------------------
    # Read PDF
    # -------------------------------------------------

    reader = PdfReader(
        str(pdf_path)
    )


    print(
        f"Number of pages: {len(reader.pages)}"
    )


    # -------------------------------------------------
    # Store chunks
    # -------------------------------------------------

    chunks = []

    metadatas = []


    # -------------------------------------------------
    # Process pages
    # -------------------------------------------------

    for page_number, page in enumerate(

        reader.pages,

        start=1

    ):

        text = page.extract_text()


        if not text or not text.strip():

            print(
                f"⚠️ Page {page_number}: "
                f"No text found"
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


            chunks.append(
                chunk
            )


            metadatas.append({

                "source": pdf_path.name,

                "page": page_number

            })


    print(
        f"🧩 Created {len(chunks)} chunks"
    )


    # -------------------------------------------------
    # Create embeddings
    # -------------------------------------------------

    embeddings = []


    for index, chunk in enumerate(chunks):

        print(

            f"🧠 Creating embedding "
            f"{index + 1}/{len(chunks)}"

        )


        result = client.models.embed_content(

            model="gemini-embedding-001",

            contents=chunk

        )


        embedding = (

            result.embeddings[0].values

        )


        embeddings.append(
            embedding
        )


    # -------------------------------------------------
    # Create unique IDs
    # -------------------------------------------------

    ids = []


    for index in range(len(chunks)):

        ids.append(

            f"{pdf_path.stem}_chunk_{index}"

        )


    # -------------------------------------------------
    # Store in ChromaDB
    # -------------------------------------------------

    if chunks:

        collection.add(

            ids=ids,

            documents=chunks,

            embeddings=embeddings,

            metadatas=metadatas

        )


    print(
        f"✅ {pdf_path.name} "
        f"successfully added to ChromaDB"
    )


    return len(chunks)