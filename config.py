from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
INTERNSHALA_EMAIL = os.getenv("INTERNSHALA_EMAIL")
INTERNSHALA_PASSWORD = os.getenv("INTERNSHALA_PASSWORD")
RESUME_PATH = "resume.pdf"  # Replace with your resume path