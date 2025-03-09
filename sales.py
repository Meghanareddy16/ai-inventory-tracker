import pandas as pd
import random

# Load the sales forecasting dataset
file_path = "/Users/meghanareddymacha/Downloads/dataset/stores_sales_forecasting.csv"
sales_forecasting = pd.read_csv(file_path, encoding="ISO-8859-1")

# Ensure 'Order Date' is in datetime format
sales_forecasting['Order Date'] = pd.to_datetime(sales_forecasting['Order Date'], errors='coerce')

# ✅ Generate random stock levels (simulate inventory data)
sales_forecasting['Stock_Available'] = [random.randint(50, 500) for _ in range(len(sales_forecasting))]

# ✅ Set AI-based reorder threshold (30% of stock)
sales_forecasting['Reorder_Level'] = sales_forecasting['Stock_Available'] * 0.3  

# ✅ Save updated stock data for AI-based restocking alerts
sales_forecasting.to_csv("simulated_stock_data.csv", index=False)
print("✅ AI-Simulated Stock Levels Created & Saved!")
