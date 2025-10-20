from fastapi import APIRouter, UploadFile, File, HTTPException
from app.transcriber import transcribe_audio
from app.summarizer import summarize_text

router = APIRouter()

@router.post("/summarize")
async def summarize_podcast(file:UploadFile = File(...)):
  """
  Upload a podcast audio file(MP3/WAV) and get a summarized transcript.
  """
  try:
    transcript = await transcribe_audio(file)
    summary = await summarize_text(transcript)
    return {"summary": summary}
  except Exception as e:
    raise HTTPException(status_code=500, detail = str(e))
