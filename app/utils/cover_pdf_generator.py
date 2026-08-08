from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)


def generate_cover_pdf(cover_letter):
    """
    Generate a PDF from an AI-generated cover letter.
    """

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=22 * mm,
        leftMargin=22 * mm,
        topMargin=22 * mm,
        bottomMargin=22 * mm,
    )

    styles = getSampleStyleSheet()

    story = []

    for line in cover_letter.splitlines():

        line = line.strip()

        if not line:
            story.append(
                Spacer(
                    1,
                    8,
                )
            )
            continue

        # Markdown heading
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

        # Bullet point
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
                5,
            )
        )

    document.build(story)

    buffer.seek(0)

    return buffer