import { useState } from 'react'
import './App.css'

const WORD_LIMIT = 300;

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

  function analyseSource() {
    // replace with fetch call
    setStatus('Source analysis will identify proposed units of creative potential.');     
  }

  function analyseTechniques() {
    // replace with fetch call
    setStatus('Technique analysis will compare the source with the target text(s).');
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
          disabled={!sourceText.trim()}
        >
          Analyse creative potential
        </button>

        <button
          type="button"
          className="secondary-button"
          onClick={analyseTechniques}
          disabled={!sourceText.trim() || !targetText.trim()}
        >
          Analyse translation techniques
        </button>
      </section>

      {status && (
        <section className="status-message" aria-live="polite">
          {status}
        </section>
      )}
    </main>
  );
}

export default App;