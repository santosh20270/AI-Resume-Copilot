from app.pdf_reader import extract_text_from_pdf
from app.job_reader import read_job_description
from app.ai_analyzer import analyze_resume
from app.prompts import ATS_SCORE_PROMPT
from app.logger import logger


def main():
    """
    Main entry point of the AI Resume Copilot application.
    """

    try:
        logger.info("========== AI Resume Copilot Started ==========")

        # Step 1: Read Resume
        logger.info("Reading resume...")
        resume_text = extract_text_from_pdf("data/resume.pdf")

        # Step 2: Read Job Description
        logger.info("Reading job description...")
        job_description = read_job_description("data/job_description.txt")

        # Step 3: Build Prompt
        logger.info("Creating ATS prompt...")
        prompt = ATS_SCORE_PROMPT.format(
            resume=resume_text,
            job_description=job_description
        )

        # Step 4: Ask Gemini
        logger.info("Sending request to Gemini...")
        result = analyze_resume(prompt)

        # Step 5: Display Result
        logger.info("ATS report generated successfully.")

        print("\n" + "=" * 60)
        print("AI RESUME COPILOT - ATS REPORT")
        print("=" * 60)
        print(result)
        print("=" * 60)

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        print("\n❌ Error")
        print("Required file not found.")
        print(e)

    except Exception as e:
        logger.exception("Unexpected error occurred.")
        print("\n❌ Unexpected Error")
        print(e)

    finally:
        logger.info("========== Application Finished ==========")


if __name__ == "__main__":
    main()