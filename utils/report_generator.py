from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def generate_report(
    filename,
    ats_score,
    found_skills,
    missing_skills,
    suggestions
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Resume Analysis Report</b>", styles["Title"]))

    story.append(Paragraph(f"ATS Score: {ats_score}%", styles["Normal"]))

    story.append(Paragraph("<b>Skills Found</b>", styles["Heading2"]))

    for skill in found_skills:
        story.append(Paragraph(skill, styles["Normal"]))

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    for skill in missing_skills:
        story.append(Paragraph(skill, styles["Normal"]))

    story.append(Paragraph("<b>Suggestions</b>", styles["Heading2"]))

    for suggestion in suggestions:
        story.append(Paragraph(suggestion, styles["Normal"]))

    doc.build(story)