import tkinter as tk
from tkinter import messagebox, scrolledtext
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# -------------------------------
# ML Evaluation Logic
# -------------------------------
def evaluate_model():
    try:
        # Load Dataset
        data = pd.read_csv("sdg_data.csv")

        X = data[['health', 'energy', 'consumption', 'travel']]
        y = data['sustainable']

        # Train-Test Split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        # Train Model
        model = LogisticRegression()
        model.fit(X_train, y_train)

        # Predictions
        y_pred = model.predict(X_test)

        # Evaluation
        accuracy = round(accuracy_score(y_test, y_pred) * 100, 2)
        report = classification_report(y_test, y_pred)

        # Display Results
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, f"Model Accuracy: {accuracy} %\n\n")
        output_box.insert(tk.END, "Classification Report:\n")
        output_box.insert(tk.END, report)

    except FileNotFoundError:
        messagebox.showerror("Error", "sdg_data.csv file not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# -------------------------------
# Tkinter GUI
# -------------------------------
root = tk.Tk()
root.title("ML Model Evaluation – SDG Project")
root.geometry("700x500")
root.resizable(False, False)

tk.Label(
    root,
    text="Machine Learning Model Evaluation",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Button(
    root,
    text="Run Model Evaluatioen",
    font=("Arial", 12, "bold"),
    bg="#1976d2",
    fg="white",
    command=evaluate_model
).pack(pady=10)

output_box = scrolledtext.ScrolledText(
    root,
    width=80,
    height=20,
    font=("Courier New", 10)
)
output_box.pack(pady=10)

tk.Label(
    root,
    text="Dataset: sdg_data.csv | Model: Logistic Regression",
    font=("Arial", 10, "italic")
).pack(pady=5)

root.mainloop()
