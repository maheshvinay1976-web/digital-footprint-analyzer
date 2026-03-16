import requests

def check_social(username):

    sites = {
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}"
    }

    found = []

    for site, url in sites.items():
        try:
            r = requests.get(url, timeout=5)

            if r.status_code == 200:
                found.append(site)

        except:
            pass

    return found


def categorize_risk(score):

    if score < 30:
        return "Low Risk"

    elif score < 70:
        return "Medium Risk"

    else:
        return "High Risk"
