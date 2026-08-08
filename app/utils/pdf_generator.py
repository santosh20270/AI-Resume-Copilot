from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)


def generate_pdf(markdown_text):
    """
    Generate a PDF from rewritten resume text.
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

    story = []

    lines = markdown_text.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            story.append(
                Spacer(
                    1,
                    6,
                )
            )
            continue

        # Markdown headings
        if line.startswith("# "):

            story.append(
                Paragraph(
                    line[2:].strip(),
                    styles["Title"],
                )
            )

        elif line.startswith("## "):

            story.append(
                Paragraph(
                    line[3:].strip(),
                    styles["Heading2"],
                )
            )

        elif line.startswith("### "):

            story.append(
                Paragraph(
                    line[4:].strip(),
                    styles["Heading3"],
                )
            )

        # Bullet points
        elif line.startswith("- "):

            story.append(
                Paragraph(
                    f"• {line[2:].strip()}",
                    styles["BodyText"],
                )
            )

        else:

            story.append(
                Paragraph(
                    line,
                    styles["BodyText"],
                )
            )

        story.append(
            Spacer(
                1,
                4,
            )
        )

    document.build(story)

    buffer.seek(0)

    return buffer