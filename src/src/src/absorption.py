def iron_absorption(iron, phytate, vitc, calcium):
    """
    Non-heme iron absorption model (dietary inhibition + enhancement)
    """

    base = 0.10  # plant-based baseline absorption

    absorption = base * (1 + 0.02 * vitc) / (
        1 + 0.001 * phytate + 0.0005 * calcium
    )

    return min(absorption, 0.25)


def zinc_absorption(zinc, phytate):
    """
    Phytate inhibits zinc absorption via ratio effect
    """

    if zinc == 0:
        return 0

    ratio = phytate / zinc
    return 0.5 / (1 + 0.03 * ratio)


def calcium_absorption(calcium, oxalate):
    """
    Oxalate reduces calcium absorption
    """

    return 0.3 / (1 + 0.002 * oxalate)
