from flask import Flask, render_template, request
from utils.helpers import check_social, calculate_risk, get_risk_level

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None

    if request.method == "POST":
        # Get user input
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        username = request.form.get("username")

        # 🔍 Social accounts
social_accounts = check_social(username)

# 📊 Risk score
risk_score = calculate_risk(email, phone, len(social_accounts))
risk_level = get_risk_level(risk_score)

# 🧠 Risk breakdown
breakdown = {
    "email_risk": 15 if email else 0,
    "phone_risk": 15 if phone else 0,
    "social_risk": len(social_accounts) * 15
}

# 🎨 Color for UI
if risk_score < 30:
    color = "green"
elif risk_score < 70:
    color = "orange"
else:
    color = "red"

results = {
    "name": name,
    "email": email,
    "phone": phone,
    "username": username,
    "social_accounts": social_accounts,
    "risk_score": risk_score,
    "risk_level": risk_level,
    "breakdown": breakdown,
    "color": color
}

    return render_template("index.html", results=results)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
