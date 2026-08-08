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
    Generate a role-specific interview preparation guide.
    """

    prompt = f"""
You are a Senior Technical Interviewer, Hiring Manager,
and Career Coach.

Create a personalized interview preparation guide based ONLY
on the candidate's resume and the target job description.

IMPORTANT TRUTHFULNESS RULES:

1. Never invent experience.
2. Never invent projects.
3. Never invent education.
4. Never invent certifications.
5. Never invent technologies or skills.
6. Never claim the candidate has experience that is not shown
   in the resume.
7. Questions may test skills mentioned in the job description,
   but suggested answers must remain truthful to the resume.
8. If the resume does not provide enough information for an
   answer, explicitly say that the candidate should prepare
   their own truthful example.
9. Do not fabricate metrics or achievements.

RESUME:

{resume_text}


JOB DESCRIPTION:

{job_description}


TASK:

Identify the target role and create a complete interview
preparation guide.

Return ONLY valid JSON.

Do NOT return Markdown.
Do NOT return explanations.
Do NOT wrap the JSON in a code block.

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

QUESTION REQUIREMENTS:

Technical Questions:
- Generate exactly 10.
- Focus on technologies, concepts, tools, and responsibilities
  relevant to the target role.
- Prioritize technologies appearing in both the resume and
  job description.
- Include a mixture of fundamental and practical questions.
- Suggested answers must be concise and truthful.

HR Questions:
- Generate exactly 10.
- Include questions about motivation, career goals,
  strengths, weaknesses, teamwork, communication,
  and interest in the role.
- Answers should be professional and based on the resume
  where appropriate.

Behavioral Questions:
- Generate exactly 10.
- Focus on real situations involving teamwork, conflict,
  problem-solving, leadership, deadlines, failure,
  adaptability, and decision-making.
- Suggested answers should follow a STAR-style structure
  when the resume provides enough information.
- Never invent a situation that is not supported by the resume.
- If no suitable example exists, say:
  "Prepare a truthful STAR example from your own experience."

Interview Tips:
- Generate exactly 8 practical preparation tips.
- Make them specific to the target role and candidate.
- Avoid generic advice where possible.

Difficulty:
Set one of:
- "Beginner"
- "Intermediate"
- "Advanced"

The difficulty should reflect the target role and job description.

OUTPUT RULES:

- Return exactly 10 technical questions.
- Return exactly 10 HR questions.
- Return exactly 10 behavioral questions.
- Return exactly 8 tips.
- Answers should normally be 2–5 sentences.
- Questions must be unique.
- Do not duplicate questions across categories.
- Escape JSON characters correctly.
- Return ONLY valid JSON.
"""

    text = generate(prompt)

    # =====================================================
    # Clean AI Markdown Wrappers
    # =====================================================

    text = text.strip()

    if text.startswith("```json"):

        text = text[
            len("```json"):
        ].strip()

        if text.endswith("```"):
            text = text[
                :-3
            ].strip()

    elif text.startswith("```"):

        text = text[
            len("```"):
        ].strip()

        if text.endswith("```"):
            text = text[
                :-3
            ].strip()

    # =====================================================
    # Parse JSON
    # =====================================================

    try:

        report = json.loads(text)

        # -------------------------------------------------
        # Ensure required fields exist
        # -------------------------------------------------

        report.setdefault(
            "job_role",
            "Unknown",
        )

        report.setdefault(
            "difficulty",
            "Unknown",
        )

        report.setdefault(
            "technical_questions",
            [],
        )

        report.setdefault(
            "hr_questions",
            [],
        )

        report.setdefault(
            "behavioral_questions",
            [],
        )

        report.setdefault(
            "tips",
            [],
        )

        return report

    except json.JSONDecodeError:

        return {
            "job_role": "Unknown",
            "difficulty": "Unknown",
            "technical_questions": [],
            "hr_questions": [],
            "behavioral_questions": [],
            "tips": [
                "Unable to process the AI interview response.",
                "Please try generating the interview guide again.",
            ],
        }