import tempfile
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
async def transcribe_audio(file) -> str:
  """
  Transcribes an uploaded audio file to text using OpenAI Wisper API.
  """
  with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
    content = await file.read()
    temp_audio.write(content)
    temp_audio_path = temp_audio.name
  with open(temp_audio_path, "rb") as audio_file:
    transcript = openai.audio.transcriptions.create(
      model = "wisper-1",
      file=audio_file
    )
  return transcript.text
