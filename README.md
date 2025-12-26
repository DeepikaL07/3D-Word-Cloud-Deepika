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
- **@react-three/drei** (v9.88.0) - Useful helpers
