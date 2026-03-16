from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def analyze_data(query):

    url = "https://www.google.com/search?q=" + query
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    results = soup.find_all("h3")

    exposure_count = len(results)

    risk_score = min(exposure_count * 10, 100)

    if risk_score > 70:
        risk = "High Risk"
    elif risk_score > 40:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    return exposure_count, risk, risk_score


@app.route("/", methods=["GET","POST"])
def index():

    exposure = None
    risk = None
    score = None

    if request.method == "POST":

        user_input = request.form["userdata"]

        exposure, risk, score = analyze_data(user_input)

    return render_template("index.html", exposure=exposure, risk=risk, score=score)


if __name__ == "__main__":
    app.run()