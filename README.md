# Plant vs Dairy Bioavailability Model

This project models nutrient bioavailability in plant-based and dairy beverages using food composition data and anti-nutrient interactions.

## Data Source
USDA FoodData Central: https://fdc.nal.usda.gov/

## Features
- Iron, zinc, calcium, vitamin A bioavailability modelling
- Anti-nutrient adjustment (phytate, oxalate)
- Meal-level simulation
- Decision-support outputs

## Structure
src/ → models and logic  
data/ → food composition datasets  
figures/ → visual outputs  
results/ → generated outputs  

## Run
```bash
python src/main.py
