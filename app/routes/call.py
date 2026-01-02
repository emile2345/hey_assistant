from fastapi import APIRouter, HTTPException
from app.state import call_state

router = APIRouter(prefix="/call", tags=["Call"])

@router.post("/start")
def start_call():
    if call_state["status"] != "idle":
        raise HTTPException(status_code=400, detail="Call already in progress")

    call_state["status"] = "ringing"
    return {"status": "ringing", "message": "Incoming call..."}


@router.post("/accept")
def accept_call():
    if call_state["status"] != "ringing":
        raise HTTPException(status_code=400, detail="No call to accept")

    call_state["status"] = "in_call"
    return {"status": "in_call", "message": "Call accepted"}


@router.post("/stop")
def stop_call():
    if call_state["status"] == "idle":
        raise HTTPException(status_code=400, detail="No active call")

    call_state["status"] = "idle"
    return {"status": "idle", "message": "Call ended"}
