from pypdf import PdfReader

pdf_path = "documents/venus_company_policy.pdf"

reader = PdfReader(pdf_path)

print("Number of pages:", len(reader.pages))

for page_number, page in enumerate(reader.pages):
    text = page.extract_text()

    print("\n==============================")
    print(f"PAGE {page_number + 1}")
    print("==============================")

    print(text[:1000])