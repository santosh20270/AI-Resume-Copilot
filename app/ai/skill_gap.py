"""
AI Skill Gap Analyzer
"""

import json

from app.ai.client import generate


def analyze_skill_gap(
    resume_text: str,
    job_description: str,
):
    """
    Analyze the skill gap between a resume and a job description.
    """

    prompt = f"""
You are an expert Career Coach and ATS Specialist.

Compare the candidate's resume with the job description.

Return ONLY valid JSON.

Resume:

{resume_text}

Job Description:

{job_description}

Return exactly this JSON structure:

{{
    "overall_readiness": "",
    "matched_skills": [],
    "missing_skills": [],
    "learning_roadmap": [],
    "recommended_projects": [],
    "recommended_certifications": [],
    "estimated_learning_time": ""
}}

Rules:

- Return ONLY JSON.
- Do not return markdown.
- Do not include explanations.
- learning_roadmap should contain 8 to 10 ordered steps.
- recommended_projects should contain 5 project ideas.
- recommended_certifications should contain 5 certifications.
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
            "overall_readiness": "Unknown",
            "matched_skills": [],
            "missing_skills": [],
            "learning_roadmap": [
                "Unable to generate learning roadmap."
            ],
            "recommended_projects": [],
            "recommended_certifications": [],
            "estimated_learning_time": "Unknown"
        }