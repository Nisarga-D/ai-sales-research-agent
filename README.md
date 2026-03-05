AI Sales Research Agent

A Python-powered AI tool that automates company research for B2B sales teams.

The application collects company information and generates structured research reports using a local LLM.

## Features

- Automated company research
- AI-generated business insights
- Structured research reports
- Downloadable reports
- Simple web interface built with Streamlit

## Demo

### Input Interface
<img width="1902" height="825" alt="Screenshot 2026-03-05 164102" src="https://github.com/user-attachments/assets/4aa4c595-3822-4213-a41b-43b11d6a0a98" />



### Generated Research Report
<img width="1019" height="782" alt="Screenshot 2026-03-05 164159" src="https://github.com/user-attachments/assets/74641633-52fd-47d9-8f7c-319c3461c3ea" />
<img width="689" height="775" alt="Screenshot 2026-03-05 164437" src="https://github.com/user-attachments/assets/4fd2207f-c3a1-4f3a-b625-3ab5c3b2ce0f" />
<img width="1147" height="723" alt="Screenshot 2026-03-05 164451" src="https://github.com/user-attachments/assets/6e416adf-95f4-4d19-ad32-19a00de46feb" />
<img width="1088" height="374" alt="Screenshot 2026-03-05 164500" src="https://github.com/user-attachments/assets/dfb3decb-6ebc-4f5c-a401-7c90749b2878" />

## How It Works

1. Enter a company name
2. The tool retrieves company information from Wikipedia
3. A local LLM analyzes the company
4. A structured research report is generated

## Tech Stack

- Python
- Streamlit
- Ollama (Local LLM)
- Wikipedia API

## Run the App

```bash
pip install -r requirements.txt
streamlit run app.py
