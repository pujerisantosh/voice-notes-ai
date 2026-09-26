from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.audio_service import AudioService


router = APIRouter()
audio_service = AudioService()


ALLOWED_AUDIO_TYPES = {
    "audio/mpeg",
    "audio/wav",
    "audio/mp4"
}


@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):

    print("🔥 ROUTE WAS CALLED")

    if file.content_type not in ALLOWED_AUDIO_TYPES:
        raise HTTPException(
            status_code=415,
            detail="Unsupported audio file type"
        )

    file_path = await audio_service.save_audio(file)

    return {
        "filename": file.filename,
        "content_type": file.content_type
    }