import streamlit as st
from rag_engine import extract_text_from_pdf, build_vector_store
from agents import analyze_resume, generate_career_roadmap

st.title("AI Resume & Career Advisor")

uploaded_resume = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
uploaded_jd = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])

if st.button("Analyze & Generate Plan") and uploaded_resume and uploaded_jd:
    with st.spinner("Processing documents with AI..."):
        resume_text = extract_text_from_pdf(uploaded_resume)
        jd_text = extract_text_from_pdf(uploaded_jd)
        
        retriever = build_vector_store(jd_text)
        relevant_jd = retriever.invoke("Key requirements and required skills")
        jd_context = "\n".join([doc.page_content for doc in relevant_jd])
        
        analysis = analyze_resume(resume_text, jd_context)
        roadmap = generate_career_roadmap(analysis, jd_context)
        
        st.subheader("📊 Resume Analysis & Score")
        st.write(analysis)
        
        st.subheader("🗺️ Career & Interview Roadmap (3-Month Plan)")
        st.write(roadmap)