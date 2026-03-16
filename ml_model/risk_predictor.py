# Placeholder AI / risk scoring

def predict_risk(name, email, phone, username):
    """
    Simple risk scoring logic for demonstration.
    You can replace with ML model later.
    """
    score = 50  # base score
    if email.endswith("@gmail.com"):
        score += 10
    if phone.startswith("9"):
        score += 5
    if len(username) < 5:
        score += 5
    return min(score, 100)
