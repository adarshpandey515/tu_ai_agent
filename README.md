# TU AI Agent

Minimal Python project using Groq AI with model `meta-llama/llama-4-scout-17b-16e-instruct`.

## Setup
- Install Python 3.10+.
- Create and activate a virtual environment (recommended).
- Install dependencies:

```
pip install -r requirements.txt
```

- Set your Groq API key in the environment:

```
export GROQ_API_KEY="<your-key>"
# Optional override:
export GROQ_MODEL="meta-llama/llama-4-scout-17b-16e-instruct"
```

You can also copy `.env.example` to `.env` and export variables manually.

## Run
- Via main entry:

```
python main.py "Explain the significance of data structures"
```

- Or pipe input:

```
echo "Summarize the assignment requirements" | python main.py
```

- Direct CLI:

```
python cli.py -t 0.2 -m 1024 "Provide a brief overview of the dataset"
```

## Assignment Pipeline
- Install extra deps:

```
pip install -r requirements.txt
```

- Run the assignment end-to-end (reads `Data Input.pdf`, writes `output/output.xlsx`):

```
python -m tasks.assignment
```

- Output contains two sheets:
	- First sheet: Full model response (name mimics first sheet in `Expected Output.xlsx` if available)
	- Second sheet: Parsed sections (name mimics second sheet in `Expected Output.xlsx` if available)

### Make output match `Expected Output.xlsx`
- Place `Expected Output.xlsx` in the repo root (already present).
- The writer will copy its sheet names when generating `output/output.xlsx`.
- If you need exact column headers/order, share the expected schema and I will update `tasks/writer.py` to format accordingly (headers, types, ordering).

## Files
- `src/groq_client.py`: Groq client wrapper.
- `src/config.py`: Env-based configuration helpers.
- `cli.py`: Simple CLI to send a prompt and print the response.
- `main.py`: Entrypoint delegating to CLI.
- `tasks/assignment.py`: Assignment runner that reads PDF and writes Excel.
- `tasks/pdf_reader.py`: PDF text extraction using `pdfplumber`.
- `tasks/writer.py`: Excel writer using `pandas`/`openpyxl`.
- `requirements.txt`: Python dependencies.
- `.env.example`: Example environment variables.

## Notes
- If `GROQ_API_KEY` is missing, the app exits with a helpful error.
- Temperature and max tokens are configurable via CLI flags.