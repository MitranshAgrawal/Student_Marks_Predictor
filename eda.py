import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("dataset.csv")

# Histogram
plt.figure(figsize=(8,5))
plt.hist(data["Final_Marks"], bins=20)
plt.title("Distribution of Final Marks")
plt.xlabel("Final Marks")
plt.ylabel("Number of Students")
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(data["Study_Hours"], data["Final_Marks"])

plt.title("Study Hours vs Final Marks")
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")

plt.show()

# Import seaborn
import seaborn as sns

# Create correlation matrix
correlation = data.corr()

# Plot heatmap
plt.figure(figsize=(8,6))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.show()