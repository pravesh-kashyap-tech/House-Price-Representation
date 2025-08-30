# data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load CSV file
# -------------------------------
df = pd.read_csv("land_data.csv")   # CSV with Area and Price

print("✅ Data Loaded Successfully!\n")

# -------------------------------
# 2. Basic Data Analysis
# -------------------------------
print("📊 First 5 Rows of Data:")
print(df.head(), "\n")

print("ℹ️ Dataset Info:")
print(df.info(), "\n")

print("📈 Summary Statistics:")
print(df.describe(), "\n")

# Example: Calculate average of Price
average_price = df["Price"].mean()
print(f"🔹 Average Land Price: {average_price:.2f}\n")

# -------------------------------
# 3. Visualizations (Matplotlib only)
# -------------------------------

# Bar Chart 1: Price by Area
plt.figure(figsize=(8, 4))
plt.bar(df["Area"], df["Price"], color="skyblue")
plt.xlabel("Area (sq ft)")
plt.ylabel("Price ($)")
plt.title("Land Price by Area")
plt.show()

# Bar Chart 2: Average Price by Area Range (grouped every 500 sq ft)
df["Area_Range"] = (df["Area"] // 500) * 500   # group areas into 500 sq ft bins
avg_prices = df.groupby("Area_Range")["Price"].mean()

plt.figure(figsize=(8, 4))
avg_prices.plot(kind="bar", color="orange")
plt.xlabel("Area Range (sq ft)")
plt.ylabel("Average Price ($)")
plt.title("Average Price by Area Range")
plt.show()

# Scatter Plot: Area vs Price
plt.figure(figsize=(6, 4))
plt.scatter(df["Area"], df["Price"], color="green", alpha=0.6)
plt.xlabel("Area (sq ft)")
plt.ylabel("Price ($)")
plt.title("Scatter Plot: Area vs Price")
plt.show()

# Heatmap Alternative: Correlation Matrix using Matplotlib
corr_matrix = df.corr(numeric_only=True)

plt.figure(figsize=(5, 4))
plt.matshow(corr_matrix, cmap="coolwarm", fignum=1)
plt.colorbar(label="Correlation")
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.title("Correlation Matrix Heatmap (Matplotlib)", pad=20)
plt.show()

# -------------------------------
# 4. Insights & Observations
# -------------------------------
print("🔍 Insights & Observations:")

# Correlation insights
if "Area" in df.columns and "Price" in df.columns:
    correlation = df["Area"].corr(df["Price"])
    print(f"➡️ Correlation between Area and Price: {correlation:.2f}")
    if correlation > 0.7:
        print("➡️ Strong positive relationship: larger areas generally cost more.\n")
    elif correlation > 0.3:
        print("➡️ Moderate positive relationship between area and price.\n")
    else:
        print("➡️ Weak relationship between area and price.\n")

print("➡️ Average price shows the general cost trend.")
print("➡️ First bar chart shows individual land prices by area.")
print("➡️ Second bar chart shows average price per 500 sq ft group.")
print("➡️ Scatter plot confirms relationship between area and price.")
print("➡️ Heatmap provides overall correlation structure.")
