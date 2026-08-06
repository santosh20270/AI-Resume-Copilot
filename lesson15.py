from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
You are an expert Python teacher.

I am a beginner.

Explain what a Python list is.

Use simple English.

Give one real-life example.

Keep the answer under 150 words.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(response.text)