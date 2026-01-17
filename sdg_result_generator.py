import pandas as pd

# -------------------------------
# Load Input Data
# -------------------------------
data = pd.read_csv("sdg_data.csv")

# -------------------------------
# Sustainability Score
# -------------------------------
data['sustainability_score'] = (
    data['health'] +
    data['energy'] +
    data['consumption'] -
    (data['travel'] / 5)
)

# -------------------------------
# Carbon Footprint
# -------------------------------
data['carbon_footprint'] = data['travel'] * 0.21  # kg CO2

# -------------------------------
# Recommendation Logic
# -------------------------------
def recommend(row):
    if row['sustainability_score'] < 10:
        return "Reduce travel, improve energy usage, consume responsibly"
    else:
        return "Maintain sustainable lifestyle and promote awareness"

data['recommendation'] = data.apply(recommend, axis=1)

# -------------------------------
# Save Output
# -------------------------------
data.to_csv("sdg_analysis_result.csv", index=False)

print("Analysis completed successfully.")
print("Results saved to sdg_analysis_result.csv")
