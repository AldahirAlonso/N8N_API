from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title="N8N_Python")

class IncomingData(BaseModel):
    text: str
    source: str | None = None

@app.post("/analyze")
def analyze(data: IncomingData):
    return {"received_text": data.text, "length": len(data.text)}

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API funcionando!"}