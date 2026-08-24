"""Generates assets/CV_AndreDeMattos.pdf, styled to match the site (same
self-hosted Source Serif 4 font, same palette). Run from anywhere:

    python3 scripts/build_resume.py

Requires: pip install reportlab
"""
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(REPO_ROOT, "assets", "fonts")
OUTPUT_PATH = os.path.join(REPO_ROOT, "assets", "CV_AndreDeMattos.pdf")

pdfmetrics.registerFont(TTFont("SourceSerif4", f"{FONT_DIR}/SourceSerif4-Regular.ttf"))
pdfmetrics.registerFont(TTFont("SourceSerif4-SemiBold", f"{FONT_DIR}/SourceSerif4-SemiBold.ttf"))
pdfmetrics.registerFont(TTFont("SourceSerif4-Italic", f"{FONT_DIR}/SourceSerif4-Italic.ttf"))
pdfmetrics.registerFontFamily(
    "SourceSerif4", normal="SourceSerif4", bold="SourceSerif4-SemiBold", italic="SourceSerif4-Italic"
)

INK = HexColor("#1a1a17")
INK_SOFT = HexColor("#4a4941")
INK_FAINT = HexColor("#8a8879")
ACCENT = HexColor("#0f4c3a")
LINE = HexColor("#e6e2d5")

name_style = ParagraphStyle("name", fontName="SourceSerif4-SemiBold", fontSize=22, leading=28, textColor=INK, spaceAfter=8)
eyebrow_style = ParagraphStyle("eyebrow", fontName="Courier", fontSize=9, textColor=INK_FAINT, spaceAfter=14)
statement_style = ParagraphStyle("statement", fontName="SourceSerif4-Italic", fontSize=11.5, textColor=INK_SOFT,
                                  leading=16, spaceAfter=14)
section_style = ParagraphStyle("section", fontName="SourceSerif4-SemiBold", fontSize=12, textColor=INK,
                                spaceBefore=16, spaceAfter=8)
role_style = ParagraphStyle("role", fontName="SourceSerif4-SemiBold", fontSize=10.5, textColor=INK)
org_style = ParagraphStyle("org", fontName="SourceSerif4-Italic", fontSize=9.5, textColor=ACCENT, spaceAfter=5)
date_style = ParagraphStyle("date", fontName="Courier", fontSize=8, textColor=INK_FAINT, alignment=TA_RIGHT)
bullet_style = ParagraphStyle("bullet", fontName="SourceSerif4", fontSize=9.5, textColor=INK_SOFT,
                               leading=13.5, spaceAfter=3, leftIndent=12)
dt_style = ParagraphStyle("dt", fontName="Courier", fontSize=8.5, textColor=INK_FAINT)
dd_style = ParagraphStyle("dd", fontName="SourceSerif4", fontSize=9.5, textColor=INK_SOFT, leading=13.5, spaceAfter=8)

doc = SimpleDocTemplate(
    OUTPUT_PATH, pagesize=A4,
    topMargin=20 * mm, bottomMargin=16 * mm, leftMargin=20 * mm, rightMargin=20 * mm,
    title="Andre de Mattos - CV", author="Andre de Mattos"
)

story = []

story.append(Paragraph("André de Mattos", name_style))
story.append(Paragraph("Data &amp; Analytics Manager", eyebrow_style))
story.append(Paragraph(
    "I help senior leadership deploy a data-driven culture, leading complex data initiatives "
    "from concept to delivery &mdash; ensuring quality, scalability, clear communication across "
    "teams, and measurable business impact.",
    statement_style
))
story.append(Paragraph(
    "andre.mtts@icloud.com &nbsp;|&nbsp; linkedin.com/in/andremnoliveira &nbsp;|&nbsp; github.com/andrmtts",
    ParagraphStyle("contact", fontName="Courier", fontSize=8.5, textColor=INK_SOFT)
))
story.append(Spacer(1, 4))
story.append(HRFlowable(width="100%", thickness=0.75, color=LINE, spaceAfter=2))

