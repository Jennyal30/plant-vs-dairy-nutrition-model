# Bioavailability adjustment model

def adjusted_nutrients(beverage):
    phytate = beverage["phytate"]

    factor = 1 - (0.2 * phytate)
    if factor < 0:
        factor = 0

    return {
        "protein": beverage["protein"] * factor,
        "calcium": beverage["calcium"] * factor,
        "iron": beverage["iron"] * factor
    }
