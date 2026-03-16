from flask import Flask, render_template, request
from scraper.search_api import check_breach
from ml_model.risk_predictor import predict_risk

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        username = request.form['username']

        breach_found, sites = check_breach(email)

        risk_score = predict_risk(breach_found, len(sites))

        exposures = []

        if breach_found:
            exposures.append(f"Email found in {len(sites)} data breaches")
            exposures.extend(sites)
        else:
            exposures.append("No breach found for this email")

        suggestions = [
            "Use strong passwords",
            "Enable 2FA on accounts",
            "Avoid sharing personal info publicly"
        ]

        results = {
            "risk_score": risk_score,
            "exposures": exposures,
            "suggestions": suggestions
        }

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run()
