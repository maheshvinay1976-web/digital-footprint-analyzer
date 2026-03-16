import requests
from bs4 import BeautifulSoup

def search_username(username):

    query = f"https://www.google.com/search?q={username}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(query, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for g in soup.select("h3"):
        results.append(g.text)

    return results[:5]
