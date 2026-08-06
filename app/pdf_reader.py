from pypdf import PdfReader
from app.logger import logger


def extract_text_from_pdf(pdf_path):
    """
    Read a PDF file and return all extracted text.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """

    logger.info(f"Reading PDF: {pdf_path}")

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    logger.info("PDF text extracted successfully.")

    return text


if __name__ == "__main__":
    resume = extract_text_from_pdf("data/resume.pdf")
    print(resume[:500])