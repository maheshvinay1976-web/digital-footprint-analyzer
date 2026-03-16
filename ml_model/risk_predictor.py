def predict_risk(username_hits, social_accounts):

    score = 10

    score += len(username_hits) * 10
    score += len(social_accounts) * 15

    if score > 100:
        score = 100

    return score
