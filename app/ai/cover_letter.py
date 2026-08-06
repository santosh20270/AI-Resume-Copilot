"""
AI Cover Letter Generator
"""

from app.ai.client import generate


def generate_cover_letter(
    resume_text: str,
    job_description: str,
):
    """
    Generate a professional ATS-friendly cover letter.
    """

    prompt = f"""
You are an expert HR Recruiter and Career Coach.

Write a professional ATS-friendly cover letter.

Requirements:

- Never invent experience.
- Never invent education.
- Never invent projects.
- Use only information from the resume.
- Tailor the letter to the job description.
- Use a professional and confident tone.
- Keep it between 300 and 450 words.
- Include:
    • Greeting
    • Introduction
    • Body
    • Closing
- Return ONLY the cover letter in Markdown.

=========================
RESUME
=========================

{resume_text}

=========================
JOB DESCRIPTION
=========================

{job_description}
"""

    return generate(prompt)