from fastapi import APIRouter

router = APIRouter()


@router.post("/translate")
async def translate(payload: dict):
    """
    Mock translation endpoint.
    Simulates STT + translation.
    """

    text = payload.get("text", "")
    source_lang = payload.get("source_lang", "unknown")
    target_lang = payload.get("target_lang", "unknown")

    translated_text = f"[{source_lang} → {target_lang}] {text}"

    return {
        "original_text": text,
        "translated_text": translated_text,
        "source_lang": source_lang,
        "target_lang": target_lang
    }

