# 🎓 Student Marks Prediction System

An end-to-end Machine Learning project that predicts a student's final marks based on academic and lifestyle factors.

---

## 📌 Project Overview

This project uses a **Linear Regression** model to predict students' final marks using the following features:

- 📚 Study Hours
- 🏫 Attendance
- 📝 Previous Marks
- 😴 Sleep Hours
- 📂 Assignments Completed

The project also includes an interactive web application built using **Streamlit**.

---

## 🚀 Features

- ✅ Synthetic Dataset Generator (1000 Students)
- ✅ Exploratory Data Analysis (EDA)
- ✅ Histogram Visualization
- ✅ Scatter Plot
- ✅ Correlation Heatmap
- ✅ Linear Regression Model
- ✅ Model Evaluation
- ✅ Save & Load Model using Joblib
- ✅ Interactive Streamlit Web App
- ✅ Student Performance Feedback
- ✅ Progress Meter
- ✅ User-Friendly Interface

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Streamlit
- Joblib

---

## 📂 Project Structure

```
Student_Marks_Predictor
│
├── models/
│   └── student_marks_model.pkl
│
├── screenshots/
│
├── dataset.csv
├── generate_dataset.py
├── train_model.py
├── predict.py
├── eda.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Model Performance

| Metric | Value |
|---------|--------|
| MAE | 2.39 |
| MSE | 9.12 |
| R² Score | 0.95 |

---

## ▶️ How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Train the model

```bash
python train_model.py
```

### Run the web application

```bash
streamlit run app.py
```

---

## 📸 Screenshots



Example:

- Home Page
- Prediction Result
- Correlation Heatmap

---

## 📈 Future Improvements

- Deploy on Streamlit Cloud
- Try Random Forest Regression
- Use a Real Student Dataset
- Add Login System
- Export Prediction Report as PDF

---

## 👨‍💻 Developer

**Mitransh Agrawal**

B.Tech AI & ML Student

Noida International University

---

⭐ If you found this project useful, consider giving it a star.
