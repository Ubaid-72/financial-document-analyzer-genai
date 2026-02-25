# tools.py

from pypdf import PdfReader


def extract_pdf_text(file_path: str) -> str:
    """Extracts text from a PDF file"""
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text if text.strip() else "No readable text found in document."