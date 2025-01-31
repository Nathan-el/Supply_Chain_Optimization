import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Define the date range (6 months)
days = pd.date_range(start="2024-01-01", end="2024-06-30")

# Generate random values for production and demand
daily_production = np.random.randint(800, 1200, len(days))  # Eggs produced per day
daily_demand = np.random.randint(750, 1000, len(days))  # Eggs requested by businesses
spoilage_rate = 0.02  # 2% of inventory spoils each day

# Initialize storage for data
data = []
inventory = 0  # Starting inventory

for i, date in enumerate(days):
    produced = daily_production[i]
    demand = daily_demand[i]
    
    spoilage = int(inventory * spoilage_rate)  # Eggs that spoil each day
    delivery = min(inventory + produced - spoilage, demand)  # Deliver as much as possible
    inventory = max(inventory + produced - spoilage - delivery, 0)  # Update inventory
    
    revenue = delivery * 0.15  # Assume $0.15 per egg sold
    
    data.append([date.strftime("%Y-%m-%d"), produced, demand, inventory, spoilage, delivery, revenue])

# Create a DataFrame
df = pd.DataFrame(data, columns=[
    "Date", "Eggs Produced", "Demand", "Inventory", "Spoilage", "Delivery Quantity", "Revenue"
])

# Save to CSV (optional)
df.to_csv("dovakin_farms_data.csv", index=False)

# Display full dataset (remove limit to see all rows)
print(df.to_string())  # Print full DataFrame




# Load the dataset
df = pd.read_csv("dovakin_farms_data.csv")

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Quick overview
print(df.head())  # Check first few rows
print(df.info())  # Check data types
print(df.describe())  # Summary statistics


#This code visualizes the Inventory Trends for 6 months

plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Inventory"], marker="o", linestyle="-", label="Inventory")
plt.xlabel("Date")
plt.ylabel("Eggs in Inventory")
plt.title("Inventory Levels Over 6 Months")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()

#This code visualizes the Spoilage Analysis for 6 months

plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Spoilage"], color="red", linestyle="--", label="Spoilage")
plt.xlabel("Date")
plt.ylabel("Spoiled Eggs")
plt.title("Daily Spoilage Over 6 Months")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()



#This code visualizes the Demand vs Delivery or Supply of the business for the next 6 months
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Demand"], label="Demand", linestyle="-")
plt.plot(df["Date"], df["Delivery Quantity"], label="Deliveries", linestyle="--")
plt.xlabel("Date")
plt.ylabel("Eggs")
plt.title("Demand vs. Deliveries")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()




#This code visualizes the revenue trends data over 6 months
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Revenue"], color="green", linestyle="-", marker="o", label="Revenue ($)")
plt.xlabel("Date")
plt.ylabel("Revenue in Dollars")
plt.title("Daily Revenue Trends Over 6 Months")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()

