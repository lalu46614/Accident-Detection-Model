import cv2
import torch
import numpy as np
import os
from ultralytics import YOLO

# Load your trained model
MODEL_PATH = "D:/Accident-Detection-Model/runs/detect/train/weights/best.pt"  # Update with your model path
model = YOLO(MODEL_PATH)

# Load the video
VIDEO_PATH = r"C:\Users\lalu3\Downloads\sample.mp4"  # Update with your test video path
OUTPUT_FOLDER = os.path.abspath("output_videos")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
OUTPUT_PATH = os.path.join(OUTPUT_FOLDER, "output_video.avi")

# Check if the video file exists
if not os.path.exists(VIDEO_PATH):
    print(f"Error: Video file not found at {VIDEO_PATH}")
    exit()

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("Error: Could not open input video file.")
    exit()

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, 20.0, (frame_width, frame_height))

# Check if VideoWriter opened successfully
if not out.isOpened():
    print("Error: Could not open output video file.")
    cap.release()
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Perform inference
    results = model(frame)
    
    # Check if results contain valid detections
    if results and results[0] is not None and hasattr(results[0], 'boxes') and results[0].boxes is not None:
        boxes = results[0].boxes  # Get detected bounding boxes
        if len(boxes) > 0:
            label = "Accident"
            color = (0, 0, 255)  # Red for accident
            
            # Draw bounding boxes on the frame
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get the coordinates of the bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)  # Draw rectangle
            print("Accident detected!")
        else:
            label = "No Accident"
            color = (0, 255, 0)  # Green for no accident
    else:
        print("Warning: No detections in this frame.")
        out.write(frame)
        continue
    
    # Display result with label
    cv2.putText(frame, label, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    
    # Write frame to output video
    out.write(frame)
    
    cv2.imshow("Accident Detection", frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
