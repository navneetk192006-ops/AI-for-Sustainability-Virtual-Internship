import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LogisticRegression

# -------------------------------
# Load CSV Data
# -------------------------------
try:
    data = pd.read_csv("sdg_data.csv")
except FileNotFoundError:
    messagebox.showerror("Error", "sdg_data.csv file not found")
    exit()

X = data[['health', 'energy', 'consumption', 'travel']]
y = data['sustainable']

# Train ML model
model = LogisticRegression()
model.fit(X, y)

# -------------------------------
# Analysis Function
# -------------------------------
def analyze():
    try:
        health = int(health_entry.get())
        energy = int(energy_entry.get())
        consumption = int(cons_entry.get())
        travel = int(travel_entry.get())

        # Sustainability score
        score = (health + energy + consumption) - (travel / 5)
        score = round(score, 2)

        # Carbon footprint estimation
        carbon = round(travel * 0.21, 2)  # kg CO2/day approx

        # ML Prediction
        prediction = model.predict([[health, energy, consumption, travel]])
        status = "SUSTAINABLE ✅" if prediction[0] == 1 else "NOT SUSTAINABLE ❌"

        # Recommendations
        if prediction[0] == 0:
            advice = (
                "• Reduce travel distance\n"
                "• Shift to clean energy\n"
                "• Avoid over-consumption\n"
                "• Improve health habits"
            )
        else:
            advice = (
                "• Maintain eco-friendly habits\n"
                "• Promote renewable energy\n"
                "• Practice responsible living"
            )

        result_label.config(
            text=f"Sustainability Score: {score}\n"
                 f"Carbon Footprint: {carbon} kg CO₂/day\n"
                 f"Prediction: {status}\n\n"
                 f"Recommendations:\n{advice}"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values")

# -------------------------------
# Tkinter GUI
# -------------------------------
root = tk.Tk()
root.title("AI-Based SDG Impact Analyzer")
root.geometry("540x500")
root.resizable(False, False)

tk.Label(root, text="AI-Based SDG Impact Analyzer",
         font=("Arial", 18, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Health Score (1–10):").grid(row=0, column=0, sticky="w")
health_entry = tk.Entry(frame)
health_entry.grid(row=0, column=1)

tk.Label(frame, text="Clean Energy Usage (1–10):").grid(row=1, column=0, sticky="w")
energy_entry = tk.Entry(frame)
energy_entry.grid(row=1, column=1)

tk.Label(frame, text="Responsible Consumption (1–10):").grid(row=2, column=0, sticky="w")
cons_entry = tk.Entry(frame)
cons_entry.grid(row=2, column=1)

tk.Label(frame, text="Daily Travel (km):").grid(row=3, column=0, sticky="w")
travel_entry = tk.Entry(frame)
travel_entry.grid(row=3, column=1)

tk.Button(
    root,
    text="Analyze Sustainability",
    font=("Arial", 12, "bold"),
    bg="#2e7d32",
    fg="white",
    command=analyze
).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

tk.Label(
    root,
    text="SDGs Covered: SDG 3 • SDG 7 • SDG 12 • SDG 13",
    font=("Arial", 10, "italic")
).pack(side="bottom", pady=10)

root.mainloop() 
