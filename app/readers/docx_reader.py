from docx import Document
from app.logger import logger


def extract_text_from_docx(file_path: str) -> str:
    """
    Extract text from a DOCX file.

    Args:
        file_path (str): Path to the DOCX file.

    Returns:
        str: Extracted text.
    """

    try:
        logger.info(f"Reading DOCX: {file_path}")

        document = Document(file_path)

        text = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                text.append(paragraph.text)

        logger.info("DOCX text extracted successfully.")

        return "\n".join(text)

    except FileNotFoundError:
        logger.error(f"DOCX file not found: {file_path}")
        raise

    except Exception as e:
        logger.exception(f"Unexpected error while reading DOCX: {e}")
        raise


if __name__ == "__main__":
    result = extract_text_from_docx("data/resume.docx")
    print(result[:500])