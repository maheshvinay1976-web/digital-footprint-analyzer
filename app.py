from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def search_web(query):

    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for g in soup.find_all("h3"):
        results.append(g.text)

    return results


@app.route("/", methods=["GET", "POST"])
def index():

    result = ""
    found_sources = []
    risk_score = 0

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        username = request.form.get("username")

        if name:
            name_results = search_web(name)
            if len(name_results) > 0:
                risk_score += 20
                found_sources.append("Name appears in public search results")

        if email:
            email_results = search_web(email)
            if len(email_results) > 0:
                risk_score += 40
                found_sources.append("Email may appear in online sources")

        if phone:
            phone_results = search_web(phone)
            if len(phone_results) > 0:
                risk_score += 30
                found_sources.append("Phone number may appear online")

        if username:
            username_results = search_web(username)
            if len(username_results) > 0:
                risk_score += 20
                found_sources.append("Username may appear on websites or social media")

        if risk_score <= 30:
            level = "Low Risk"
        elif risk_score <= 60:
            level = "Medium Risk"
        else:
            level = "High Risk"

        result = f"Risk Score: {risk_score}% ({level})"

    return render_template("index.html", result=result, sources=found_sources)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
