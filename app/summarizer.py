import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
async def summarize_text(transcript: str) -> str:
  """
  Summarizes the given podcast transcript into a short summary.
  """
  prompt = f"""
  Summarize the following podcast transcript into 3 concise paragraphs.
  Focus on the main topics, ideas, and tone of the conversation.

  Transcript:
  {transcript[:8000]}
  """
  response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content": prompt}],
    temperature=0.7,
  )
  return response.choices[0].message.content.strip()
  
