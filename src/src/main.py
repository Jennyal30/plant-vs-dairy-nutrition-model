import pandas as pd

from src.meal_model import build_meal, aggregate_meal
from src.absorption import iron_absorption
from src.vitamin_a import vitamin_a_bio
from src.decision_layer import generate_recommendation

# 📊 Load data
df = pd.read_csv("data/foods.csv")

# 🍽️ Define meal (THIS is the key MICROSUNSET concept)
meal_foods = ["milk", "soy_milk", "oat_milk"]
meal = build_meal(df, meal_foods)

# 🧪 Aggregate nutrients
meal_totals = aggregate_meal(meal)

# ⚙️ Iron bioavailability
iron_bio = meal_totals["iron_mg"] * iron_absorption(
    meal_totals["iron_mg"],
    meal_totals["phytate_mg"],
    meal_totals["vitc_mg"],
    meal_totals["calcium_mg"]
)

# 🥕 Vitamin A bioavailability
vitA_bio = vitamin_a_bio(
    meal_totals["vitaminA_rae"],
    meal_totals["carotene_mg"],
    meal_totals["fat_g"]
)

# 📦 Final result object
result = {
    "iron_bio": iron_bio,
    "vitaminA_bio": vitA_bio,
    "calcium": meal_totals["calcium_mg"]
}

print("\n📊 MEAL BIOAVAILABILITY RESULT")
print(result)

# 🧠 Decision output (VERY IMPORTANT FOR PhD)
print("\n🧠 PROFESSIONAL GUIDANCE")
print(generate_recommendation(result))
