from pypdf import PdfReader
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Read PDF
reader = PdfReader("data/resume.pdf")

resume_text = ""

for page in reader.pages:
    extracted = page.extract_text()
    if extracted:
        resume_text += extracted + "\n"

# Prompt for Gemini
prompt = f"""
You are an experienced HR recruiter.

Review the following resume.

Provide:
1. Overall feedback
2. Strengths
3. Weaknesses
4. Missing skills
5. Suggestions for improvement

Resume:

{resume_text}
"""

# Ask Gemini
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(response.text)