from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


def generate_ats_report(report):
    """
    Generate a professional ATS analysis PDF report.

    Returns:
        BytesIO: PDF file in memory.
    """

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )

    styles = getSampleStyleSheet()

    # =====================================================
    # Custom Styles
    # =====================================================

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=24,
        leading=30,
        alignment=TA_CENTER,
        spaceAfter=8,
    )

    subtitle_style = ParagraphStyle(
        "ReportSubtitle",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.grey,
        spaceAfter=20,
    )

    section_style = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontSize=15,
        leading=20,
        spaceBefore=12,
        spaceAfter=8,
    )

    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontSize=10,
        leading=15,
        spaceAfter=5,
    )

    score_style = ParagraphStyle(
        "Score",
        parent=styles["Heading1"],
        fontSize=30,
        leading=36,
        alignment=TA_CENTER,
    )

    # =====================================================
    # Helper
    # =====================================================

    def safe_value(key, default="Unavailable"):
        value = report.get(key, default)

        if value is None:
            return default

        return str(value)

    def list_items(items):
        if not items:
            return [
                Paragraph(
                    "None identified.",
                    body_style,
                )
            ]

        return [
            Paragraph(
                f"• {str(item)}",
                body_style,
            )
            for item in items
        ]

    # =====================================================
    # Report Data
    # =====================================================

    ats_score = int(
        report.get(
            "ats_score",
            0,
        )
    )

    keyword_match = int(
        report.get(
            "keyword_match",
            0,
        )
    )

    skills_match = int(
        report.get(
            "skills_match",
            0,
        )
    )

    experience_match = int(
        report.get(
            "experience_match",
            0,
        )
    )

    education_match = int(
        report.get(
            "education_match",
            0,
        )
    )

    # =====================================================
    # Story
    # =====================================================

    story = []

    story.append(
        Paragraph(
            "AI Resume Copilot",
            title_style,
        )
    )

    story.append(
        Paragraph(
            "ATS Resume Analysis Report",
            subtitle_style,
        )
    )

    # =====================================================
    # ATS Score
    # =====================================================

    story.append(
        Paragraph(
            "ATS SCORE",
            section_style,
        )
    )

    score_table = Table(
        [
            [
                Paragraph(
                    f"<b>{ats_score}%</b>",
                    score_style,
                ),
                Paragraph(
                    f"<b>{safe_value('overall_match')}</b>",
                    body_style,
                ),
            ]
        ],
        colWidths=[
            55 * mm,
            115 * mm,
        ],
    )

    score_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    colors.whitesmoke,
                ),
                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    0.8,
                    colors.lightgrey,
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "ALIGN",
                    (0, 0),
                    (0, 0),
                    "CENTER",
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    12,
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    12,
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    15,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    15,
                ),
            ]
        )
    )

    story.append(score_table)

    story.append(Spacer(1, 10))

    # =====================================================
    # Job Role
    # =====================================================

    story.append(
        Paragraph(
            "Target Job Role",
            section_style,
        )
    )

    story.append(
        Paragraph(
            safe_value("job_role"),
            body_style,
        )
    )

    # =====================================================
    # Match Metrics
    # =====================================================

    story.append(
        Paragraph(
            "Match Analysis",
            section_style,
        )
    )

    metrics = [
        [
            "Category",
            "Match",
        ],
        [
            "Keyword Match",
            f"{keyword_match}%",
        ],
        [
            "Skills Match",
            f"{skills_match}%",
        ],
        [
            "Experience Match",
            f"{experience_match}%",
        ],
        [
            "Education Match",
            f"{education_match}%",
        ],
    ]

    metrics_table = Table(
        metrics,
        colWidths=[
            120 * mm,
            50 * mm,
        ],
    )

    metrics_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#1E293B"),
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white,
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.lightgrey,
                ),
                (
                    "ALIGN",
                    (1, 1),
                    (1, -1),
                    "CENTER",
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    8,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    8,
                ),
            ]
        )
    )

    story.append(metrics_table)

    # =====================================================
    # Skills
    # =====================================================

    story.append(
        Paragraph(
            "Matched Skills",
            section_style,
        )
    )

    story.extend(
        list_items(
            report.get(
                "matched_skills",
                [],
            )
        )
    )

    story.append(
        Paragraph(
            "Missing Skills",
            section_style,
        )
    )

    story.extend(
        list_items(
            report.get(
                "missing_skills",
                [],
            )
        )
    )

    # =====================================================
    # Strengths
    # =====================================================

    story.append(
        Paragraph(
            "Resume Strengths",
            section_style,
        )
    )

    story.extend(
        list_items(
            report.get(
                "strengths",
                [],
            )
        )
    )

    # =====================================================
    # Weaknesses
    # =====================================================

    story.append(
        Paragraph(
            "Areas to Improve",
            section_style,
        )
    )

    story.extend(
        list_items(
            report.get(
                "weaknesses",
                [],
            )
        )
    )

    # =====================================================
    # Recommendations
    # =====================================================

    story.append(
        Paragraph(
            "AI Recommendations",
            section_style,
        )
    )

    story.extend(
        list_items(
            report.get(
                "suggestions",
                [],
            )
        )
    )

    # =====================================================
    # Interview Probability
    # =====================================================

    story.append(
        Paragraph(
            "Interview Probability",
            section_style,
        )
    )

    story.append(
        Paragraph(
            safe_value(
                "interview_probability"
            ),
            body_style,
        )
    )

    # =====================================================
    # Final Verdict
    # =====================================================

    story.append(
        Paragraph(
            "Final Verdict",
            section_style,
        )
    )

    story.append(
        Paragraph(
            safe_value(
                "verdict"
            ),
            body_style,
        )
    )

    # =====================================================
    # Footer
    # =====================================================

    story.append(
        Spacer(
            1,
            15,
        )
    )

    story.append(
        Paragraph(
            "Generated by AI Resume Copilot • 2026",
            subtitle_style,
        )
    )

    # =====================================================
    # Build PDF
    # =====================================================

    document.build(story)

    buffer.seek(0)

    return buffer