from fastapi import FastAPI, File, UploadFile
import torch
import cv2
import numpy as np
from ultralytics import YOLO
from io import BytesIO
import os

app = FastAPI()

MODEL_PATH = r"C:\Users\lalu3\Desktop\Accident-Detection-Model\runs\detect\train\weights\best.pt"  # Update with your model path
model = YOLO(MODEL_PATH).to('cpu')  # Force CPU mode for debugging

# Function to read image or video frame
def read_video_frame(file: bytes) -> np.ndarray:
    image = np.frombuffer(file, np.uint8)
    return cv2.imdecode(image, cv2.IMREAD_COLOR)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Save the uploaded video to a temporary file
        temp_file_path = "temp_video.mp4"
        with open(temp_file_path, "wb") as f:
            f.write(await file.read())

        # Open the video
        cap = cv2.VideoCapture(temp_file_path)
        if not cap.isOpened():
            return {"error": "Error opening video"}

        accident_detected = False

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Perform inference on each frame
            results = model(frame)

            # Check for detection results
            if results and hasattr(results[0], 'boxes') and results[0].boxes is not None:
                boxes = results[0].boxes
                if len(boxes) > 0:
                    accident_detected = True
                    break  # If accident is detected in any frame, stop further processing

        # Close video file after processing
        cap.release()
        os.remove(temp_file_path)  # Clean up the temporary file

        return {"label": "Accident Detected" if accident_detected else "No Accident"}

    except Exception as e:
        return {"error": "Internal Server Error", "message": str(e)}
