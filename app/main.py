from app.routes.voice import router as voice_router
from fastapi import FastAPI
from app.routes.call import router as call_router
from fastapi.staticfiles import StaticFiles
import os


app = FastAPI(title="HEY Assistant")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(call_router)
app.include_router(voice_router)
# Sert tout ce qui est dans static/

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)






