import math
import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Table, TableStyle

from adapter.util.table import get_table_data, get_date, get_dict_from_table


def create_pdf(date, wines, output_pdf, client_name):
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)

    # Calculate the number of tables needed
    num_wines = len(wines)
    num_tables = math.ceil(num_wines / 6)

    # Create a list to hold all the elements (tables and page breaks)
    elements = []

    # Add title to the document
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    title_text = Paragraph(client_name, title_style)
    elements.append(title_text)

    # Add subtitle to the document
    subtitle_style = ParagraphStyle(name='SubtitleStyle', parent=styles['Normal'], alignment=TA_CENTER)
    subtitle_text = Paragraph(date, subtitle_style)
    elements.append(subtitle_text)

    # Create tables with up to 6 wines each
    for table_num in range(num_tables):
        # Add a page break before every table except the first one
        if table_num > 0:
            elements.append(PageBreak())

        start_index = table_num * 6
        end_index = min((table_num + 1) * 6, num_wines)
        wines_subset = wines[start_index:end_index]

        # Extract headers and keys for other parameters
        header = [""] + [wine["vino"] for wine in wines_subset]
        keys = list(wines_subset[0].keys())[1:]  # Exclude "vino"

        # Define the data for the table
        table_data = [header]  # Insert header row
        for key in keys:
            row = [key] + [wine[key] for wine in wines_subset]
            table_data.append(row)

        # Create the table style
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background color
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center-align content
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Even row background color
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),  # Content text color
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical alignment
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add grid lines
        ])

        # Create the table object
        table = Table(table_data)
        table.setStyle(table_style)

        # Add the table to the list of elements
        elements.append(table)

    # Build the PDF document with all the elements
    doc.build(elements)

    print("PDF successfully created at ", os.path.abspath(output_pdf))


def convert_to_proper_pdf(input_pdf, output_pdf, client_name):
    table_data = get_table_data(input_pdf)
    date = get_date(table_data)
    wines_dict = get_dict_from_table(table_data)
    create_pdf(date, wines_dict, output_pdf, client_name)
