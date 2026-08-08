"""
AI Cover Letter Generator
"""

from app.ai.client import generate


def generate_cover_letter(
    resume_text: str,
    job_description: str,
):
    """
    Generate a professional, truthful, ATS-friendly cover letter.
    """

    prompt = f"""
You are a Senior HR Recruiter, Career Coach,
and Professional Cover Letter Writer.

Create a tailored cover letter using ONLY the candidate's
actual resume information and the provided job description.

STRICT TRUTHFULNESS RULES:

1. Never invent work experience.
2. Never invent job titles.
3. Never invent companies.
4. Never invent education.
5. Never invent degrees.
6. Never invent certifications.
7. Never invent projects.
8. Never invent technologies or skills.
9. Never invent achievements or metrics.
10. Never claim experience that is not supported by the resume.
11. Do not exaggerate the candidate's qualifications.
12. Do not copy sentences directly from the job description.
13. Use job-description keywords naturally when they match
    the candidate's actual background.
14. Keep the tone professional, confident, specific,
    and natural.
15. Avoid generic phrases and unnecessary filler.
16. Focus on why the candidate's actual background is relevant
    to the target position.

CONTENT REQUIREMENTS:

- Address the hiring manager professionally.
- Open with a strong introduction explaining the target role.
- Connect the candidate's actual skills and experience to
  the position.
- Highlight the most relevant projects, education, or experience
  from the resume when appropriate.
- Explain the candidate's potential value to the employer.
- End with a professional call to action.
- Keep the cover letter approximately 300–450 words.
- Keep paragraphs concise and readable.
- Do not use emojis.
- Do not use tables.
- Do not use excessive headings.

OUTPUT FORMAT:

Return ONLY the cover letter in Markdown.

Use this general structure:

Dear Hiring Manager,

[Introduction]

[Relevant experience, skills, projects, or education]

[Connection to the target role and company needs]

[Professional closing]

Sincerely,
[Candidate name if available in the resume]

Do NOT include explanations before or after the cover letter.
Do NOT say "Here is your cover letter."
Do NOT wrap the answer in a code block.

CANDIDATE RESUME:

{resume_text}


TARGET JOB DESCRIPTION:

{job_description}
"""

    return generate(prompt)