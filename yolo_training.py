import os
from ultralytics import YOLO
import torch

# Set up device
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")

# Load pretrained model
model = YOLO("yolov8s.pt")

# Function to predict tablet name
def predict_tablet_name(image_path):
    results = model(image_path)
    
    # Print all class names detected in the image
    print("Detected Classes and their IDs:")
    for i, name in enumerate(results[0].names):
        print(f"{i}: {name}")
    
    # Check if any objects are detected
    if results[0].boxes is not None and len(results[0].boxes) > 0:
        # Get the detected class ID of the first detected object
        class_id = int(results[0].boxes[0].cls[0])  # Get class ID of the first detected box
        tablet_name = results[0].names[class_id]
        return tablet_name
    else:
        return "No tablet detected."