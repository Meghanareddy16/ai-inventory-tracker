import os
import cv2
import numpy as np
from ultralytics import YOLO
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()
firebase_cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# ✅ Initialize Firebase
if firebase_cred_path and not firebase_admin._apps:
    cred = credentials.Certificate(firebase_cred_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
else:
    print("❌ Firebase Initialization Failed: Missing Credentials")
    db = None  # Prevent further errors

# ✅ Load YOLOv8 Model
model_path = "runs/detect/train8/weights/best.pt"
model = YOLO(model_path)

# ✅ Define Image Processing Folder
image_folder = "dataset/test/"
processed_files = set()

def detect_empty_shelves(image_path):
    """Run YOLOv8 detection to identify empty shelves."""
    results = model(image_path)
    detections = []

    for r in results:
        if r.boxes is not None:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                cls_name = r.names.get(cls_id, "Unknown")  # Ensure no key errors
                confidence = float(box.conf[0])  # Get confidence score
                if confidence > 0.5:  # Filter low-confidence detections
                    detections.append(cls_name)
    
    return detections

# ✅ Process Images in the Folder
for filename in os.listdir(image_folder):
    if filename.endswith(('.jpg', '.png')) and filename not in processed_files:
        image_path = os.path.join(image_folder, filename)
        detections = detect_empty_shelves(image_path)
        
        if "empty_shelf" in detections:
            print(f"⚠ Empty shelves detected in {filename}! Restocking required.")
            doc_id = os.path.basename(image_path).split('.')[0]  # Use filename as ID
            doc_ref = db.collection("inventory").document(doc_id)
            doc_ref.set({
                "image_name": filename,
                "detections": detections,
                "timestamp": firestore.SERVER_TIMESTAMP
            })
        else:
            print(f"✅ No empty shelves detected in {filename}.")
        
        processed_files.add(filename)