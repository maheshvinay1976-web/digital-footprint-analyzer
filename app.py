from flask import Flask, render_template, request
from ml_model.risk_predictor import predict_risk
from scraper.search_api import dummy_search
from utils.helpers import categorize_risk

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form.get('phone', '')
        username = request.form.get('username', '')

        # Call placeholder AI function
        risk_score = predict_risk(name, email, phone, username)

        # Call placeholder scraper
        exposures = dummy_search(name) + dummy_search(email) + dummy_search(username)

        results = {
            "risk_score": risk_score,
            "exposures": exposures,
            "suggestions": [f"Risk Level: {categorize_risk(risk_score)}"]
        }

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
