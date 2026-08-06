from app.logger import logger


def extract_text_from_txt(file_path: str) -> str:
    """
    Extract text from a TXT file.

    Args:
        file_path (str): Path to the TXT file.

    Returns:
        str: Extracted text.
    """

    try:
        logger.info(f"Reading TXT file: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        logger.info("TXT text extracted successfully.")

        return text

    except FileNotFoundError:
        logger.error(f"TXT file not found: {file_path}")
        raise

    except Exception as e:
        logger.exception(f"Unexpected error while reading TXT: {e}")
        raise


if __name__ == "__main__":
    result = extract_text_from_txt("data/job_description.txt")
    print(result)