from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# =====================
# Function to calculate basic risk
# =====================
def calculate_risk(name, email, phone, username):
    score = 0
    reasons = []

    # Name check
    if name:
        score += 10
        reasons.append("Name can reveal identity")

    # Email check
    if email:
        score += 20
        if any(char.isdigit() for char in email):
            score += 10
            reasons.append("Email may reveal birth year or personal info")

    # Phone check
    if phone:
        score += 20
        reasons.append("Phone number exposure risk")

    # Username check
    if username:
        score += 20
        if len(username) < 6:
            score += 10
            reasons.append("Short username easy to search")

    return score, reasons

# =====================
# Function to generate social media links
# =====================
def generate_social_links(username):
    platforms = {
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}"
    }
    return platforms

# =====================
# Function to check data breach (using Have I Been Pwned API)
# =====================
def check_email_breach(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-api-key": "YOUR_HIBP_API_KEY",  # Get free API key from Have I Been Pwned
        "User-Agent": "DigitalFootprintAnalyzer"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            breaches = [breach['Name'] for breach in response.json()]
            return breaches
        else:
            return []
    except:
        return []

# =====================
# Function to simulate Dark Web email check
# =====================
def dark_web_email_check(email):
    # We will simulate this safely
    dark_web_leak_emails = ["test@example.com", "sample@gmail.com"]
    if email.lower() in dark_web_leak_emails:
        return True
    return False

# =====================
# Routes
# =====================
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        username = request.form["username"]

        # Basic risk score
        score, reasons = calculate_risk(name, email, phone, username)

        # Social media links
        social_links = generate_social_links(username)

        # Check breaches
        breaches = check_email_breach(email)
        if breaches:
            score += 20
            reasons.append("Email found in data breaches")

        # Dark web check
        dark_web_risk = dark_web_email_check(email)
        if dark_web_risk:
            score += 20
            reasons.append("Email exposed in dark web leaks")

        # Risk level
        if score < 30:
            level = "Low Risk"
        elif score < 60:
            level = "Medium Risk"
        else:
            level = "High Risk"

        return render_template("index.html", score=score, level=level, reasons=reasons,
                               social_links=social_links, breaches=breaches, dark_web_risk=dark_web_risk)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
