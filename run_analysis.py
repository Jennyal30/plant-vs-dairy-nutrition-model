from data.beverages import beverages
from models.absorption import adjusted_nutrients
from models.digestion import in_vitro_digestion

print("BIOAVAILABILITY + DIGESTION COMPARISON\n")

for name, bev in beverages.items():

    digested = in_vitro_digestion(bev)
    absorbed = adjusted_nutrients(bev)

    print("Product:", name)

    print("\n-- In Vitro Digestion --")
    print("Protein:", round(digested["digested_protein"], 2))
    print("Calcium:", round(digested["digested_calcium"], 2))
    print("Iron:", round(digested["digested_iron"], 2))
    print("Digestion Efficiency:", digested["digestion_efficiency"])

    print("\n-- Absorption Adjusted --")
    print("Protein:", round(absorbed["protein"], 2))
    print("Calcium:", round(absorbed["calcium"], 2))
    print("Iron:", round(absorbed["iron"], 2))

    print("\n----------------------\n")
