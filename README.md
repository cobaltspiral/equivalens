# Equivalens

A human-in-the-loop annotation assistant for exploring creative choices in literary translation.

Equivalens is available at: https://equivalens.onrender.com

## The problem

Literary-translation students and researchers often compare and annotate a source text with one or more translations manually. Identifying units that may require creative problem-solving, then recording the translation technique used for each one, is time-consuming and difficult to reproduce consistently.

Equivalens provides a lightweight, structured starting point for this process. It proposes annotations for human review; it does not replace a translator, teacher, or researcher.

## What Equivalens does

1. A user pastes a source text, a target translation, and (optionally) a machine translation.
2. The app identifies potential **units of creative potential** in the source text.
3. It can then analyse how each selected unit was translated:
   - in the human target translation;
   - separately, in the optional machine translation.
4. It proposes translation-technique labels, confidence levels, and short rationales for the choice of label.

The interface currently accepts up to 300 words per text panel.

## Research foundation

The annotation workflow and taxonomy is based on:

> Macken, L., Ruffo, P., & Daems, J. (2025). *The Role of Translation Workflows in Overcoming Translation Difficulties: A Comparative Analysis of Human and Machine Translation (Post-Editing) Approaches.*

The prototype uses:

- units of creative potential, including multiword units, complex structures, cultural and linguistic variants, colloquial language, and metaphors/original images;
- translation-technique labels based on the taxonomy in Appendix A of the paper.

This project is a prototype and research-support tool. All model outputs are suggestions requiring human judgement.

## Tech stack

- **Frontend:** React + Vite
- **Backend:** Python + FastAPI
- **Runtime model:** Mistral Small through the Mistral API
- **Deployment:** Render
- **Development workflow:** OpenAI Codex

## How Codex was used

Equivalens was built and meaningfully extended during OpenAI Build Week 2026 with Codex.

Codex was used to support:

- planning the prototype architecture and annotation workflow;
- building the React text-input interface;
- implementing FastAPI request models and endpoints;
- integrating the Mistral API securely through the backend;
- debugging API, CORS, environment-variable, and deployment issues;
- refining the annotation response schema and user interface.

Mistral Small is used for the app’s runtime annotation requests. It is a third-party API integration.

## Run locally

### Prerequisites

- Python 3.9 or later
- Node.js 18 or later
- A Mistral API key

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd equivalens
```

### 2. Configure and run the backend
```bash
cd equivalens-backend
python -m venv venv
```
Activate the virtual environment:
```bash
.\venv\Scripts\Activate.ps1
```
Install dependencies
```bash
pip install -r requirements.txt
```
Create equivalens-backend/.env:
```bash
MISTRAL_API_KEY=your_mistral_api_key
```
Start FASTAPI:
```bash
python -m uvicorn main:app --reload --port 8001
```
The backend documentation is available at: 
```bash
http://127.0.0.1:8001/docs
```

### 3. Configure and run the frontend
```bash
cd equivalens
npm install
npm run dev
```
Open the URL shown by Vite, usually:
```bash
http://localhost:5173
```
The frontend defaults to using the local backend at http://127.0.0.1:8001.

## Project Structure
```bash
equivalens/
├── equivalens/             # React + Vite frontend
│   └── src/
├── equivalens-backend/     # FastAPI backend
│   ├── main.py
│   ├── taxonomy.py
│   └── requirements.txt
├── .gitignore
└── README.md
```

## API Endpoints
| Endpoint | Purpose |
|---|---|
| `POST /analyse-source` | Identifies proposed units of creative potential in the source text |
| `POST /analyse-techniques` | Analyses how the selected source units were translated in the target and optional MT text |

## Limitations
- The app proposes annotations; it does not provide ground-truth labels.
- Results can vary between model calls and should be reviewed by a human.
– The current taxonomy is implemented for this prototype and should be evaluated against expert annotations before research use.
- The model may miss alignments or suggest an unsuitable translation technique.
- The current prototype is designed for short text passages only.
- Do not submit confidential, unpublished, or copyrighted text unless you have permission to send it to the Mistral API.

## Future work
- Editable accept/reject/relabel annotation controls
- JSON and CSV export of reviewed annotations
- Better span highlighting and source-target alignment
- Support for more language pairs
- Evaluation against a human-annotated dataset
- User accounts and persistent annotation projects

## License
The project is released under the MIT License.

## Author
Created by Paola Ruffo (cobaltspiral) for **OpenAI Build Week 2026 (Education track)**

## References







