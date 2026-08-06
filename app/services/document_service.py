from pathlib import Path

from app.logger import logger
from app.readers.pdf_reader import extract_text_from_pdf
from app.readers.docx_reader import extract_text_from_docx
from app.readers.text_reader import extract_text_from_txt
from app.readers.image_reader import extract_text_from_image


def extract_text(file_path: str) -> str:
    """
    Automatically detect the file type and extract text.
    """

    extension = Path(file_path).suffix.lower()

    logger.info(f"Detected file type: {extension}")

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension == ".docx":
        return extract_text_from_docx(file_path)

    elif extension == ".txt":
        return extract_text_from_txt(file_path)

    elif extension in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(file_path)

    else:
        raise ValueError(f"Unsupported file type: {extension}")


if __name__ == "__main__":
    result = extract_text("data/sample_resume.png")
    print(result[:1000])