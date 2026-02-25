# agents.py

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial text and provide factual insights.",
    backstory="Expert in reading earnings reports and financial disclosures.",
    llm=llm,
    verbose=True
)

verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify whether the content represents a financial document.",
    backstory="Experienced in financial compliance and reporting standards.",
    llm=llm,
    verbose=True
)

investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide balanced investment insights based on financial analysis.",
    backstory="Focuses on long-term value and risk-aware investing.",
    llm=llm,
    verbose=True
)

risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Identify financial and market risks in the document.",
    backstory="Specialist in financial risk and uncertainty analysis.",
    llm=llm,
    verbose=True
)