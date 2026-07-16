import pandas as pd
import joblib

# Load the saved model
model = joblib.load("models/student_marks_model.pkl")

print("======================================")
print(" Student Marks Prediction System")
print("======================================\n")

# Take user input
study_hours = float(input("Enter Study Hours (1-10): "))
attendance = float(input("Enter Attendance (%): "))
previous_marks = float(input("Enter Previous Marks: "))
sleep_hours = float(input("Enter Sleep Hours: "))
assignments = float(input("Enter Number of Assignments: "))

# Create DataFrame
new_student = pd.DataFrame({
    "Study_Hours": [study_hours],
    "Attendance": [attendance],
    "Previous_Marks": [previous_marks],
    "Sleep_Hours": [sleep_hours],
    "Assignments": [assignments]
})

# Predict
prediction = model.predict(new_student)

print("\n==============================")
print(f"Predicted Final Marks: {prediction[0]:.2f}")
print("==============================")