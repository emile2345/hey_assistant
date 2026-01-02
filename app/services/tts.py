from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

AUDIO_DIR = "app/audio"
OUTPUT_PATH = f"{AUDIO_DIR}/output.mp3"

def generate_voice(text: str):
    os.makedirs(AUDIO_DIR, exist_ok=True)

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="nova",
        input=text,
    ) as response:
        response.stream_to_file(OUTPUT_PATH)

    return OUTPUT_PATH
