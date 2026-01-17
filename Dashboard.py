import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# -------------------------------
# Get project directory
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------------------
# Function to run programs safely
# -------------------------------
def run_program(file_name, message=None):
    file_path = os.path.join(BASE_DIR, file_name)

    if not os.path.exists(file_path):
        messagebox.showerror(
            "File Not Found",
            f"Cannot find:\n{file_name}"
        )
        return

    try:
        subprocess.Popen([sys.executable, file_path])

        # Show confirmation for non-GUI programs
        if message:
            messagebox.showinfo("Program Executed", message)

    except Exception as e:
        messagebox.showerror("Execution Error", str(e))
# -------------------------------
# Tkinter Window
# -------------------------------
root = tk.Tk()
root.title("AI-Based SDG Project – Viva Dashboard")
root.geometry("620x520")
root.resizable(False, False)

# -------------------------------
# Title
# -------------------------------
tk.Label(
    root,
    text="AI-Based SDG Impact Analyzer",
    font=("Arial", 20, "bold")
).pack(pady=10)

tk.Label(
    root,
    text="Viva Demonstration Dashboard",
    font=("Arial", 12, "italic")
).pack(pady=5)

# -------------------------------
# Button Style
# -------------------------------
btn_style = {
    "font": ("Arial", 12, "bold"),
    "width": 42,
    "pady": 6
}

# -------------------------------
# Buttons
# -------------------------------
tk.Button(
    root, text="Program 1: GUI + ML Prediction",
    command=lambda: run_program("sdg_impact_analyzer_gui_csv.py"),
    **btn_style
).pack(pady=4)

tk.Button(
    root, text="Program 2: Data Analysis & Visualization",
    command=lambda: run_program("sdg_analysis_visualization.py"),
    **btn_style
).pack(pady=4)

tk.Button(
    root, text="Program 3: CSV Result Generator",
    command=lambda: run_program("sdg_result_generator.py"),
    **btn_style
).pack(pady=4)

tk.Button(
    root, text="Program 4: ML Model Evaluation",
    command=lambda: run_program(
        "sdg_ml_evaluation.py",
        "ML evaluation executed.\n\nCheck terminal for accuracy & report."
    ),
    **btn_style
).pack(pady=4)

tk.Button(
    root, text="Program 5: Dashboard with Charts",
    command=lambda: run_program("sdg_dashboard_charts_Ex.py"),
    **btn_style
).pack(pady=4)

tk.Button(
    root, text="Program 6: Carbon Footprint Calculator",
    command=lambda: run_program(
        "sdg_carbon_footprint_calculator.py",
        "Carbon footprint calculated.\n\nOutput saved to:\ncarbon_footprint_result.csv"
    ),
    **btn_style
).pack(pady=4)


tk.Button(
    root, text="Program 7: Automatic Report Generator",
    command=lambda: run_program(
        "sdg_project_report_generator.py",
        "Project report generated successfully.\n\nFile:\nSDG_Project_Report.txt / PDF"
    ),
    **btn_style
).pack(pady=4)

# -------------------------------
# Footer
# -------------------------------
tk.Label(
    root,
    text="SDGs Covered: SDG 3 • SDG 7 • SDG 12 • SDG 13",
    font=("Arial", 10)
).pack(side="bottom", pady=10)

root.mainloop()
