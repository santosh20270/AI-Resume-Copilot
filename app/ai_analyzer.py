import json
from google import genai

from app.config import GEMINI_API_KEY, GEMINI_MODEL

# ==========================================================
# GEMINI CLIENT
# ==========================================================

client = genai.Client(api_key=GEMINI_API_KEY)

# ==========================================================
# ATS ANALYSIS
# ==========================================================

def analyze_resume(resume_text: str, job_description: str):
    """
    Analyze a resume against a job description and return
    structured ATS results as JSON.
    """

    prompt = f"""
You are an ATS system and Senior HR Recruiter.

Analyze the resume against the job description.

Return ONLY valid JSON.

Do NOT return markdown.
Do NOT return explanation.
Do NOT wrap in ```json.

Resume:
{resume_text}

Job Description:
{job_description}

Return exactly this JSON format:

{{
    "ats_score": 0,
    "job_role": "",
    "overall_match": "",
    "keyword_match": 0,
    "skills_match": 0,
    "experience_match": 0,
    "education_match": 0,
    "matched_skills": [],
    "missing_skills": [],
    "strengths": [],
    "weaknesses": [],
    "suggestions": [],
    "interview_probability": "",
    "verdict": ""
}}

Rules:
- ats_score must be an integer (0-100)
- All percentages must be integers
- Arrays should contain short bullet-style strings
- Return ONLY JSON
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)


# ==========================================================
# RESUME REWRITE
# ==========================================================

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
- Improve wording.
- Improve formatting.
- Add missing keywords naturally.
- Improve professional summary.
- Improve skills section.
- Improve project descriptions.
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

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    return response.text


# ==========================================================
# COVER LETTER GENERATOR
# ==========================================================

def generate_cover_letter(resume_text: str, job_description: str):
    """
    Generate a professional ATS-friendly cover letter.
    """

    prompt = f"""
You are an expert HR recruiter and professional career coach.

Write a professional ATS-friendly cover letter using the
candidate's resume and the job description.

Requirements:

- Do NOT invent experience.
- Do NOT invent education.
- Do NOT invent projects.
- Use ONLY the information available in the resume.
- Tailor the letter to the job description.
- Professional tone.
- Keep it between 300 and 450 words.
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

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    return response.text