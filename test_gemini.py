import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Ask Gemini a question
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain RAG in very simple language for a school student."
)

# Print Gemini's answer
print(response.text)