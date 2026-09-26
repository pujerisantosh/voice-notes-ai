import os

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class AudioService:

    async def save_audio(self, file):
        file_path = os.path.abspath(
            os.path.join(UPLOAD_DIR, file.filename)
        )

        print("🔥 SAVING FILE TO:", file_path)

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        print("🔥 FILE EXISTS:", os.path.exists(file_path))

        return file_path