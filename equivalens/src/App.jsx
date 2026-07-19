import { useState } from 'react'
import './App.css'

const WORD_LIMIT = 300;
const API_BASE_URL = "http://127.0.0.1:8001";

function countWords(text) {
  const trimmedText = text.trim();
  return trimmedText ? trimmedText.split(/\s+/).length : 0;
}

function trimToWordLimit(text) {
  const words = text.trim().split(/\s+/);
  if (text.trim() === '' || words.length <= WORD_LIMIT) {
    return text;
  }
  return words.slice(0, WORD_LIMIT).join(' ');
}

function TextPanel({ title, optional = false, value, onChange }) {
  const wordCount = countWords(value);

  function handleChange(event) {
    onChange(trimToWordLimit(event.target.value));
  }

  return (
    <section className="text-panel">
      <div className="text-panel-header">
        <div>
          <h2>{title}</h2>
          {optional && <p className="optional-label">Optional</p>}
        </div>
        <span className={wordCount == WORD_LIMIT ? 'word-count limit-reached' : 'word-count'}>
          {wordCount}/{WORD_LIMIT} words
        </span>
      </div>

      <textarea
        value={value}
        onChange={handleChange}
        placeholder={`Paste your ${title.toLowerCase()} here...`}
        aria-label={title}
      />
    </section>
  );
}

function App() {
  const [sourceText, setSourceText] = useState('');
  const [targetText, setTargetText] = useState('');
  const [machineTranslation, setMachineTranslation] = useState('');
  const [status, setStatus] = useState('');
  const [sourceAnnotations, setSourceAnnotations] = useState([]);
  const [techniqueAnnotations, setTechniqueAnnotations] = useState([]);
  const [loading, setLoading] = useState("");
  const [error, setError] = useState("");

async function analyseSource() {
  setLoading("source");
  setError("");
  setTechniqueAnnotations([]);

  try {
    const response = await fetch(`${API_BASE_URL}/analyse-source`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        source_text: sourceText,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Source analysis failed.");
    }

    setSourceAnnotations(data.annotations);
  } catch (error) {
    setError(error.message);
    setSourceAnnotations([]);
  } finally {
    setLoading("");
  }
}

async function analyseTechniques() {
  setLoading("techniques");
  setError("");

  try {
    const response = await fetch(`${API_BASE_URL}/analyse-techniques`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        source_text: sourceText,
        target_text: targetText,
        machine_translation: machineTranslation || null,
        creative_potential_units: sourceAnnotations,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Technique analysis failed.");
    }

    setTechniqueAnnotations(data.annotations);
  } catch (error) {
    setError(error.message);
    setTechniqueAnnotations([]);
  } finally {
    setLoading("");
  }
}

  return (
    <main className="app">
      <header className="hero">
        <p className="eyebrow">Literary translation annotation assistant</p>
        <h1>Equivalens</h1>
        <p className="intro">
          Paste aligned source and translation texts to prepare an annotation.
        </p>
      </header>

      <section className="text-grid" aria-label="Text inputs">
        <TextPanel
          title="Source text"
          value={sourceText}
          onChange={setSourceText}
        />

        <TextPanel
          title="Target text"
          value={targetText}
          onChange={setTargetText}
        />

        <TextPanel
          title="Machine translation"
          optional
          value={machineTranslation}
          onChange={setMachineTranslation}
        />
      </section>

<section className="actions" aria-label="Analysis actions">
  <button
    type="button"
    onClick={analyseSource}
    disabled={!sourceText.trim() || loading !== ""}
  >
    {loading === "source"
      ? "Analysing source..."
      : "Analyse creative potential"}
  </button>

  <button
    type="button"
    className="secondary-button"
    onClick={analyseTechniques}
    disabled={
      !sourceText.trim() ||
      !targetText.trim() ||
      sourceAnnotations.length === 0 ||
      loading !== ""
    }
  >
    {loading === "techniques"
      ? "Analysing techniques..."
      : "Analyse translation techniques"}
  </button>
</section>

{error && (
  <p className="error-message" role="alert">
    {error}
  </p>
)}

{sourceAnnotations.length > 0 && (
  <section className="results-section">
    <h2>Units of creative potential</h2>

    {sourceAnnotations.map((annotation, index) => (
      <article className="annotation-card" key={`${annotation.source_start}-${index}`}>
        <strong>{annotation.source_unit}</strong>
        <p>
          {annotation.category}
          {annotation.subcategory ? ` · ${annotation.subcategory}` : ""}
        </p>
        <p>{annotation.rationale}</p>
        <small>Confidence: {annotation.confidence}</small>
      </article>
    ))}
  </section>
)}

{techniqueAnnotations.length > 0 && (
  <section className="results-section">
    <h2>Proposed translation techniques</h2>

    {techniqueAnnotations.map((annotation, index) => (
      <article className="annotation-card" key={`${annotation.source_unit}-${index}`}>
        <strong>{annotation.source_unit}</strong>
        <p>Target: {annotation.target_unit || "No aligned unit found"}</p>
        <p>Technique: {annotation.techniques.join(", ")}</p>
        <p>{annotation.rationale}</p>
        <small>Confidence: {annotation.confidence}</small>
      </article>
    ))}
  </section>
)}

      {status && (
        <section className="status-message" aria-live="polite">
          {status}
        </section>
      )}
    </main>
  );
}

export default App;