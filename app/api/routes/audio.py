import os
from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()


UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


ALLOWED_AUDIO_TYPES = {
    "audio/mpeg",
    "audio/wav",
    "audio/mp4"
}


@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):

    if file.content_type not in ALLOWED_AUDIO_TYPES:
        raise HTTPException(
            status_code=415,
            detail="Unsupported audio file type"
        )

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    return {
        "filename": file.filename,
        "content_type": file.content_type
    }