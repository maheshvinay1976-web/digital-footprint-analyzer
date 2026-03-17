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

            if response.status_code == 200 and "Not Found" not in response.text:
                # ✅ RETURN DICTIONARY (IMPORTANT)
                found.append({
                    "platform": name,
                    "url": url
                })

        except:
            pass

    return found

# 📊 Calculate risk score (REAL logic)
def calculate_risk(email, phone, social_count):
    score = 0

    # Personal info exposure
    if email:
        score += 20
    if phone:
        score += 20

    # Social media exposure
    score += social_count * 15

    # Limit max score
    if score > 100:
        score = 100

    return score


# 🚦 Convert score to risk level
def get_risk_level(score):
    if score < 30:
        return "Low Risk"
    elif score < 70:
        return "Medium Risk"
    else:
        return "High Risk"
