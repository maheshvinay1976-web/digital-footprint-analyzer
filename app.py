from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    result = ""
    risk_score = 0
    messages = []

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        username = request.form.get("username")

        if name:
            risk_score += 10
            messages.append("Your name may appear in public records.")

        if email:
            risk_score += 40
            messages.append("Email addresses are commonly exposed in data breaches.")

        if phone:
            risk_score += 30
            messages.append("Phone numbers can be used for spam or phishing attacks.")

        if username:
            risk_score += 20
            messages.append("Usernames can reveal social media accounts.")

        risk_level = ""

        if risk_score <= 20:
            risk_level = "Low Risk"
        elif risk_score <= 50:
            risk_level = "Medium Risk"
        else:
            risk_level = "High Risk"

        result = f"Risk Score: {risk_score}% ({risk_level})"

        if messages:
            result += " | " + " ".join(messages)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
