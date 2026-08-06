from PIL import Image
import pytesseract

from app.logger import logger
from app.config import TESSERACT_PATH

# Configure Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def extract_text_from_image(file_path: str) -> str:
    """
    Extract text from an image using Tesseract OCR.

    Supported formats:
    - PNG
    - JPG
    - JPEG

    Args:
        file_path (str): Path to the image.

    Returns:
        str: Extracted text.
    """

    try:
        logger.info(f"Reading image: {file_path}")

        image = Image.open(file_path)

        # Convert image to RGB for better OCR compatibility
        if image.mode != "RGB":
            image = image.convert("RGB")

        text = pytesseract.image_to_string(image)

        logger.info("Image OCR completed successfully.")

        return text.strip()

    except FileNotFoundError:
        logger.error(f"Image file not found: {file_path}")
        raise

    except Exception as e:
        logger.exception(f"Unexpected OCR error: {e}")
        raise


if __name__ == "__main__":

    result = extract_text_from_image("data/sample_resume.png")

    print("=" * 60)
    print("OCR OUTPUT")
    print("=" * 60)
    print(result)