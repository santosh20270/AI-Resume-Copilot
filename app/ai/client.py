"""
Gemini Client Configuration
"""

import time

from google import genai
from google.genai.errors import ServerError

from app.config import GEMINI_API_KEY, GEMINI_MODEL

# ==========================================================
# Gemini Client
# ==========================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)

MODEL = GEMINI_MODEL


# ==========================================================
# Shared Gemini Function
# ==========================================================

def generate(prompt: str):
    """
    Generate content using Gemini.

    Automatically retries if the Gemini server is busy.
    """

    retries = 3

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
            )

            return response.text

        except ServerError:

            if attempt < retries - 1:

                time.sleep(5)

            else:

                raise

        except Exception:

            raise