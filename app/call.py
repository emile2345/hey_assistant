# -*- coding: utf-8 -*-

from fastapi import APIRouter

router = APIRouter()

# état d’appel en mémoire (ultra simple)
call_state = {
    "active": False
}


@router.post("/call/start")
async def start_call():
    call_state["active"] = True
    return {
        "status": "started",
        "active": call_state["active"]
    }


@router.post("/call/stop")
async def stop_call():
    call_state["active"] = False
    return {
        "status": "stopped",
        "active": call_state["active"]
    }

