# AutoScholar

AutoScholar is a Python research assistant that turns a topic into a structured mini research report. It collects source notes, extracts key points, generates a summary, and exports a clean Markdown report with citations.

Built after the Google Kaggle 5-Day Intensive AI Workshop as a portfolio project to demonstrate practical AI, automation, prompt engineering, and research workflow design.

## Features

- Topic-based research workflow
- Source note collection from URLs or manual text
- Extractive summarization without requiring paid APIs
- Markdown report generation with citations
- Optional Streamlit interface
- Clean Python project structure for open-source contribution

## Demo

Example command:

```bash
python -m auto_researcher.cli "Impact of AI in education" --source examples/sample_sources.txt
```

Example output:

```text
reports/impact-of-ai-in-education.md
```

## Project Structure

```text
autoresearcher/
|-- auto_researcher/
|   |-- __init__.py
|   |-- cli.py
|   |-- report.py
|   |-- research.py
|   `-- text_utils.py
|-- examples/
|   `-- sample_sources.txt
|-- reports/
|   `-- sample-report.md
|-- app.py
|-- requirements.txt
|-- LICENSE
`-- README.md
```

## Tech Stack

- Python
- Streamlit
- Markdown
- AI research workflow design
- Natural language processing basics

## Installation

```bash
git clone https://github.com/HarshadaTS/autoresearcher.git
cd autoresearcher
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run the command-line app:

```bash
python -m auto_researcher.cli "Your research topic" --source examples/sample_sources.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

## How It Works

1. The user enters a research topic.
2. The app reads source notes from a text file or text box.
3. The summarizer ranks sentences based on relevance and frequency.
4. A Markdown report is generated with summary, key findings, and citations.

## Future Improvements

- Add web search integration
- Add Gemini/OpenAI API support
- Export reports as PDF
- Add source reliability scoring
- Add multi-language research support

## Author

Harshada TS  
GitHub: [HarshadaTS](https://github.com/HarshadaTS)
