import requests

def check_social(username):
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}"
    }

    found = []

    for name, url in sites.items():
        try:
            response = requests.get(url, timeout=5)

            # REAL CHECK (not fake)
            if response.status_code == 200 and "Not Found" not in response.text:
                found.append(name)

        except:
            pass

    return found
