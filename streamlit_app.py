import streamlit as st
import os
import process_images  

# Streamlit UI
st.title("🛒 AI Inventory Tracker - Shelf Detection")
st.success("✅ YOLO model loaded successfully!")

st.header("📂 Detect Empty Shelves in Inventory")

# ✅ Process all images automatically
results_dict = process_images.process_all_images()  
empty_shelf_detected = False  # Flag to check if empty shelves exist

for img_path, detections in results_dict.items():
    st.image(img_path, caption=f"Processing {os.path.basename(img_path)}", use_column_width=True)

    if "Empty_shelf" in detections:
        empty_shelf_detected = True
        st.error(f"⚠ Empty shelves detected in {os.path.basename(img_path)}! Restocking required.")
    else:
        st.success(f"✅ No empty shelves detected in {os.path.basename(img_path)}.")

if not empty_shelf_detected:
    st.success("🎉 All shelves are fully stocked!")

st.info("💡 This tool automatically scans all images in the dataset and reports empty shelves.")
