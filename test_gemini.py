from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

print("✅ API Key Loaded:", api_key[:10] + "...")

# Create Gemini client
client = genai.Client(api_key=api_key)

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Reply with only: Hello World"
    )

    print("\n✅ SUCCESS")
    print("=" * 50)
    print(response.text)

except Exception as e:
    print("\n❌ ERROR")
    print("=" * 50)
    print(str(e))