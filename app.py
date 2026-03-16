from flask import Flask, render_template, request
from scraper.search_api import search_username
from utils.social_finder import check_social
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

        username_hits = search_username(username)

        social_accounts = check_social(username)

        risk_score = predict_risk(username_hits, social_accounts)

        results = {
            "risk_score": risk_score,
            "exposures": username_hits,
            "social": social_accounts,
            "suggestions": [
                "Enable 2FA",
                "Avoid public personal data",
                "Use different passwords"
            ]
        }

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run()
