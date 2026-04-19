import pandas as pd

def build_meal(df, food_list):
    """
    Select foods in a meal
    """

    return df[df["food"].isin(food_list)]


def aggregate_meal(meal_df):
    """
    Convert food-level → meal-level nutrients
    """

    return meal_df.sum(numeric_only=True)
