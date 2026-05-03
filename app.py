from __future__ import annotations

import streamlit as st

from auto_researcher.report import render_markdown
from auto_researcher.research import build_research, parse_source_file


st.set_page_config(page_title="Auto Researcher AI", page_icon="AI", layout="wide")

st.title("Auto Researcher AI")
st.caption("Generate structured research notes from source text.")

topic = st.text_input("Research topic", value="Impact of AI in education")
source_text = st.text_area(
    "Source notes",
    height=260,
    value="""Title: AI in Education
URL: https://example.com/ai-education
Artificial intelligence is changing education through personalized learning, automated feedback, and intelligent tutoring systems. AI tools can help teachers reduce repetitive work and support students with adaptive practice.
---
Title: Responsible AI Learning
URL: https://example.com/responsible-ai
Responsible use of AI in education requires privacy protection, transparent systems, and human oversight. Schools should verify AI-generated information and avoid replacing teachers with automated tools.""",
)

if st.button("Generate Report", type="primary"):
    sources = parse_source_file(source_text)
    result = build_research(topic, sources)
    markdown_report = render_markdown(result)

    st.subheader("Generated Report")
    st.markdown(markdown_report)
    st.download_button(
        "Download Markdown",
        data=markdown_report,
        file_name="research-report.md",
        mime="text/markdown",
    )
