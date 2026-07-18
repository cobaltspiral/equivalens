from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SourceAnalysisRequest(BaseModel):
    source_text: str = Field(min_length=1, max_length=12000)

class TechniqueAnalysisRequest(BaseModel):
    source_text: str = Field(min_length=1, max_length=12000)
    target_text: str = Field(min_length=1, max_length=12000)
    machine_translation: str | None = Field(default=None, max_length=12000)

@app.post("/analyse-source")
async def analyse_source(request: SourceAnalysisRequest):
    # Replace with AI model.
    return {
        "annotations": [],
        "message": "Source text received successfully."
    }

@app.post("/analyse-techniques")
async def analyse_techniques(request: TechniqueAnalysisRequest):
    # Replace with AI model.
    return {
        "annotations": [],
        "message": "Source and target text received successfully.",
        "has_machine_translation": bool(request.machine_translation),
    }