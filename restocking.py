import pandas as pd

# ✅ Load AI-Simulated Stock Data
file_path = "simulated_stock_data.csv"

try:
    sales_forecasting = pd.read_csv(file_path)
    print("✅ AI-Simulated Stock Data Loaded Successfully!")
except FileNotFoundError:
    print(f"❌ Error: File {file_path} not found! Run `sales.py` first to generate stock data.")
    exit()

# ✅ Function to check and trigger restocking alerts
def check_reorder(product_id, current_stock, reorder_level):
    if current_stock < reorder_level:
        print(f"⚠️ Reorder Alert for Product {product_id}: Current stock = {current_stock}, Reorder Level = {reorder_level}")

# ✅ Apply restocking alert function to the dataset
for index, row in sales_forecasting.iterrows():
    check_reorder(row['Order ID'], row['Stock_Available'], row['Reorder_Level'])
