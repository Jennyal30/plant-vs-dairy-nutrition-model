# Simplified in-vitro digestion simulation layer

def in_vitro_digestion(beverage):
    """
    Simulates digestion efficiency based on matrix type.
    This is a simplified proxy of INFOGEST-style digestion.
    """

    phytate = beverage["phytate"]

    # digestion efficiency (not absorption yet)
    digestion_efficiency = 0.85 - (0.15 * phytate)

    if digestion_efficiency < 0:
        digestion_efficiency = 0

    return {
        "digested_protein": beverage["protein"] * digestion_efficiency,
        "digested_calcium": beverage["calcium"] * digestion_efficiency,
        "digested_iron": beverage["iron"] * digestion_efficiency,
        "digestion_efficiency": round(digestion_efficiency, 2)
    }
