import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import tempfile
import os

# In object detection using YOLO (You Only Look Once), each predicted object is assigned a confidence score, a probability between 0 and 1.
# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(page_title="YOLOv8 Object Detector", layout="wide")

st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: 700;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #6c757d;
            margin-bottom: 30px;
        }
        .st-emotion-cache-1v0mbdj {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🔍 Real-Time Object Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Using YOLOv8 - Powered by Ultralytics & Streamlit</div>', unsafe_allow_html=True)

# -------------------------
# Sidebar Configuration
# -------------------------
with st.sidebar:
    st.header("⚙️ Detection Settings")
    confidence = st.slider("Confidence Threshold", 0.1, 1.0, 0.25, 0.05)
    st.markdown("---")
    uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])
    uploaded_video = st.file_uploader("🎥 Upload a video", type=["mp4", "avi", "mov"])
    st.markdown("Made with ❤️ by Ibrahim Abou Zahr & Mohamad Mawed")
    st.markdown("---")
    st.subheader("🔗 Connect with us on LinkedIn")
    st.markdown("""
    - [Ibrahim Abou Zahr](https://www.linkedin.com/in/ibrahim-abouzahr-dev/)
    - [Mohamad El Mawed](https://www.linkedin.com/in/mohamad-el-mawed-dev/)
    """)

model = YOLO("yolov8n.pt")

# -------------------------
# Image Logic
# -------------------------
if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    results = model(image_np, conf=confidence)
    annotated_bgr = results[0].plot()
    annotated_rgb = cv2.cvtColor(annotated_bgr, cv2.COLOR_BGR2RGB)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📷 Original Image")
        st.image(image_np, use_column_width=True)

    with col2:
        st.subheader("🧠 Detected Objects")
        st.image(annotated_rgb, use_column_width=True)

        boxes = results[0].boxes
        class_ids = boxes.cls.tolist()
        count = len(class_ids)
        st.success(f"✅ Total Objects Detected: {count}")

        if count > 0:
            names = [model.names[int(cls_id)] for cls_id in class_ids]
            labels_count = {name: names.count(name) for name in set(names)}
            st.info("📦 Detected Classes:")
            for label, freq in labels_count.items():
                st.write(f"- **{label.capitalize()}**: {freq}x")

# -------------------------
# Video Logic
# -------------------------
elif uploaded_video:
    st.subheader("🎬 Processing Video...")

    # Save uploaded video to a temporary file
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tfile.write(uploaded_video.read())
    video_path = tfile.name

    cap = cv2.VideoCapture(video_path)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = int(cap.get(cv2.CAP_PROP_FPS))

    # Output video path (save to the current directory)
    output_dir = os.getcwd()  # Current directory
    output_path = os.path.join(output_dir, "output_detected.mp4")
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    with st.spinner("Detecting objects in video..."):
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame, conf=confidence)
            annotated_frame = results[0].plot()
            out.write(annotated_frame)

        cap.release()
        out.release()

    st.success("✅ Video processed successfully!")
    st.subheader("🎥 Output Video with Detections")

    # Display the processed video
    st.video(output_path)


