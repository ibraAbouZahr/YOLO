# 🔍 YOLOv8 Object Detection Web App

A real-time object detection web application using **YOLOv8** (by Ultralytics), powered by **Streamlit**. Detect objects in images and videos with an adjustable confidence threshold and visually see the results instantly!

![Demo](https://via.placeholder.com/800x400?text=Demo+GIF+Placeholder) <!-- Replace with actual demo GIF -->

---

## ✨ Features

- Upload images or videos for object detection
- Choose a confidence threshold using a slider
- View original vs detected visuals side by side
- Download and preview annotated video outputs
- Powered by [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) and [Streamlit](https://streamlit.io)

---

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/yolov8-streamlit-app.git
   cd yolov8-streamlit-app
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. **Run the app**

   ```bash
   streamlit run app.py
   ```

2. Open in browser: Streamlit will provide a local URL (e.g., `http://localhost:8501`)

3. Upload an image or video and watch the detection magic happen!

---

## 📁 File Structure

```bash
📦 yolov8-streamlit-app
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── output_detected.mp4     # Output video (generated after processing)
```

---

## ⚙️ Requirements

- Python 3.8+
- Streamlit
- OpenCV
- PIL
- NumPy
- Ultralytics (YOLOv8)

_All are listed in requirements.txt_

---

## 🌐 Deployment

### Streamlit Cloud

1. Create a free account on [Streamlit Cloud](https://streamlit.io/cloud)
2. Connect your GitHub repository
3. Deploy! The app will be automatically deployed and publicly accessible

---

## 👥 Authors

- **Ibrahim Abou Zahr** - [LinkedIn](https://www.linkedin.com/in/ibrahim-abouzahr-dev/)
- **Mohamad Mawed** - [LinkedIn](https://www.linkedin.com/in/mohamad-el-mawed-dev/)

---

## 📜 License

MIT License - feel free to use, modify, and distribute this project.

```

```
