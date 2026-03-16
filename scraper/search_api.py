import requests
from bs4 import BeautifulSoup

def dummy_search(query):
    """
    Placeholder function to simulate web search.
    Real Google API can be added here.
    """
    # This is just a placeholder list
    results = [
        f"Found {query} on example.com",
        f"Found {query} on testsite.org"
    ]
    return results
