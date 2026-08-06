import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini Model
GEMINI_MODEL = "gemini-3.6-flash"

# OCR
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"