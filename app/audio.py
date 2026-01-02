# -*- coding: utf-8 -*-

from fastapi import APIRouter

router = APIRouter()

# état audio simulé
audio_state = {
    "last_input": None,
    "last_output": None
}


@router.post("/audio/input")
async def audio_input(payload: dict):
    """
    Simule la reception d'audio depuis un client
    """
    audio_state["last_input"] = payload

    return {
        "status": "audio_received",
        "payload": payload
    }


@router.get("/audio/output")
async def audio_output():
    """
    Simule un retour audio vers le client
    """
    fake_audio = {
        "audio": "FAKE_AUDIO_DATA"
    }

    audio_state["last_output"] = fake_audio

    return fake_audio
