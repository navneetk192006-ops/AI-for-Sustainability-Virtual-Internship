import pandas as pd
from datetime import date

# -------------------------------
# Load Processed Data
# -------------------------------
sdg_data = pd.read_csv("sdg_analysis_result.csv")
carbon_data = pd.read_csv("carbon_footprint_result.csv")

# -------------------------------
# Summary Calculations
# -------------------------------
avg_sustainability = round(sdg_data['sustainability_score'].mean(), 2)
avg_carbon_daily = round(carbon_data['total_daily_co2'].mean(), 2)
avg_carbon_annual = round(carbon_data['annual_co2'].mean(), 2)

high_footprint_count = len(
    carbon_data[carbon_data['footprint_level'] == "High"]
)

# -------------------------------
# Report Content
# -------------------------------
report = f"""
AI-BASED SUSTAINABLE DEVELOPMENT GOAL (SDG) IMPACT ANALYZER
==========================================================

Date: {date.today()}

1. INTRODUCTION
----------------
Sustainable Development Goals (SDGs) aim to create a balanced and
environmentally responsible future. This project uses Artificial
Intelligence and Data Analysis to measure sustainability behavior
and environmental impact.

2. SDGs COVERED
----------------
• SDG 3  : Good Health and Well-Being
• SDG 7  : Affordable and Clean Energy
• SDG 12 : Responsible Consumption
• SDG 13 : Climate Action

3. TECHNOLOGY STACK
-------------------
• Programming Language : Python 3
• Libraries           : Pandas, Scikit-learn, Matplotlib, Tkinter
• Data Format         : CSV
• Platform            : Windows / Linux / macOS

4. METHODOLOGY
---------------
• Data collection using CSV datasets
• Sustainability score calculation
• Machine learning prediction of sustainable behavior
• Carbon footprint estimation using emission factors
• Visualization and dashboard creation
• Automated report generation

5. RESULTS AND ANALYSIS
-----------------------
Average Sustainability Score : {avg_sustainability}

Average Daily Carbon Footprint (kg CO₂)  : {avg_carbon_daily}
Average Annual Carbon Footprint (kg CO₂) : {avg_carbon_annual}

High Carbon Footprint Records : {high_footprint_count}

The results indicate that lifestyle choices such as travel,
energy usage, and consumption significantly influence sustainability.

6. CONCLUSION
--------------
The AI-Based SDG Impact Analyzer successfully evaluates sustainability
behavior and environmental impact. The system provides intelligent
recommendations and supports informed decision-making aligned with
global sustainability goals.

7. FUTURE ENHANCEMENTS
----------------------
• Web-based dashboard
• Real-time data collection
• Integration with IoT sensors
• Advanced machine learning models

----------------------------------------------------------
End of Report
"""

# -------------------------------
# Save Report
# -------------------------------
with open("SDG_Project_Report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("Project Report Generated Successfully!")
print("File saved as SDG_Project_Report.txt")
