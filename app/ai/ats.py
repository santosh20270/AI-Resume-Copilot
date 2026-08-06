"""
ATS Resume Analyzer
"""

import json

from app.ai.client import generate


def analyze_resume(resume_text: str, job_description: str):
    """
    Analyze resume against a job description and
    return ATS results as JSON.
    """

    prompt = f"""
You are an ATS system and Senior HR Recruiter.

Analyze the resume against the job description.

Return ONLY valid JSON.

Do NOT return markdown.
Do NOT return explanation.
Do NOT wrap the response inside ```json.

Resume:
{resume_text}

Job Description:
{job_description}

Return exactly this JSON:

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

- ATS Score must be an integer between 0 and 100.
- Percentages must be integers.
- Arrays should contain short bullet-style strings.
- Return ONLY valid JSON.
"""

    text = generate(prompt)

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    try:
        return json.loads(text)

    except json.JSONDecodeError:

        return {
            "ats_score": 0,
            "job_role": "Unknown",
            "overall_match": "Unavailable",
            "keyword_match": 0,
            "skills_match": 0,
            "experience_match": 0,
            "education_match": 0,
            "matched_skills": [],
            "missing_skills": [],
            "strengths": [],
            "weaknesses": [
                "Unable to parse AI response."
            ],
            "suggestions": [
                "Please try again after a few moments."
            ],
            "interview_probability": "Unavailable",
            "verdict": "AI response could not be processed."
        }