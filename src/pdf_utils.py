"""PDF text extraction helpers."""
from io import StringIO
from typing import Optional

from pdfminer.high_level import extract_text


def extract_text_from_pdf(path_or_file) -> str:
    """Extracts text from a PDF file path or a file-like object.

    Returns an empty string on failure.
    """
    try:
        # pdfminer accepts a path or file-like object
        text = extract_text(path_or_file)
        return text or ""
    except Exception:
        return ""
