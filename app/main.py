from fastapi import FastAPI
from app.routes import router as podcast_router
app = FastAPI(title= "Podcast Summariser Microservice")
app.include_router(podcast_router, prefix="/podcast")

@app.get("/")
def root():
  return{"message": "Podcast Summarizer API is running")
