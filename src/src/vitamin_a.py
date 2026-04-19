def vitamin_a_bio(retinol, carotene, fat):
    """
    Vitamin A bioavailability model:
    - Retinol = directly absorbed
    - Beta-carotene = fat-dependent conversion
    """

    fat_factor = min(1.0, fat / 10)

    return retinol + 0.12 * carotene * fat_factor
