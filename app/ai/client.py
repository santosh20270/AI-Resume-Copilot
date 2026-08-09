"""
Gemini Client Configuration
"""

import time

from google import genai
from google.genai.errors import ServerError, ClientError

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

    Automatically retries temporary server errors.
    Handles API quota errors with a user-friendly message.
    """

    retries = 3

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
            )

            return response.text

        # --------------------------------------------------
        # Gemini Server Error
        # --------------------------------------------------

        except ServerError:

            if attempt < retries - 1:

                time.sleep(5)

            else:

                raise RuntimeError(
                    "Gemini AI is temporarily unavailable. "
                    "Please try again in a few moments."
                )

        # --------------------------------------------------
        # Gemini Client/API Error
        # --------------------------------------------------

        except ClientError as error:

            error_text = str(error)

            # ----------------------------------------------
            # Quota / Rate Limit
            # ----------------------------------------------

            if (
                "429" in error_text
                or "RESOURCE_EXHAUSTED" in error_text
                or "quota" in error_text.lower()
            ):

                raise RuntimeError(
                    "⚠️ Gemini API quota temporarily exhausted. "
                    "Please try again after the quota resets "
                    "or check your Gemini API usage."
                )

            # ----------------------------------------------
            # Other API errors
            # ----------------------------------------------

            raise RuntimeError(
                "⚠️ Gemini API request failed. "
                "Please check your API configuration and try again."
            )

        # --------------------------------------------------
        # Unexpected Error
        # --------------------------------------------------

        except Exception as error:

            raise RuntimeError(
                f"⚠️ Unable to generate AI response: {error}"
            )