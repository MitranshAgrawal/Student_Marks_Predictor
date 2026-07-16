import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/student_marks_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Student Marks Predictor",
    page_icon="🎓",
    layout="centered"
)

# Sidebar
st.sidebar.title("🎓 About Project")

st.sidebar.write("""
This project predicts a student's final marks using a Machine Learning model.

### Algorithm
- Linear Regression

### Dataset
- 1000 Synthetic Student Records

### Model Accuracy
- R² Score: 0.95

### Developer
- Mitransh Agrawal
""")

# Title
st.title("🎓 Student Marks Prediction System")

st.info("📊 Model Accuracy (R² Score): 0.95")

st.write(
    "Enter the student's details below and click **Predict Marks**."
)

# Input fields
study_hours = st.slider("Study Hours", 1, 10, 5)

attendance = st.slider("Attendance (%)", 50, 100, 75)

previous_marks = st.slider("Previous Marks", 35, 100, 60)

sleep_hours = st.slider("Sleep Hours", 4, 10, 7)

assignments = st.slider("Assignments Completed", 0, 10, 5)

# Predict button
if st.button("Predict Marks"):

    new_student = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance],
        "Previous_Marks": [previous_marks],
        "Sleep_Hours": [sleep_hours],
        "Assignments": [assignments]
    })

    prediction = model.predict(new_student)

    marks = prediction[0]

    st.success(f"🎯 Predicted Final Marks: {marks:.2f}")

    st.progress(min(int(marks), 100))

    st.subheader("📈 Performance Meter")

    if marks >= 90:
        st.metric("Performance", "Excellent 🌟")

    elif marks >= 75:
        st.metric("Performance", "Very Good 👍")

    elif marks >= 60:
        st.metric("Performance", "Good 🙂")

    else:
        st.metric("Performance", "Needs Improvement 📚")

    if marks >= 90:
        feedback = """
    Excellent work!

    • Keep maintaining your study routine.
    • Continue completing assignments.
    • Aim for consistency.
    """

    elif marks >= 75:
        feedback = """
    Very good!

    • Increase study time slightly.
    • Revise regularly.
    • Focus on weak subjects.
    """

    elif marks >= 60:
        feedback = """
    Good, but there's room to improve.

    • Study 1–2 more hours daily.
    • Improve attendance.
    • Solve more practice questions.
    """

    else:
        feedback = """
    Needs Improvement.

    • Increase study hours.
    • Improve attendance.
    • Complete all assignments.
    """

    st.subheader("💡 Suggestions")

    st.write(feedback)

    st.subheader("📋 Input Summary")

    st.write(f"📚 Study Hours: {study_hours}")
    st.write(f"🏫 Attendance: {attendance}%")
    st.write(f"📝 Previous Marks: {previous_marks}")
    st.write(f"😴 Sleep Hours: {sleep_hours}")
    st.write(f"📂 Assignments: {assignments}")

    student_data = pd.DataFrame({
        "Feature": [
            "Study Hours",
            "Attendance",
            "Previous Marks",
            "Sleep Hours",
            "Assignments"
        ],
        "Value": [
            study_hours,
            attendance,
            previous_marks,
            sleep_hours,
            assignments
        ]
    })

    st.table(student_data)
    st.divider()

    st.caption(
        "Developed by Mitransh Agrawal | AI/ML Student | Student Marks Prediction System"
    )