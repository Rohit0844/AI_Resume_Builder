from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from tkinter import messagebox
import sqlite3
import os

styles = getSampleStyleSheet()

def generate_pdf():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        name,
        email,
        phone,
        address,
        skills,
        education,
        projects
    FROM resumes
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()
    conn.close()

    if not row:
        messagebox.showerror("Error", "No resume found!")
        return

    name, email, phone, address, skills, education, projects = row

    filename = f"{name}_Resume.pdf"

    pdf = SimpleDocTemplate(filename, pagesize=A4)
    story = []

    # Title
    story.append(Paragraph(f"<font size=22><b>{name}</b></font>", styles["Title"]))
    story.append(Paragraph(email, styles["Normal"]))
    story.append(Paragraph(phone, styles["Normal"]))
    story.append(Paragraph(address, styles["Normal"]))
    story.append(Spacer(1, 12))

    # Education
    story.append(Paragraph("<b>EDUCATION</b>", styles["Heading2"]))
    story.append(Paragraph(education.replace("\n", "<br/>"), styles["Normal"]))
    story.append(Spacer(1, 12))

    # Skills
    story.append(Paragraph("<b>SKILLS</b>", styles["Heading2"]))
    story.append(Paragraph(skills.replace("\n", "<br/>"), styles["Normal"]))
    story.append(Spacer(1, 12))

    # Projects
    story.append(Paragraph("<b>PROJECTS</b>", styles["Heading2"]))
    story.append(Paragraph(projects.replace("\n", "<br/>"), styles["Normal"]))
    story.append(Spacer(1, 12))

    pdf.build(story)

    os.startfile(filename)

    messagebox.showinfo(
        "Success",
        f"Resume PDF generated successfully!\n\n{filename}"
    )