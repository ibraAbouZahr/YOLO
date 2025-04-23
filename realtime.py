from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # You can swap with yolov8s.pt

cap = cv2.VideoCapture(0)  # Webcam. 

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
