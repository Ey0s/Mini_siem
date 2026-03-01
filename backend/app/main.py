from fastapi import FastAPI

app = FastAPI(
    title="SecureSight SIEM",
    description="ML-Based Security Information and Event Management System",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "SecureSight backend is running"}