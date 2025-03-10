from ultralytics import YOLO

model_path = "/Users/meghanareddymacha/Downloads/dataset/runs/detect/train8/weights/best.pt"
model = YOLO(model_path)

# Print all class names
print("🔍 Model Class Names:", model.names)
