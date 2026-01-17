import pandas as pd

# -------------------------------
# Emission Factors (Approximate)
# -------------------------------
EMISSION_TRAVEL = 0.21      # kg CO2 per km
EMISSION_ELECTRICITY = 0.82 # kg CO2 per unit
EMISSION_LPG = 3.0          # kg CO2 per kg LPG
LPG_PER_CYLINDER = 14.2     # kg
SHOPPING_FACTOR = 0.5       # kg CO2 per score unit

# -------------------------------
# Load Data
# -------------------------------
data = pd.read_csv("carbon_input.csv")

# -------------------------------
# Calculations
# -------------------------------
data['travel_emission'] = data['travel_km'] * EMISSION_TRAVEL
data['electricity_emission'] = data['electricity_units'] * EMISSION_ELECTRICITY
data['lpg_emission'] = (
    data['lpg_cylinders'] * LPG_PER_CYLINDER * EMISSION_LPG
)
data['shopping_emission'] = data['shopping_score'] * SHOPPING_FACTOR

data['total_daily_co2'] = (
    data['travel_emission'] +
    data['electricity_emission'] +
    data['lpg_emission'] +
    data['shopping_emission']
)

data['annual_co2'] = data['total_daily_co2'] * 365

# -------------------------------
# Classification
# -------------------------------
def footprint_level(value):
    if value < 10:
        return "Low"
    elif value < 25:
        return "Moderate"
    else:
        return "High"

data['footprint_level'] = data['total_daily_co2'].apply(footprint_level)

# -------------------------------
# Save Output
# -------------------------------
data.to_csv("carbon_footprint_result.csv", index=False)

# -------------------------------
# Summary
# -------------------------------
print("Carbon Footprint Calculation Completed\n")
print("Average Daily CO2 (kg):",
      round(data['total_daily_co2'].mean(), 2))
print("Average Annual CO2 (kg):",
      round(data['annual_co2'].mean(), 2))
