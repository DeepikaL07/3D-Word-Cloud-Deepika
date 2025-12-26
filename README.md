# 3D Word Cloud Analyzer

An interactive web application that analyzes news articles and visualizes their key topics as a dynamic 3D word cloud using React Three Fiber and FastAPI.

## 🎯 Features

- 🌐 Fetch and parse articles from any URL
- 🤖 AI-powered topic extraction using TF-IDF (NLP)
- 🎨 Beautiful 3D interactive visualization with Three.js
- 🔄 Auto-rotating word cloud with manual controls
- 📊 Word size and color based on topic importance
- ⚡ Real-time analysis and rendering
- 🎮 Interactive controls (drag to rotate, scroll to zoom)

## 🛠️ Tech Stack

### Backend

- **FastAPI** (v0.104.1) - Modern, fast Python web framework
- **BeautifulSoup4** (v4.12.2) - HTML parsing and web scraping
- **scikit-learn** (v1.3.2) - TF-IDF keyword extraction and NLP
- **Requests** (v2.31.0) - HTTP library for fetching articles
- **Uvicorn** (v0.24.0) - ASGI server for FastAPI
- **lxml** - Fast XML/HTML parser

### Frontend

- **React** (v18.2.0) - UI library
- **TypeScript** (v4.9.5) - Type-safe JavaScript
- **React Three Fiber** (v8.15.0) - React renderer for Three.js
- **Three.js** (v0.159.0) - 3D graphics library
- **@react-three/drei** (v9.88.0) - Useful helpers for React Three Fiber
- **Axios** (v1.6.0) - HTTP client for API calls

## 📁 Project Structure

```
3D-Word-Cloud-Deepika/
├── backend/
│   ├── main.py              # FastAPI application & endpoints
│   ├── requirements.txt     # Python dependencies
│   └── utils/
│       ├── scraper.py      # Article fetching logic
│       └── nlp.py          # TF-IDF topic modeling
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── URLInput.tsx     # URL input component
│   │   │   └── WordCloud3D.tsx  # 3D visualization
│   │   ├── types/
│   │   │   └── index.ts         # TypeScript interfaces
│   │   ├── App.tsx              # Main application
│   │   └── App.css              # Styling
│   └── package.json
├── setup.bat                # Windows setup script
├── setup.sh                 # Mac/Linux setup script
└── README.md
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.9 or higher
- Node.js 16 or higher
- npm

### Quick Start (Automated)

#### Windows:

```bash
setup.bat
```

#### Mac/Linux:

```bash
chmod +x setup.sh
./setup.sh
```

This will automatically install all dependencies and start both servers.

### Manual Setup

#### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

Backend runs at: `http://localhost:8000`

API Documentation: `http://localhost:8000/docs`

#### Frontend Setup

```bash
# Navigate to frontend directory (in a new terminal)
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend runs at: `http://localhost:3000`

## 📖 Usage

1. Open `http://localhost:3000` in your browser
2. Enter a news article URL in the input field (or select a sample URL)
3. Click "Analyze"
4. Wait 5-10 seconds for analysis
5. Interact with the 3D word cloud:
   - **Drag** to rotate
   - **Scroll** to zoom
   - **Right-click + drag** to pan
   - Words auto-rotate for dynamic effect

## 🔗 Sample URLs to Try

- **Wikipedia:** `https://en.wikipedia.org/wiki/Artificial_intelligence`
- **BBC News:** `https://www.bbc.com/news`
- **Reuters:** `https://www.reuters.com/world/`
- **The Guardian:** `https://www.theguardian.com/world`

## 🔌 API Endpoints

### `GET /`

Returns API status and available endpoints

**Response:**

```json
{
  "message": "3D Word Cloud API is running!",
  "endpoints": {
    "/analyze": "POST - Analyze article from URL"
  }
}
```

### `POST /analyze`

Analyzes an article and extracts keywords

**Request:**

```json
{
  "url": "https://example.com/article"
}
```

**Response:**

```json
{
  "words": [
    { "word": "artificial intelligence", "weight": 0.85 },
    { "word": "machine learning", "weight": 0.72 },
    { "word": "technology", "weight": 0.65 }
  ],
  "article_length": 5432,
  "status": "success"
}
```

### `GET /health`

Health check endpoint

**Response:**

```json
{
  "status": "healthy"
}
```

## 🧠 How It Works

### Backend Pipeline:

1. **Fetch** - Downloads HTML from provided URL using `requests`
2. **Parse** - Extracts article text with `BeautifulSoup4` (removes scripts, navigation, footer)
3. **Clean** - Preprocesses text (lowercase, removes special characters)
4. **Analyze** - Applies TF-IDF vectorization to extract key topics
5. **Return** - Sends JSON with word-weight pairs to frontend

### Frontend Rendering:

1. **Receive** - Gets keyword data from API via Axios
2. **Position** - Distributes words in spherical coordinates (3D space)
3. **Scale** - Sizes words based on importance weights
4. **Color** - Applies gradient (blue→purple) based on relevance
5. **Animate** - Auto-rotates and responds to user interactions

## 🎨 Technical Highlights

- **Multi-strategy scraping:** Falls back through `<article>`, `<main>`, all `<p>` tags
- **Robust NLP:** TF-IDF with CountVectorizer fallback for edge cases
- **Spherical layout:** Words positioned using spherical coordinates for aesthetic distribution
- **Dynamic sizing:** Font size calculated as `0.3 + weight * 0.7`
- **CORS enabled:** Configured for local development
- **Full TypeScript:** Type safety throughout frontend
- **Error handling:** Comprehensive error messages and loading states

## ⚠️ Known Limitations

- **Paywall sites** may block scraping
- **JavaScript-heavy sites** (SPAs) may not be fully parsed
- **Very short articles** (<100 characters) won't generate results
- **Bot detection** on some news sites may prevent access
- **Wikipedia** and simple blog sites work best

## 🐛 Troubleshooting

### Backend not starting

```bash
# Check Python version
python --version  # Should be 3.9+

# Ensure virtual environment is activated
# You should see (venv) in terminal

# Reinstall dependencies
pip install -r requirements.txt
```

### Frontend not starting

```bash
# Clear cache
npm cache clean --force

# Delete and reinstall
rm -rf node_modules package-lock.json
npm install
```

### "Could not fetch article" error

- Try Wikipedia URLs (most reliable)
- Check if site requires authentication
- Some sites block automated requests
- Verify the backend is running on port 8000

### CORS errors

- Ensure backend is running on port 8000
- Check `CORSMiddleware` configuration in `main.py`

### Port already in use

```bash
# Backend (change port)
uvicorn main:app --reload --port 8001

# Frontend - create .env file with:
PORT=3001
```

## 🚧 Future Enhancements

- [ ] PDF document support
- [ ] Multiple language support
- [ ] Sentiment analysis integration
- [ ] Export word cloud as PNG/SVG
- [ ] Custom color schemes
- [ ] Different word cloud shapes (sphere, cube, cylinder)
- [ ] Save/load analyses
- [ ] Compare multiple articles side-by-side
- [ ] Advanced NLP with BERT/transformers

## 👨‍💻 Development Notes

- Backend uses Python's asyncio for concurrent requests
- Frontend uses React hooks for state management
- Three.js objects are memoized for performance optimization
- Auto-reload enabled for development
- Comprehensive logging for debugging
- Feature-based commit history for transparent development process

## 📝 Author

**Deepika**

## 📄 License

MIT License - Feel free to use for learning and projects!

---

**Built with ❤️ for the 3D Word Cloud Technical Assessment**
