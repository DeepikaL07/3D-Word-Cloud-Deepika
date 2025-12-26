from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.scraper import fetch_article_text
from utils.nlp import extract_keywords
from typing import List

# Create FastAPI app
app = FastAPI(
    title="3D Word Cloud API",
    description="API for extracting and analyzing topics from news articles",
    version="1.0.0"
)

# Enable CORS so frontend can access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Word data model
class Word(BaseModel):
    word: str
    weight: float

# Request model
class URLRequest(BaseModel):
    url: str

# Response model
class WordCloudResponse(BaseModel):
    words: List[Word]
    article_length: int
    status: str

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "3D Word Cloud API is running!",
        "endpoints": {
            "/analyze": "POST - Analyze article from URL"
        }
    }

# Main analysis endpoint
@app.post("/analyze", response_model=WordCloudResponse)
async def analyze_article(request: URLRequest):
    """
    Analyze an article from a URL and return word cloud data
    """
    print(f"\n{'='*60}")
    print(f"🚀 NEW REQUEST: Analyzing URL")
    print(f"{'='*60}")
    print(f"URL: {request.url}")
    
    # Step 1: Fetch article text
    print("\n📥 STEP 1: Fetching article...")
    text = fetch_article_text(request.url)
    
    if not text:
        print("❌ STEP 1 FAILED: Could not fetch article")
        raise HTTPException(
            status_code=400,
            detail="Could not fetch or parse article from the provided URL. Please check the URL and try again."
        )
    
    print(f"✅ STEP 1 SUCCESS: Got {len(text)} characters")
    print(f"First 200 chars: {text[:200]}...")
    
    # Step 2: Extract keywords using NLP
    print("\n🔬 STEP 2: Extracting keywords...")
    keywords = extract_keywords(text, top_n=30)
    
    if not keywords:
        print("❌ STEP 2 FAILED: Could not extract keywords")
        raise HTTPException(
            status_code=500,
            detail="Could not extract keywords from article. The article might be too short or in an unsupported format."
        )
    
    print(f"✅ STEP 2 SUCCESS: Got {len(keywords)} keywords")
    print(f"{'='*60}")
    print(f"✅ REQUEST COMPLETE")
    print(f"{'='*60}\n")
    
    return {
        "words": keywords,
        "article_length": len(text),
        "status": "success"
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}
