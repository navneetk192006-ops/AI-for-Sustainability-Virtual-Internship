import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# -------------------------------
# Load CSV Data
# -------------------------------
data = pd.read_csv("sdg_data.csv")

# -------------------------------
# Calculations
# -------------------------------
avg_health = data['health'].mean()
avg_energy = data['energy'].mean()
avg_consumption = data['consumption'].mean()
avg_travel = data['travel'].mean()

data['carbon_footprint'] = data['travel'] * 0.21

# -------------------------------
# Tkinter Window
# -------------------------------
root = tk.Tk()
root.title("SDG Impact Dashboard")
root.geometry("900x600")

tk.Label(
    root,
    text="AI-Based SDG Impact Dashboard",
    font=("Arial", 18, "bold")
).pack(pady=10)

# -------------------------------
# Frame for Charts
# -------------------------------
chart_frame = tk.Frame(root)
chart_frame.pack(fill="both", expand=True)

# -------------------------------
# Chart 1: SDG Scores Bar Chart
# -------------------------------
fig1 = plt.Figure(figsize=(4.5, 4), dpi=100)
ax1 = fig1.add_subplot(111)

sdg_labels = ['Health (SDG 3)', 'Energy (SDG 7)',
              'Consumption (SDG 12)', 'Travel (SDG 13)']
sdg_values = [avg_health, avg_energy, avg_consumption, avg_travel]

ax1.bar(sdg_labels, sdg_values)
ax1.set_title("Average SDG Indicator Scores")
ax1.set_ylabel("Score")

canvas1 = FigureCanvasTkAgg(fig1, master=chart_frame)
canvas1.draw()
canvas1.get_tk_widget().grid(row=0, column=0, padx=20, pady=20)

# -------------------------------
# Chart 2: Carbon Footprint Line Chart
# -------------------------------
fig2 = plt.Figure(figsize=(4.5, 4), dpi=100)
ax2 = fig2.add_subplot(111)

ax2.plot(data['carbon_footprint'], marker='o')
ax2.set_title("Carbon Footprint per Record")
ax2.set_xlabel("Record Index")
ax2.set_ylabel("kg CO₂")

canvas2 = FigureCanvasTkAgg(fig2, master=chart_frame)
canvas2.draw()
canvas2.get_tk_widget().grid(row=0, column=1, padx=20, pady=20)

# -------------------------------
# Footer
# -------------------------------
tk.Label(
    root,
    text="SDGs Covered: SDG 3 • SDG 7 • SDG 12 • SDG 13",
    font=("Arial", 10, "italic")
).pack(pady=10)

root.mainloop()
