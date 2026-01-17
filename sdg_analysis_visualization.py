import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Load CSV Data
# -------------------------------
data = pd.read_csv("sdg_data.csv")

# -------------------------------
# SDG-wise Average Scores
# -------------------------------
avg_health = data['health'].mean()        # SDG 3
avg_energy = data['energy'].mean()        # SDG 7
avg_consumption = data['consumption'].mean()  # SDG 12
avg_travel = data['travel'].mean()        # SDG 13

# -------------------------------
# Sustainability Index
# -------------------------------
data['sustainability_score'] = (
    data['health'] +
    data['energy'] +
    data['consumption'] -
    (data['travel'] / 5)
)

# -------------------------------
# Carbon Footprint Estimation
# -------------------------------
data['carbon_footprint'] = data['travel'] * 0.21  # kg CO2

# -------------------------------
# Visualization 1: SDG Scores
# -------------------------------
sdg_labels = ['SDG 3 Health', 'SDG 7 Energy', 'SDG 12 Consumption', 'SDG 13 Travel']
sdg_values = [avg_health, avg_energy, avg_consumption, avg_travel]

plt.figure()
plt.bar(sdg_labels, sdg_values)
plt.title("Average SDG Indicator Scores")
plt.ylabel("Score")
plt.xlabel("SDGs")
plt.show()

# -------------------------------
# Visualization 2: Sustainability Score
# -------------------------------
plt.figure()
plt.plot(data['sustainability_score'], marker='o')
plt.title("Sustainability Score per Record")
plt.ylabel("Score")
plt.xlabel("Record Index")
plt.show()

# -------------------------------
# Visualization 3: Carbon Footprint
# -------------------------------
plt.figure()
plt.scatter(data.index, data['carbon_footprint'])
plt.title("Carbon Footprint Distribution")
plt.xlabel("Record Index")
plt.ylabel("kg CO₂")
plt.show()

# -------------------------------
# Summary Output
# -------------------------------
print("Average Sustainability Score:",
      round(data['sustainability_score'].mean(), 2))

print("Average Carbon Footprint (kg CO2):",
      round(data['carbon_footprint'].mean(), 2))
