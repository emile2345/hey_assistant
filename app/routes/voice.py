from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.state import call_state
from app.services.tts import generate_voice

router = APIRouter()

@router.post("/voice/speak")
def speak():
    return FileResponse(
        "app/audio/output.mp3",
        media_type="audio/mpeg",
        filename="output.mp3"
    )
