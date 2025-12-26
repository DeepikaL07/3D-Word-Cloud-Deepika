import React, { useState } from 'react';
import axios from 'axios';
import URLInput from './components/URLInput';
import WordCloud3D from './components/WordCloud3D';
import { APIResponse, WordData } from './types';
import './App.css';

function App() {
  const [words, setWords] = useState<WordData[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleAnalyze = async (url: string) => {
    setLoading(true);
    setError(null);
    setWords([]);

    try {
      const response = await axios.post<APIResponse>(
        'http://localhost:8000/analyze',
        { url }
      );

      setWords(response.data.words);
    } catch (err: any) {
      setError(
        err.response?.data?.detail || 
        'Failed to analyze article. Please check the URL and try again.'
      );
      console.error('Error analyzing article:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <URLInput onSubmit={handleAnalyze} loading={loading} />

      {error && (
        <div style={styles.error}>
          <p>❌ {error}</p>
        </div>
      )}

      {loading && (
        <div style={styles.loading}>
          <p>🔄 Analyzing article...</p>
        </div>
      )}

      {words.length > 0 && !loading && (
        <div style={styles.cloudContainer}>
          <h2 style={styles.cloudTitle}>
            Topic Word Cloud ({words.length} keywords)
          </h2>
          <WordCloud3D words={words} />
          <p style={styles.instructions}>
            💡 Drag to rotate • Scroll to zoom • Larger words = more important topics
          </p>
        </div>
      )}
    </div>
  );
}

const styles = {
  error: {
    backgroundColor: '#fee',
    color: '#c00',
    padding: '15px',
    margin: '20px auto',
    maxWidth: '800px',
    borderRadius: '8px',
    border: '2px solid #fcc',
  },
  loading: {
    padding: '20px',
    fontSize: '1.2rem',
    color: '#007bff',
  },
  cloudContainer: {
    marginTop: '30px',
  },
  cloudTitle: {
    fontSize: '1.5rem',
    marginBottom: '15px',
    color: '#333',
  },
  instructions: {
    marginTop: '15px',
    color: '#666',
    fontSize: '14px',
  },
};

export default App;