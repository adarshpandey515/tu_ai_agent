import sys
from pathlib import Path
from typing import Dict, Any

from src.groq_client import GroqClient, GroqError
from tasks.pdf_reader import extract_text
from tasks.writer import write_excel


def build_prompt(data_text: str) -> str:
    return (
        "You are given data extracted from a PDF. "
        "Analyze it and produce a concise, structured summary with key sections: "
        "Overview, Key Points, Action Items, and Data Table (if applicable). "
        "Use bullet points where helpful.\n\n"
        f"DATA:\n{data_text[:8000]}"
    )


def run(input_pdf: Path, out_path: Path) -> Path:
    text = extract_text(input_pdf)
    client = GroqClient()
    response = client.complete(build_prompt(text), temperature=0.2, max_tokens=1500)

    # Basic structured parse: keep raw, and split into sections
    sections: Dict[str, Any] = {"raw": response}
    for title in ["Overview", "Key Points", "Action Items", "Data Table"]:
        idx = response.find(title)
        if idx != -1:
            # naïve slice from section header to next section header
            nxt_idx = min([i for i in [response.find(t, idx + 1) for t in ["Overview", "Key Points", "Action Items", "Data Table"]] if i != -1] or [len(response)])
            sections[title] = response[idx:nxt_idx].strip()

    write_excel(out_path, sections)
    return out_path


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    input_pdf = Path("Data Input.pdf")
    output_xlsx = Path("output/output.xlsx")
    output_xlsx.parent.mkdir(parents=True, exist_ok=True)
    try:
        out = run(input_pdf, output_xlsx)
        print(f"Wrote: {out}")
        return 0
    except GroqError as ge:
        print(f"Error: {ge}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
