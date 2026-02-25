# task.py

from crewai import Task
from agents import financial_analyst, verifier, investment_advisor, risk_assessor

verify_document = Task(
    description="Determine whether the provided text is a financial document.",
    expected_output="Confirmation with justification.",
    agent=verifier
)

analyze_financial_document = Task(
    description=(
        "Analyze the financial text and extract key insights such as revenue trends, "
        "profitability, cash flow, and outlook."
    ),
    expected_output="Structured financial analysis.",
    agent=financial_analyst
)

risk_assessment = Task(
    description="Identify financial and market risks mentioned or implied.",
    expected_output="List of risks with explanation.",
    agent=risk_assessor
)

investment_analysis = Task(
    description="Provide realistic investment insights based on the analysis.",
    expected_output="Balanced investment recommendations.",
    agent=investment_advisor
)