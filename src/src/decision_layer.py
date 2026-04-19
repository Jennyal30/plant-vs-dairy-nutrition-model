def generate_recommendation(result):
    """
    Converts numbers → professional dietary guidance
    """

    advice = []

    if result.get("iron_bio", 0) < 1:
        advice.append("Low iron bioavailability → pair with vitamin C foods")

    if result.get("calcium", 0) < 300:
        advice.append("Low calcium → consider dairy or fortified alternatives")

    if result.get("vitaminA_bio", 0) < 500:
        advice.append("Low vitamin A → add beta-carotene rich foods")

    return advice if advice else ["Adequate nutrient profile"]
