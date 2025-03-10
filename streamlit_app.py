import streamlit as st
import os
from glob import glob

# Streamlit UI
st.title("🛒 AI Inventory Tracker - Shelf Detection")

# Path to detected images
results_path = "/Users/meghanareddymacha/Downloads/dataset/runs/detect/predict17/"
image_paths = glob(os.path.join(results_path, "*.jpg"))

st.header("📂 Detected Shelves with YOLOv8")

if not image_paths:
    st.warning("No images found! Run detection first.")
else:
    for img_path in image_paths:
        st.image(img_path, caption=os.path.basename(img_path), use_column_width=True)

