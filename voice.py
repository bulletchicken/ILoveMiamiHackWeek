from pathlib import Path
from openai import OpenAI
client = OpenAI(api_key="")

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=""
)

response.stream_to_file(speech_file_path)