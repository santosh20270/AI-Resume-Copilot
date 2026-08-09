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
    Analyze the candidate's skill gap against a target job.
    """

    prompt = f"""
You are a Senior Career Coach, ATS Specialist,
Technical Recruiter, and Learning Roadmap Advisor.

Analyze the candidate's actual skills against the target
job description.

IMPORTANT:

The analysis must remain truthful and evidence-based.

RULES:

1. Never invent skills the candidate already possesses.
2. Never assume experience that is not supported by the resume.
3. Only place a skill in matched_skills when it is clearly
   supported by the resume.
4. Place required job skills that are not supported by the
   resume in missing_skills.
5. Do not treat a skill as matched simply because it appears
   in the job description.
6. Do not invent certifications the candidate already has.
7. Recommended certifications must be relevant to the target role.
8. Recommended projects should be realistic portfolio projects
   that help close the identified skill gaps.
9. The learning roadmap must prioritize the most important
   missing skills first.
10. Avoid generic recommendations whenever the job description
    provides enough information for specific recommendations.

RESUME:

{resume_text}


TARGET JOB DESCRIPTION:

{job_description}


RETURN FORMAT:

Return ONLY valid JSON.

Do NOT return Markdown.
Do NOT return explanations.
Do NOT wrap the JSON in a code block.

Return exactly:

{{
    "overall_readiness": "",
    "matched_skills": [],
    "missing_skills": [],
    "learning_roadmap": [],
    "recommended_projects": [],
    "recommended_certifications": [],
    "estimated_learning_time": ""
}}

FIELD REQUIREMENTS:

overall_readiness:
- Give a concise assessment such as:
  "Strong readiness"
  "Moderate readiness"
  "Needs improvement"
  "Early-stage readiness"
- Base this assessment on the candidate's actual skills
  versus the requirements of the target role.

matched_skills:
- Include only skills clearly supported by the resume.
- Prefer concrete technical skills and relevant professional skills.
- Do not duplicate skills.

missing_skills:
- Include important skills required by the job description
  that are not clearly supported by the resume.
- Prioritize skills that have a strong impact on candidate
  suitability.
- Do not include irrelevant requirements.

learning_roadmap:
- Generate exactly 8 to 10 ordered steps.
- Start with the highest-priority skill gaps.
- Move from fundamentals to practical application.
- Include hands-on practice where appropriate.
- Make each step actionable.
- Do not claim the candidate already knows a skill that is
  being recommended for learning.

recommended_projects:
- Generate exactly 5 project ideas.
- Each project must help address one or more missing skills.
- Projects should be realistic for a student or early-career
  candidate.
- Prefer projects that can be demonstrated in a GitHub portfolio.
- Do not claim these projects have already been completed.

recommended_certifications:
- Generate exactly 5 relevant certification recommendations.
- Recommend certifications based on the target role and
  identified skill gaps.
- Do not state that the candidate already holds them.

estimated_learning_time:
- Give a realistic approximate timeframe such as:
  "6–8 weeks"
  "2–3 months"
  "3–4 months"
- Base it on the number and complexity of the missing skills.

QUALITY REQUIREMENTS:

- matched_skills must not contain duplicates.
- missing_skills must not contain duplicates.
- learning_roadmap must contain 8–10 steps.
- recommended_projects must contain exactly 5 items.
- recommended_certifications must contain exactly 5 items.
- Return valid JSON only.
"""

    text = generate(prompt)

    # =====================================================
    # Clean Markdown Code Fences
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
            "overall_readiness",
            "Unknown",
        )

        report.setdefault(
            "matched_skills",
            [],
        )

        report.setdefault(
            "missing_skills",
            [],
        )

        report.setdefault(
            "learning_roadmap",
            [],
        )

        report.setdefault(
            "recommended_projects",
            [],
        )

        report.setdefault(
            "recommended_certifications",
            [],
        )

        report.setdefault(
            "estimated_learning_time",
            "Unknown",
        )

        return report

    except json.JSONDecodeError:

        return {
            "overall_readiness": "Unknown",
            "matched_skills": [],
            "missing_skills": [],
            "learning_roadmap": [
                "Unable to generate the learning roadmap.",
                "Please try the skill-gap analysis again.",
            ],
            "recommended_projects": [],
            "recommended_certifications": [],
            "estimated_learning_time": "Unknown",
        }