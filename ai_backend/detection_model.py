import torch
from PIL import Image
import numpy as np

# Load a pre-trained lightweight model (e.g., YOLOv5)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_objects(image: Image):
    results = model(image)
    detections = results.pandas().xyxy[0].to_dict(orient="records")
    return {"detections": detections}
