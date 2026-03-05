# AI Sales Research Agent

A Python automation tool that generates structured company research reports using web data and local LLMs.

## Problem
Sales and growth teams often spend significant time researching companies before outreach. This project automates initial company research.

## Solution
The tool:
1. Takes a company name as input
2. Collects company information from Wikipedia
3. Uses a local LLM (Ollama) to analyze the company
4. Generates a structured research brief

## Example Output

Industry: Financial Technology

Key Services:
- Payment processing
- Financial APIs
- Online business infrastructure

Potential Business Travel Needs:
- Client meetings
- Conferences
- Sales outreach

## Tech Stack
- Python
- Ollama (local LLM)
- Wikipedia API
- BeautifulSoup

## Run the Project

```bash
pip install -r requirements.txt
python research_agent.py