from fastapi import FastAPI

app = FastAPI(
    title="AI Customer Complaint Management System",
    description="AI-powered complaint management system for pharmaceutical manufacturing.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Customer Complaint Management System"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }