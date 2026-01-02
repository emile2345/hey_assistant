from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.state import call_state
from app.services.tts import generate_voice

router = APIRouter(prefix="/voice", tags=["Voice"])

@router.post("/speak")
def speak():
    if call_state["status"] != "in_call":
        raise HTTPException(status_code=400, detail="Call not active")

    text = "Bonjour, je suis HEY Assistant. Je suis prêt à vous aider."

    audio_path = generate_voice(text)
    return FileResponse(audio_path, media_type="audio/mpeg")

