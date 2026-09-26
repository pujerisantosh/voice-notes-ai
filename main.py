from fastapi import FastAPI
from app.api.routes.audio import router as audio_router


app = FastAPI(title="Voice Notes AI")


app.include_router(audio_router, prefix="/audio", tags=["Audio"])


@app.get("/")
def home():
    return {"message": "Voice Notes AI is running!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}