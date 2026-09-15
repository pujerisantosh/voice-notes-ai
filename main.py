from fastapi import FastAPI

app = FastAPI(title="Voice Notes AI")


@app.get("/")
def home():
    return {"message": "Voice Notes AI is running!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}