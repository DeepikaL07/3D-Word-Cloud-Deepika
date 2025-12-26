from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from typing import List, Dict
import re
import numpy as np

def clean_text(text: str) -> str:
    """
    Clean and preprocess text for NLP
    """
    # Remove URLs
    text = re.sub(r'http\S+|www.\S+', '', text)
    # Remove special characters but keep spaces
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Convert to lowercase
    text = text.lower()
    return text

def extract_keywords(text: str, top_n: int = 30) -> List[Dict[str, float]]:
    """
    Extract top keywords from text using TF-IDF
    """
    try:
        print(f"\n🔍 Starting keyword extraction...")
        print(f"📏 Original text length: {len(text)} characters")
        
        # Clean the text
        cleaned_text = clean_text(text)
        print(f"📏 Cleaned text length: {len(cleaned_text)} characters")
        
        if len(cleaned_text) < 50:
            print("❌ Text too short after cleaning")
            return []
        
        # Count words
        word_count = len(cleaned_text.split())
        print(f"📊 Word count: {word_count}")
        
        if word_count < 20:
            print("❌ Not enough words for analysis")
            return []
        
        # Try TF-IDF first
        try:
            print("🔧 Trying TF-IDF vectorization...")
            vectorizer = TfidfVectorizer(
                max_features=min(top_n, word_count),
                stop_words='english',
                ngram_range=(1, 2),
                min_df=1,
                max_df=0.9,
                lowercase=True,
                strip_accents='unicode'
            )
            
            tfidf_matrix = vectorizer.fit_transform([cleaned_text])
            feature_names = vectorizer.get_feature_names_out()
            scores = tfidf_matrix.toarray()[0]
            
            print(f"✅ Found {len(feature_names)} features")
            
        except ValueError as e:
            print(f"⚠️ TF-IDF failed: {e}")
            print("🔧 Trying simpler approach with CountVectorizer...")
            
            # Fallback to CountVectorizer
            vectorizer = CountVectorizer(
                max_features=min(top_n, word_count),
                stop_words='english',
                ngram_range=(1, 1),
                lowercase=True
            )
            
            count_matrix = vectorizer.fit_transform([cleaned_text])
            feature_names = vectorizer.get_feature_names_out()
            scores = count_matrix.toarray()[0]
            
            # Normalize scores
            if scores.max() > 0:
                scores = scores / scores.max()
            
            print(f"✅ Found {len(feature_names)} features with CountVectorizer")
        
        # Create word-weight pairs
        word_weights = []
        for word, score in zip(feature_names, scores):
            if score > 0 and len(word) > 2:  # Filter out very short words
                word_weights.append({
                    "word": word,
                    "weight": float(score)
                })
        
        # Sort by weight (highest first)
        word_weights.sort(key=lambda x: x['weight'], reverse=True)
        
        # Take top N
        word_weights = word_weights[:top_n]
        
        print(f"✅ Extracted {len(word_weights)} keywords")
        
        # Print top 5 for debugging
        if word_weights:
            print(f"🏆 Top 5 keywords:")
            for i, w in enumerate(word_weights[:5]):
                print(f"   {i+1}. {w['word']} (weight: {w['weight']:.3f})")
        
        return word_weights
        
    except Exception as e:
        print(f"❌ Error in keyword extraction: {e}")
        import traceback
        traceback.print_exc()
        return []
