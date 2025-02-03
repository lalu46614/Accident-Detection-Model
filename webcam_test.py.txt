from ultralytics import YOLO
import cv2

# Load your trained model
model_path = "C:\\Users\\lalu3\\Desktop\\Accident-Detection-Model\\runs\\detect\\train\\weights\\best.pt"
model = YOLO(model_path)

# Open webcam
cap = cv2.VideoCapture(0)  # Use 0 for default webcam, change if using an external camera

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run YOLOv8 on the frame
    results = model(frame)

    # Visualize results
    for r in results:
        annotated_frame = r.plot()  # Draw predictions on the frame
    
    # Display the frame
    cv2.imshow("Accident Detection", annotated_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
