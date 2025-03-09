import cv2
import numpy as np
import os

# Set the dataset folder path
image_folder = "/Users/meghanareddymacha/Downloads/dataset/train/images"  # Change this path if needed

# Function to calculate image brightness
def calculate_brightness(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
    return np.mean(img)  # Get average pixel brightness

# Scan images and calculate brightness
brightness_levels = []
for img_name in os.listdir(image_folder):
    img_path = os.path.join(image_folder, img_name)
    if img_name.endswith((".jpg", ".png", ".jpeg")):
        brightness = calculate_brightness(img_path)
        brightness_levels.append((img_name, brightness))

# Sort by brightness (low to high)
brightness_levels.sort(key=lambda x: x[1])

# Print the lowest brightness images
print("\n📉 Low-Brightness Images (Possible Low-Light Images):")
for img_name, brightness in brightness_levels[:5]:  # Show 5 lowest brightness images
    print(f"{img_name}: Brightness = {brightness:.2f}")

# Print the highest brightness images for comparison
print("\n☀️ High-Brightness Images (Well-Lit Samples):")
for img_name, brightness in brightness_levels[-5:]:  # Show 5 highest brightness images
    print(f"{img_name}: Brightness = {brightness:.2f}")
