from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal
from mistralai.client import Mistral
from dotenv import load_dotenv
import os
from taxonomy import UCP_CATEGORIES, TRANSLATION_TECHNIQUES
import json

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
    source_text: str
    target_text: str
    machine_translation: str | None = None
    creative_potential_units: list[CreativePotentialAnnotation]

@app.post("/analyse-source", response_model=SourceAnalysisResponse)
def analyse_source(request: SourceAnalysisRequest):
    client = get_mistral_client()

    system_prompt = f"""
You are Equivalens, a careful literary-translation annotation assistant.

Your task is to identify units of creative potential (UCPs) in a source text.
Units of creative potential are units that require the translators to use their high problem
solving capacity as opposed to those that are regarded as routine units that are standard in the 
translation practice (for example, a standard unit is a unit that already has an established 
equivalent translation). We could say that units of creative potential are those commonly 
known as translation problems. Creativity starts with a problem that is not easy to solve for 
the experienced translator and that also stems from the desire to offer a non-standard and an 
improved translation. 

# Allowed categories
{UCP_CATEGORIES}

# Rules
- Highlight all units of creative potential in the text.
-  Do not use several classifications for the same unit, choose the classification that better suits the unit.
- `source_unit` must be an exact substring of the source text.
- `source_start` and `source_end` must be Python character offsets:
  source_text[source_start:source_end] must equal source_unit.
- Use only the listed category keys.
- If no meaningful unit is present, return an empty annotations list.
- This is a proposal for human review, not a definitive annotation.
"""

    try:
        response = client.chat.parse(
            model="mistral-small-latest",
            temperature=0,
            max_tokens=1800,
            response_format=SourceAnalysisResponse,
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"<source_text>\n{request.source_text}\n</source_text>",
                },
            ],
        )

        return SourceAnalysisResponse.model_validate(
            response.choices[0].message.parsed
        )

    except Exception as error:
        raise HTTPException(
            status_code=502,
            detail=f"Mistral source analysis failed: {str(error)}",
        )

@app.post("/analyse-techniques", response_model=TechniqueAnalysisResponse)
def analyse_techniques(request: TechniqueAnalysisRequest):
    client = get_mistral_client()

    system_prompt = f"""
You are Equivalens, a careful literary-translation annotation assistant.

Your task is to annotate the translation techniques used in the target text
to translate the units of creative potential previously found in the source text.

# Allowed translation techniques
{TRANSLATION_TECHNIQUES}

# Rules
- Analyse only the supplied units of creative potential. For each supplied source unit:
- Find its translation in the target text.
- If available, find its translation in the machine translation.
- Assign one translation technique label from the allowed taxonomy.
- Do not identify new source units.
- Return one annotation for every supplied unit, using the supplied source_unit exactly.
- Use `uncertain` if no confident technique can be proposed.
- These are proposals for human review, not definitive annotations.

"""

    user_prompt = f"""
<source_text>
{request.source_text}
</source_text>

<target_text>
{request.target_text}
</target_text>

<machine_translation>
{request.machine_translation or "[Not supplied]"}
</machine_translation>

<creative_potential_units>
{json.dumps(
    [unit.model_dump() for unit in request.creative_potential_units],
    ensure_ascii=False,
    indent=2,
)}
</creative_potential_units>
"""

    try:
        response = client.chat.parse(
            model="mistral-small-latest",
            temperature=0,
            max_tokens=2000,
            response_format=TechniqueAnalysisResponse,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        return TechniqueAnalysisResponse.model_validate(
            response.choices[0].message.parsed
        )

    except Exception as error:
        raise HTTPException(
            status_code=502,
            detail=f"Mistral technique analysis failed: {str(error)}",
        )

class CreativePotentialAnnotation(BaseModel):
    source_unit: str
    source_start: int = Field(ge=0)
    source_end: int = Field(ge=0)
    category: str
    confidence: Literal["high", "medium", "low"]
    rationale: str

class SourceAnalysisResponse(BaseModel):
    annotations: list[CreativePotentialAnnotation]
    limitations: list[str]

class TechniqueAnnotation(BaseModel):
    source_unit: str
    target_unit: str | None = None
    machine_translation_unit: str | None = None
    techniques: list[str]
    confidence: Literal["high", "medium", "low"]
    rationale: str

class TechniqueAnalysisResponse(BaseModel):
    annotations: list[TechniqueAnnotation]
    limitations: list[str]

def get_mistral_client() -> Mistral:
    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="MISTRAL_API_KEY is not configured on the backend.",
        )

    return Mistral(api_key=api_key)