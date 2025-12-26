import React, { useState } from 'react';

interface URLInputProps {
  onSubmit: (url: string) => void;
  loading: boolean;
}

const SAMPLE_URLS = [
  'https://www.bbc.com/news',
  'https://en.wikipedia.org/wiki/Artificial_intelligence',
  'https://www.reuters.com/world/',
];

const URLInput: React.FC<URLInputProps> = ({ onSubmit, loading }) => {
  const [url, setUrl] = useState(SAMPLE_URLS[0]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (url.trim()) {
      onSubmit(url.trim());
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>3D Word Cloud Analyzer</h1>
      <p style={styles.subtitle}>Enter a news article URL to visualize its topics</p>
      
      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          type="url"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter article URL..."
          style={styles.input}
          disabled={loading}
          required
        />
        <button 
          type="submit" 
          style={styles.button}
          disabled={loading}
        >
          {loading ? 'Analyzing...' : 'Analyze'}
        </button>
      </form>

      <div style={styles.samples}>
        <p style={styles.samplesTitle}>Sample URLs:</p>
        {SAMPLE_URLS.map((sampleUrl, index) => (
          <button
            key={index}
            onClick={() => setUrl(sampleUrl)}
            style={styles.sampleButton}
            disabled={loading}
          >
            {sampleUrl}
          </button>
        ))}
      </div>
    </div>
  );
};

const styles = {
  container: {
    padding: '20px',
    maxWidth: '800px',
    margin: '0 auto',
    textAlign: 'center' as const,
  },
  title: {
    fontSize: '2.5rem',
    marginBottom: '10px',
    color: '#333',
  },
  subtitle: {
    fontSize: '1.1rem',
    color: '#666',
    marginBottom: '30px',
  },
  form: {
    display: 'flex',
    gap: '10px',
    marginBottom: '20px',
  },
  input: {
    flex: 1,
    padding: '12px 15px',
    fontSize: '16px',
    border: '2px solid #ddd',
    borderRadius: '8px',
    outline: 'none',
  },
  button: {
    padding: '12px 30px',
    fontSize: '16px',
    backgroundColor: '#007bff',
    color: 'white',
    border: 'none',
    borderRadius: '8px',
    cursor: 'pointer',
    fontWeight: 'bold' as const,
  },
  samples: {
    marginTop: '20px',
  },
  samplesTitle: {
    fontSize: '14px',
    color: '#888',
    marginBottom: '10px',
  },
  sampleButton: {
    display: 'block',
    width: '100%',
    padding: '10px',
    margin: '5px 0',
    fontSize: '14px',
    backgroundColor: '#f8f9fa',
    border: '1px solid #ddd',
    borderRadius: '5px',
    cursor: 'pointer',
    textAlign: 'left' as const,
  },
};

export default URLInput;