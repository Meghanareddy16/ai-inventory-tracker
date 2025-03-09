import os
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# ✅ Set the correct file path
dataset_folder = "/Users/meghanareddymacha/Downloads/dataset"
file_name = "stores_sales_forecasting.csv"
file_path = os.path.join(dataset_folder, file_name)

# ✅ Check if the file exists before loading
if not os.path.exists(file_path):
    print(f"❌ Error: File {file_path} not found! Please check if the file is inside 'Downloads/dataset'.")
    exit()
else:
    print("✅ File found. Proceeding with forecast...")

# ✅ Fix: Use a different encoding format
try:
    sales_forecasting = pd.read_csv(file_path, encoding="ISO-8859-1")  # Alternative encodings: 'latin1' or 'windows-1252'
    print("✅ Data loaded successfully!")
except UnicodeDecodeError:
    print("❌ UnicodeDecodeError: Retrying with a different encoding...")
    sales_forecasting = pd.read_csv(file_path, encoding="latin1")
    print("✅ Data loaded using 'latin1' encoding.")

# ✅ Ensure 'Order Date' column is in datetime format
if 'Order Date' in sales_forecasting.columns:
    sales_forecasting['Order Date'] = pd.to_datetime(sales_forecasting['Order Date'], errors='coerce')
else:
    print("❌ Error: 'Order Date' column not found in dataset.")
    exit()

# ✅ Prepare dataset for Prophet forecasting
df = sales_forecasting[['Order Date', 'Sales']]
df.columns = ['ds', 'y']  # Prophet requires 'ds' (date) & 'y' (sales value)

# ✅ Initialize Prophet model
model = Prophet()
model.fit(df)

# ✅ Create future dates for prediction
future = model.make_future_dataframe(periods=30)  # Forecast next 30 days
forecast = model.predict(future)

# ✅ Fix Plotly warning (Install if missing)
try:
    import plotly
except ImportError:
    print("⚠️ Warning: Plotly is not installed. Install it using 'pip install plotly' for interactive graphs.")

# ✅ Plot forecasted results
model.plot(forecast)
plt.title("📈 AI-Powered Sales Forecasting")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

# ✅ Save the forecast data
forecast[['ds', 'yhat']].to_csv("sales_forecast.csv", index=False)
print("✅ Sales Forecasting Completed & Data Saved!")
