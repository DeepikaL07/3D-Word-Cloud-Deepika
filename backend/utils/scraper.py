import requests
from bs4 import BeautifulSoup
from typing import Optional
import time

def fetch_article_text(url: str) -> Optional[str]:
    """
    Fetch and extract text content from a news article URL
    """
    try:
        # Better headers to avoid being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        
        print(f"\n📡 Fetching URL: {url}")
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        
        print(f"✅ Status Code: {response.status_code}")
        
        if response.status_code != 200:
            print(f"❌ Bad status code: {response.status_code}")
            return None
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove unwanted elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside', 'iframe', 'noscript']):
            element.decompose()
        
        # Try multiple strategies to get text
        text = ""
        
        # Strategy 1: Look for article tags
        article = soup.find('article')
        if article:
            print("📄 Found <article> tag")
            paragraphs = article.find_all('p')
            text = ' '.join([p.get_text() for p in paragraphs])
        
        # Strategy 2: Look for main content
        if not text or len(text) < 200:
            main = soup.find('main')
            if main:
                print("📄 Found <main> tag")
                paragraphs = main.find_all('p')
                text = ' '.join([p.get_text() for p in paragraphs])
        
        # Strategy 3: Get all paragraphs
        if not text or len(text) < 200:
            print("📄 Getting all <p> tags")
            paragraphs = soup.find_all('p')
            text = ' '.join([p.get_text() for p in paragraphs])
        
        # Strategy 4: Get all div text (last resort)
        if not text or len(text) < 200:
            print("📄 Getting all text from body")
            body = soup.find('body')
            if body:
                text = body.get_text()
        
        # Clean up whitespace
        text = ' '.join(text.split())
        
        print(f"📊 Extracted {len(text)} characters")
        
        if len(text) < 100:
            print(f"❌ Text too short: {len(text)} characters")
            return None
        
        print(f"✅ Successfully extracted text!")
        return text
        
    except requests.exceptions.Timeout:
        print(f"❌ Timeout error - site took too long to respond")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request error: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None
