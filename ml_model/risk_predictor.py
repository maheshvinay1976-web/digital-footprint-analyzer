def predict_risk(breach_found, breach_count):
    score = 10

    if breach_found:
        score += breach_count * 20

    if score > 100:
        score = 100

    return score
