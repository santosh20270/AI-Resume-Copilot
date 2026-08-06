from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

history = []

print("🤖 Gemini Chatbot with Memory")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    history.append(f"User: {user_input}")

    prompt = "\n".join(history)

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    ai_reply = response.text

    print("\nGemini:", ai_reply)
    print()

    history.append(f"Gemini: {ai_reply}")