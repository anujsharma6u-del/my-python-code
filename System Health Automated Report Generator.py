import psutil
import platform
import socket
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib import getSampleStyleSheet, colors

def get_system_info():
    return {
        "Hostname": socket.gethostname(),
        "OS": platform.system() + " " + platform.release(),
        "Platform": platform.platform(),
        "CPU Cores": psutil.cpu_count(logical=True),
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "Total Memory (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
        "Used Memory (GB)": round(psutil.virtual_memory().used / (1024**3), 2),
        "Memory Usage (%)": psutil.virtual_memory().percent,
        "Disk Total (GB)": round(psutil.disk_usage('/').total / (1024**3), 2),
        "Disk Used (GB)": round(psutil.disk_usage('/').used / (1024**3), 2),
        "Disk Usage (%)": psutil.disk_usage('/').percent,
        "Network Interfaces": list(psutil.net_if_addrs().keys())
    }

def generate_pdf_report(data, filename="system_health_report.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title = Paragraph("System Health Report", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))

    # Date
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_para = Paragraph(f"Generated on: {date_str}", styles['Normal'])
    story.append(date_para)
    story.append(Spacer(1, 12))

    # System Info Table
    table_data = [["Parameter", "Value"]]
    for key, value in data.items():
        table_data.append([key, str(value)])

    table = Table(table_data)
    table.setStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    story.append(table)

    doc.build(story)

if __name__ == "__main__":
    info = get_system_info()
    generate_pdf_report(info)

     
