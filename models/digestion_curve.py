import numpy as np

# time-based digestion simulation (0–120 minutes)

def digestion_curve(beverage, steps=6):
    """
    Simulates nutrient release over time.
    """

    phytate = beverage["phytate"]

    time = np.linspace(0, 120, steps)

    # digestion rate slows with phytate
    rate = 0.9 - 0.2 * phytate
    if rate < 0:
        rate = 0

    curve = []

    for t in time:
        absorbed = (1 - np.exp(-rate * (t / 120)))

        curve.append({
            "time": round(t, 1),
            "protein": beverage["protein"] * absorbed,
            "calcium": beverage["calcium"] * absorbed,
            "iron": beverage["iron"] * absorbed
        })

    return curve
