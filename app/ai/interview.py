"""
AI Interview Preparation Module
"""

import json

from app.ai.client import generate


def generate_interview_questions(
    resume_text: str,
    job_description: str,
):
    """
    Generate interview questions and suggested answers.
    """

    prompt = f"""
You are a Senior Technical Interviewer.

Create a complete interview preparation guide.

Resume:

{resume_text}

Job Description:

{job_description}

Return ONLY valid JSON.

Do NOT return markdown.
Do NOT return explanation.

Return exactly this structure:

{{
    "job_role": "",
    "difficulty": "",
    "technical_questions": [
        {{
            "question": "",
            "answer": ""
        }}
    ],
    "hr_questions": [
        {{
            "question": "",
            "answer": ""
        }}
    ],
    "behavioral_questions": [
        {{
            "question": "",
            "answer": ""
        }}
    ],
    "tips": []
}}

Rules:

- Generate exactly 10 technical questions.
- Generate exactly 10 HR questions.
- Generate exactly 10 behavioral questions.
- Answers should be concise (2–5 sentences).
- Generate 8 interview preparation tips.
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
            "job_role": "Unknown",
            "difficulty": "Unknown",
            "technical_questions": [],
            "hr_questions": [],
            "behavioral_questions": [],
            "tips": [
                "Unable to generate interview questions.",
                "Please try again in a few moments."
            ]
        }