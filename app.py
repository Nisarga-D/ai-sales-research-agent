import streamlit as st
import ollama
from company_research import get_company_info

st.set_page_config(page_title="AI Sales Research Agent")

st.title("AI Sales Research Agent")

st.sidebar.title("About")
st.sidebar.write(
"""
AI-powered tool that automates company research for B2B sales teams.

Enter a company name to generate a structured research report including:
- Industry
- Products/Services
- Travel needs
- Business insights
"""
)

company = st.text_input("Enter company name")


def analyze_company(summary):

    prompt = f"""
You are helping a B2B sales team research a company.

Company description:
{summary}

Provide:

Industry
Key products/services
Potential business travel needs
Why this company might need travel management software
Short summary
"""

    response = ollama.chat(
        model='mistral',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response['message']['content']


if st.button("Generate Research Report"):

    if company.strip() == "":
        st.warning("Please enter a company name.")
    else:

        info = get_company_info(company)

        if info is None:
            st.error("Company information not found.")
        else:

            summary, url = info

            st.subheader("Company Source")
            st.write(url)

            st.subheader("Company Summary")
            st.write(summary)

            with st.spinner("Running AI analysis..."):
                report = analyze_company(summary)

            st.subheader("AI Research Report")
            st.write(report)

            st.download_button(
                label="Download Report",
                data=report,
                file_name=f"{company}_research_report.txt",
                mime="text/plain"
            )