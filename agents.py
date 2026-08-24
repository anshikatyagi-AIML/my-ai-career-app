import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

def analyze_resume(resume_text, jd_context):
    prompt = PromptTemplate.from_template(
        """You are an expert Resume Reviewer.
        Compare the candidate's Resume against the provided Job Description context.
        
        Resume: {resume}
        Job Description Context: {jd}
        
        Provide:
        1. Overall Resume Match Score (0 to 100)
        2. List of Missing/Weak Skills
        3. 3 Key Strengths
        """
    )
    chain = prompt | llm
    return chain.invoke({"resume": resume_text, "jd": jd_context}).content

def generate_career_roadmap(resume_analysis, jd_context):
    prompt = PromptTemplate.from_template(
        """You are a Career Advisor.
        Based on this resume analysis and job description, provide:
        1. Interview Preparation Roadmap (Top 5 topics to revise)
        2. Personalized 3-Month Learning Plan to bridge missing skills
        
        Analysis: {analysis}
        Job Description: {jd}
        """
    )
    chain = prompt | llm
    return chain.invoke({"analysis": resume_analysis, "jd": jd_context}).content