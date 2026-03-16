def validate_email(email):
    return "@" in email and "." in email

def categorize_risk(score):
    if score < 30:
        return "Low Risk"
    elif score < 70:
        return "Medium Risk"
    else:
        return "High Risk"