def role(title, org_loc, dates, bullets):
    story.append(Spacer(1, 9))
    t = Table([[Paragraph(title, role_style), Paragraph(dates.replace(" ", "&nbsp;"), date_style)]],
              colWidths=[122 * mm, 38 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(t)
    story.append(Paragraph(org_loc, org_style))
    for b in bullets:
        story.append(Paragraph(f"&ndash;&nbsp;&nbsp;{b}", bullet_style))

story.append(Paragraph("EXPERIENCE — nine years across banking, industrial and public-sector analytics", section_style))

role("Manager, Data &amp; Analytics", "Grupo Qaracter Consulting — Madrid, Spain", "Jun 2025 — Present", [
    "Managed and expanded the Business Intelligence consulting service to <b>€600K</b> in annual revenue.",
    "Part-time at BBVA: BI advisor on product development for Global Transactional Banking; built operational dashboards on GCP (Data Studio, BigQuery).",
    "Part-time for Oracle LS: built an E2E pipeline on Azure from vendor SFTP drops to templated reports with masked PII.",
    "Authored technical proposals for public-sector tenders, securing new client contracts in Mexico and Spain.",
])

role("Senior Business Intelligence Consultant", "BNP Paribas (via Grupo Qaracter) — Madrid, Spain", "Aug 2023 — May 2025", [
    "Led multidisciplinary, multicultural teams through agile delivery cycles; implemented CI/CD to streamline delivery.",
    "Administered Alteryx, Tableau and Power BI server environments across Corporate &amp; Investment Banking (CIB).",
    "Reduced processing time of a critical data pipeline by <b>65%</b> by removing intermediary outputs and restructuring data joins.",
])

role("Business Intelligence Consultant", "BNP Paribas (via Grupo Qaracter) — Madrid, Spain", "Jun 2022 — Jul 2023", [
    "Built financial reports for the Country CFO office, averaging 2K quarterly views.",
    "Presented roadmap and usage statistics to C-level audiences in SteerCo meetings.",
    "Handled high-complexity requirements: multiple data source connections, row-level security, sensitive data governance.",
])

role("Business Intelligence Analyst, Supply Chain", "Aker Solutions — Curitiba, Brazil", "Jul 2020 — Apr 2021", [
    "Built analytics apps to track supplier delivery delays, helping recover more than <b>R$6M</b> in financial impact.",
    "Led Supply Chain digitization under the 2021 'Digital Journey' program (Six Sigma/DMAIC), saving over <b>R$2M</b>.",
])

role("Jr. Business Intelligence Analyst, Procurement", "Aker Solutions — Curitiba, Brazil", "Aug 2018 — Jul 2020", [
    "Built a Procurement &amp; Logistics KPI cockpit (OTIF, lead time, spend, inventory turnover) from SAP data.",
])

story.append(Paragraph("EDUCATION", section_style))
role("Data Science Bootcamp", "ID Digital School, Madrid, Spain — 432 hours", "2021", [
    "Built an NLP/ML job-recommender system ranking 18K+ scraped EU job listings.",
])
role("B.Eng. Industrial Engineering", "PUCPR, Curitiba, Brazil", "2018", [])
role("Computer Networks, Exchange Year", "Halmstad University, Sweden", "2016", [
    "Science without Borders scholarship, Brazilian Federal Government.",
])

story.append(Paragraph("SKILLS", section_style))

def skill_row(term, definition):
    t = Table([[Paragraph(term, dt_style), Paragraph(definition, dd_style)]],
              colWidths=[28 * mm, 132 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(t)

skill_row("Expert", "Tableau, Alteryx, Google Data Studio, Excel")
skill_row("Proficient", "Python (PySpark, Scikit-learn, Pandas, NLTK), SQL/T-SQL, BigQuery, Power BI, Databricks, "
                         "Snowflake, Git, Spark, dbt, Azure Data Factory, MS Fabric, VBA, PowerShell, Linux, "
                         "Cloud (AWS/GCP), AI-assisted dev (Claude Code, Devin, GitHub Actions, SonarQube, Jira integration)")
skill_row("Other", "Docker, Jenkins, JavaScript, R, MongoDB, Hadoop, database administration")
skill_row("Languages", "Portuguese (native), English (fluent), Spanish (fluent)")

doc.build(story)
print(f"Wrote {OUTPUT_PATH}")
