from pypdf import PdfReader
from app.logger import logger


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.
    """

    try:
        logger.info(f"Reading PDF: {file_path}")

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        logger.info("PDF text extracted successfully.")

        return text

    except FileNotFoundError:
        logger.error(f"PDF file not found: {file_path}")
        raise

    except Exception as e:
        logger.exception(f"Unexpected error while reading PDF: {e}")
        raise


if __name__ == "__main__":
    result = extract_text_from_pdf("data/resume.pdf")
    print(result[:500])