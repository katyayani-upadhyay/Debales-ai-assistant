import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

BASE_URL = "https://debales.ai"
visited = set()
all_text = ""


def is_valid(url):
    parsed = urlparse(url)
    return parsed.netloc == urlparse(BASE_URL).netloc


def extract_text(soup):
    texts = []
    for tag in soup.find_all(["p", "h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if text:
            texts.append(text)
    return "\n".join(texts)


def crawl(url):
    global all_text

    if len(visited) > 20:
        return
    
    url = url.rstrip("/")
    
    if url in visited:
        return

    print(f"Scraping: {url}")
    visited.add(url)

    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        # extract useful text
        page_text = extract_text(soup)
        all_text += page_text + "\n\n"

        # find new links
        for link in soup.find_all("a", href=True):
            next_url = urljoin(BASE_URL, link["href"])

            if is_valid(next_url) and next_url not in visited:
                crawl(next_url)

    except Exception as e:
        print(f"Error scraping {url}: {e}")


def save_data():
    global all_text
    all_text = "\n".join(set(all_text.split("\n")))
    os.makedirs("data", exist_ok=True)
    with open("data/debales_docs.txt", "w", encoding="utf-8") as f:
        f.write(all_text)


if __name__ == "__main__":
    crawl(BASE_URL)
    save_data()
    print("Scraping complete. Data saved.")