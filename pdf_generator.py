from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(cluster_id, summary):

    filename = f"Cluster_{cluster_id}_Hazard_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Aviation Safety Hazard Review</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Cluster:</b> {cluster_id}", styles["Heading2"]))

    summary = summary.replace("\n", "<br/>")

    story.append(Paragraph(summary, styles["BodyText"]))

    doc.build(story)

    return filename