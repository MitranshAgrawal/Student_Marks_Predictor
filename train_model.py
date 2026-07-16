import joblib
# Import pandas
import pandas as pd

# Load dataset
data = pd.read_csv("dataset.csv")

# Display dataset
print("===== Student Marks Dataset =====")
print(data)

# Shape of dataset
print("\n===== Shape of Dataset =====")
print(data.shape)

# Column names
print("\n===== Column Names =====")
print(data.columns)

# Basic information
print("\n===== Dataset Information =====")
print(data.info())

# Statistical summary
print("\n===== Statistical Summary =====")
print(data.describe())

# Check for missing values
print("\n===== Missing Values =====")
print(data.isnull().sum())

# Features (Input)
X = data[['Study_Hours', 'Attendance', 'Previous_Marks', 'Sleep_Hours', 'Assignments']]

# Target (Output)
y = data['Final_Marks']

print("\n===== Features (X) =====")
print(X)

print("\n===== Target (y) =====")
print(y)

# Import train_test_split
from sklearn.model_selection import train_test_split

# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n===== Training Features =====")
print(X_train)

print("\n===== Testing Features =====")
print(X_test)

print("\n===== Training Target =====")
print(y_train)

print("\n===== Testing Target =====")
print(y_test)

# Import Linear Regression
from sklearn.linear_model import LinearRegression

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "models/student_marks_model.pkl")

print("\n✅ Model saved successfully!")

print("\n===== Model Trained Successfully =====")

# Predict marks for the testing data
predictions = model.predict(X_test)

print("\n===== Predicted Marks =====")
print(predictions)

print("\n===== Actual Marks =====")
print(y_test.values)

# Import evaluation metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Calculate metrics
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n===== Model Evaluation =====")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R2 Score: {r2:.2f}")