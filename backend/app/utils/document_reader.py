from pathlib import Path
from pypdf import PdfReader
from docx import Document


def extract_text(file_path: str) -> str:
    """Extract text from PDF or DOCX files."""

    path = Path(file_path)

    if path.suffix.lower() == ".pdf":
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    elif path.suffix.lower() == ".docx":
        document = Document(file_path)
        return "\n".join(paragraph.text for paragraph in document.paragraphs)

    else:
        raise ValueError("Only PDF and DOCX files are supported.")