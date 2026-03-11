from fpdf import FPDF


def clean_text(text):
    """
    Remove characters FPDF cannot encode
    """
    return text.encode("latin-1", "replace").decode("latin-1")


def generate_pdf(text):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    # Clean text before writing
    text = clean_text(text)

    for line in text.split("\n"):
        pdf.multi_cell(0, 8, line)

    file_path = "research_report.pdf"
    pdf.output(file_path)

    return file_path