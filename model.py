def predict_segment(data):
    clicks = data["clicks"].values[0]
    time_spent = data["time_spent"].values[0]
    activity = data["activity"].values[0]

    # Since data is normalized (0–1), adjust scoring
    score = (clicks * 0.4) + (time_spent * 0.4) + (activity * 0.2)

    if score < 0.3:
        return "🟢 Low Engagement"
    elif score < 0.7:
        return "🟡 Medium Engagement"
    else:
        return "🔴 High Engagement"