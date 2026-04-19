from data.beverages import beverages
from models.absorption import adjusted_nutrients

print("BIOAVAILABILITY COMPARISON\n")

for name, bev in beverages.items():
    result = adjusted_nutrients(bev)

    print("Product:", name)
    print("Protein:", round(result["protein"], 2))
    print("Calcium:", round(result["calcium"], 2))
    print("Iron:", round(result["iron"], 2))
    print("----------------------")
