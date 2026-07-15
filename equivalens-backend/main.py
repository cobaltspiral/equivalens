from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import csv
from pydantic import BaseModel

app = FastAPI()

# Allow React frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Segment(BaseModel):
    id: int
    source: str
    target: str
    mt: str = None  # machine translation (optional)

class LabelRequest(BaseModel):
    segment: Segment

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    """Parse CSV with columns: id, source, target, [mt]"""
    contents = await file.read()
    lines = contents.decode().split("\n")
    reader = csv.DictReader(lines)
    segments = [dict(row) for row in reader if row.get("source")]
    return {"segments": segments, "count": len(segments)}

@app.post("/analyze")
async def analyze(request: LabelRequest):
    """Dummy response for now; will add LLM later"""
    source = request.segment.source
    target = request.segment.target
    
    # Placeholder: suggest a label based on text length
    if len(target) < len(source) * 0.7:
        suggestion = "reduction"
    elif len(target) > len(source) * 1.3:
        suggestion = "expansion"
    else:
        suggestion = "literal"
    
    return {
        "suggestion": suggestion,
        "confidence": 0.5,
        "metrics": {
            "length_ratio": len(target) / len(source),
            "similarity": 0.6  # Placeholder
        }
    }

@app.post("/export")
async def export(labels: list):
    """Return CSV of labeled segments"""
    # Later: write to CSV
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)