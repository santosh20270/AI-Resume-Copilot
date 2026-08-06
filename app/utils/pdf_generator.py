from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def generate_pdf(report: dict):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    # -------------------------------------------------------
    # Title
    # -------------------------------------------------------

    story.append(Paragraph("<b>AI Resume Copilot - ATS Report</b>", styles["Title"]))
    story.append(Spacer(1, 20))

    # -------------------------------------------------------
    # Basic Information
    # -------------------------------------------------------

    story.append(Paragraph(f"<b>ATS Score:</b> {report['ats_score']}/100", styles["Heading2"]))
    story.append(Paragraph(f"<b>Job Role:</b> {report['job_role']}", styles["Normal"]))
    story.append(Paragraph(f"<b>Overall Match:</b> {report['overall_match']}", styles["Normal"]))
    story.append(Paragraph(f"<b>Interview Chance:</b> {report['interview_probability']}", styles["Normal"]))

    story.append(Spacer(1, 15))

    # -------------------------------------------------------
    # Match Analysis
    # -------------------------------------------------------

    story.append(Paragraph("<b>Match Analysis</b>", styles["Heading2"]))

    story.append(Paragraph(f"Keyword Match: {report['keyword_match']}%", styles["Normal"]))
    story.append(Paragraph(f"Skills Match: {report['skills_match']}%", styles["Normal"]))
    story.append(Paragraph(f"Experience Match: {report['experience_match']}%", styles["Normal"]))
    story.append(Paragraph(f"Education Match: {report['education_match']}%", styles["Normal"]))

    story.append(Spacer(1, 15))

    # -------------------------------------------------------
    # Matched Skills
    # -------------------------------------------------------

    story.append(Paragraph("<b>Matched Skills</b>", styles["Heading2"]))

    for skill in report["matched_skills"]:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Spacer(1, 15))

    # -------------------------------------------------------
    # Missing Skills
    # -------------------------------------------------------

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    for skill in report["missing_skills"]:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Spacer(1, 15))

    # -------------------------------------------------------
    # Strengths
    # -------------------------------------------------------

    story.append(Paragraph("<b>Strengths</b>", styles["Heading2"]))

    for item in report["strengths"]:
        story.append(Paragraph(f"• {item}", styles["Normal"]))

    story.append(Spacer(1, 15))

    # -------------------------------------------------------
    # Weaknesses
    # -------------------------------------------------------

    story.append(Paragraph("<b>Weaknesses</b>", styles["Heading2"]))

    for item in report["weaknesses"]:
        story.append(Paragraph(f"• {item}", styles["Normal"]))

    story.append(Spacer(1, 15))

    # -------------------------------------------------------
    # Suggestions
    # -------------------------------------------------------

    story.append(Paragraph("<b>ATS Improvement Suggestions</b>", styles["Heading2"]))

    for item in report["suggestions"]:
        story.append(Paragraph(f"• {item}", styles["Normal"]))

    story.append(Spacer(1, 15))

    # -------------------------------------------------------
    # Verdict
    # -------------------------------------------------------

    story.append(Paragraph("<b>Recruiter Verdict</b>", styles["Heading2"]))
    story.append(Paragraph(report["verdict"], styles["Normal"]))

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf