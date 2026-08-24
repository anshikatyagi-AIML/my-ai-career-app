# AI Resume & Career Advisor 

An interactive AI-powered application designed to help job seekers optimize their resumes and prepare for interviews. By leveraging **LangChain** and **Google Gemini AI**, the application extracts text from resume and job description PDFs to deliver tailored match analysis and actionable career roadmaps.

##  Key Features

- **Resume vs. JD Analysis:** Evaluates candidate resumes against target job descriptions to generate an overall match score (0–100).
- **Skill Gap Identification:** Pinpoints missing or weak technical/soft skills required for the target role.
- **Strength Highlight:** Pinpoints key candidate strengths matching the job requirements.
- **Personalized Learning Plan:** Generates a structured 3-month roadmap to bridge skill gaps.
- **Interview Preparation:** Suggests top technical concepts and topics to revise prior to interviews.

##  Tech Stack

- **Frontend:** Streamlit
- **LLM Orchestration:** LangChain (`langchain-google-genai`, `langchain-core`)
- **AI Model:** Google Gemini (`gemini-3.6-flash`)
- **PDF Extraction:** PyPDF
- **Environment Management:** Python `dotenv`

##  Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/anshikatyagi-AIML/my-ai-career-app.git](https://github.com/anshikatyagi-AIML/my-ai-career-app.git)
   cd my-ai-career-app
