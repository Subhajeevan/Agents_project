from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import pdfplumber

class ResumeAnalyzer:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    
    def extract_text(self, resume_path):
        with pdfplumber.open(resume_path) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages)
    
    def analyze_resume(self, resume_text):
        prompt = ChatPromptTemplate.from_template("""
        Extract from this resume:
        - Skills (technical & soft)
        - Education
        - Work experience
        - Projects
        
        Return as JSON.
        
        Resume: {resume}
        """)
        chain = prompt | self.llm
        return chain.invoke({"resume": resume_text})