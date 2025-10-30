# app.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"email": "24f3001857@ds.study.iitm.ac.in", "message": "Hello from Codespaces!"}

# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
