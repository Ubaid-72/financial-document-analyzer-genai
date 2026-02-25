# Financial Document Analyzer – Debug Assignment (Generative AI)

## Overview
AI-powered backend application built with **FastAPI** and **CrewAI** to analyze financial documents such as earnings reports and investor updates.  
This project focuses on **debugging an existing codebase**, resolving dependency issues, and improving prompt reliability in a multi-agent AI system.

---

## Features
- Upload financial PDF documents
- AI-driven financial analysis
- Risk assessment and investment insights
- REST API with Swagger UI

---

## Tech Stack
- Python 3.12
- FastAPI
- CrewAI
- LangChain OpenAI
- Uvicorn
- PyPDF

---

## Setup & Run

### 1. Create Virtual Environment

python -m venv venv312
venv312\Scripts\activate

2. Install Dependencies
pip install -r requirements.txt

3. Environment Variables
Create .env file:
OPENAI_API_KEY=your_openai_api_key_here

4. Start Server
uvicorn main:app --reload
Server:
http://127.0.0.1:8000
Swagger UI:
http://127.0.0.1:8000/docs

API Usage
POST /analyze
1.Upload a financial PDF
2.Optional query for analysis
Returns AI-generated financial insights.

Sample Document
Tesla Q2 2025 Financial Update
https://www.tesla.com/sites/default/files/downloads/TSLA-Q2-2025-Update.pdf

Debugging Summary
*Fixed CrewAI agent/task initialization issues
*Resolved dependency and version conflicts
*Improved prompts to reduce hallucinations

**Note
If you receive:
Error 429 – insufficient_quota
This is due to OpenAI billing limits, not an application error.

Author
Ubaidulla Makandar


---

This version is:
✅ Clean  
✅ Recruiter-friendly  
✅ GitHub-ready  
✅ Not over-explained  
