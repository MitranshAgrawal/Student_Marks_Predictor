import pandas as pd
import numpy as np

# Make the random numbers reproducible
np.random.seed(42)

# Number of students
num_students = 1000

# Generate features
study_hours = np.random.randint(1, 11, num_students)
attendance = np.random.randint(50, 101, num_students)
previous_marks = np.random.randint(35, 96, num_students)
sleep_hours = np.random.randint(4, 10, num_students)
assignments = np.random.randint(0, 11, num_students)

# Random variation
noise = np.random.normal(0, 3, num_students)

# Calculate final marks
final_marks = (
    previous_marks * 0.30 +
    study_hours * 3 +
    attendance * 0.20 +
    assignments * 2 +
    sleep_hours * 1.5 +
    noise
)

# Keep marks between 0 and 100
final_marks = np.clip(final_marks, 0, 100)

# Round marks
final_marks = np.round(final_marks, 2)

# Create DataFrame
data = pd.DataFrame({
    "Study_Hours": study_hours,
    "Attendance": attendance,
    "Previous_Marks": previous_marks,
    "Sleep_Hours": sleep_hours,
    "Assignments": assignments,
    "Final_Marks": final_marks
})

# Save dataset
data.to_csv("dataset.csv", index=False)

print("✅ Dataset generated successfully!")
print(data.head())