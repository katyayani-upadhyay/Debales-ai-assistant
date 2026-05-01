from dotenv import load_dotenv
import os

load_dotenv()

import requests
import os

def search_tool(query):
    api_key = os.getenv("SERP_API_KEY")

    url = f"https://serpapi.com/search?q={query}&api_key={api_key}"
    res = requests.get(url).json()

    try:
        return res["organic_results"][0]["snippet"]
    except:
        return "No results found."
