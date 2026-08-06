"""
AI Resume Rewriter
"""

from app.ai.client import generate


def rewrite_resume(resume_text: str, job_description: str):
    """
    Rewrite the resume to improve ATS compatibility.
    """

    prompt = f"""
You are a professional ATS Resume Writer.

Rewrite the resume to maximize ATS compatibility.

Rules:

- Never invent experience.
- Never invent education.
- Never invent projects.
- Keep all information truthful.
- Improve wording and grammar.
- Improve formatting.
- Add missing keywords naturally.
- Improve the professional summary.
- Improve the skills section.
- Improve project descriptions.
- Make the resume ATS-friendly.
- Return ONLY the rewritten resume in Markdown.

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