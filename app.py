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

        # 🔍 Check social media accounts
        social_accounts = []
        if username:
            social_accounts = check_social(username)

        # 📊 Calculate risk score
        risk_score = calculate_risk(email, phone, len(social_accounts))

        # 🚦 Get risk level
        risk_level = get_risk_level(risk_score)

        # 📦 Prepare results
        results = {
            "name": name,
            "email": email,
            "phone": phone,
            "username": username,
            "social_accounts": social_accounts,
            "risk_score": risk_score,
            "risk_level": risk_level
        }

    return render_template("index.html", results=results)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
