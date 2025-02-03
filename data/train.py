from ultralytics import YOLO

# Load YOLOv8 pre-trained model
model = YOLO("yolov8s.pt")  # 'n' is the smallest, use 'm' or 'l' for better accuracy

# Train the model
model.train(
    data="C:\\Users\\lalu3\\Desktop\\Accident-Detection-Model\\data\\data.yaml",  # Correct path to data.yaml
    epochs=50,
    batch=8,
    imgsz=416,
    device="cpu"  # Use "cpu" if no GPU
)


# Save the trained model
model.export(format="onnx")  # Export for optimized inference
