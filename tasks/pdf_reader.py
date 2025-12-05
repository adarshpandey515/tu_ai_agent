from pathlib import Path

def extract_text(pdf_path: Path) -> str:
    try:
        import pdfplumber  # type: ignore
    except Exception:
        # Fallback: minimal placeholder if lib not installed
        return f"[pdfplumber not installed] Could not read {pdf_path}."

    text_parts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            text_parts.append(text)
    return "\n\n".join(text_parts).strip()
