# main.py

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from task import verify_document, analyze_financial_document, risk_assessment, investment_analysis
from tools import extract_pdf_text

app = FastAPI(title="Financial Document Analyzer")


def run_crew(query: str, document_text: str):
    crew = Crew(
        agents=[
            verifier,
            financial_analyst,
            risk_assessor,
            investment_advisor
        ],
        tasks=[
            verify_document,
            analyze_financial_document,
            risk_assessment,
            investment_analysis
        ],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff(
        inputs={
            "query": query,
            "document_text": document_text
        }
    )


@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        document_text = extract_pdf_text(file_path)

        response = run_crew(query, document_text)

        return {
            "status": "success",
            "analysis": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)