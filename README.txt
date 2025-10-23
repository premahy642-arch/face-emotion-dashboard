# Face Emotion Age Dashboard 🎯

A real-time AI dashboard that detects faces, predicts age and gender, assigns emotion labels, and logs all detections to CSV — built without TensorFlow for lightweight deployment.

## 🚀 Features

- ✅ Real-time face detection using OpenCV
- ✅ Age and gender prediction using Caffe models
- ✅ Emotion labeling via mock classifier (customizable)
- ✅ Manual gender override (`m`, `f`, `r` keys)
- ✅ Confidence filtering for gender predictions
- ✅ Voice alerts using pyttsx3
- ✅ Snapshot saving every 5 seconds
- ✅ CSV logging with timestamp, age, gender, confidence, emotion

## 📁 Folder Structure

face emotion age dashboard/ ├── models/ │ ├── haarcascade_frontalface_default.xml │ ├── deploy_age.prototxt │ ├── age_net.caffemodel │ ├── deploy_gender.prototxt │ ├── gender_net.caffemodel ├── snapshots/ ← auto-created ├── src/ │ └── faceDashboard.py ← main dashboard code ├── main.py ├── face_log.csv ← auto-generated log file ├── README.md

Code

## 🧠 Keyboard Controls

- `m` → Force gender to Male  
- `f` → Force gender to Female  
- `r` → Reset to auto prediction  
- `q` → Quit the dashboard

## 📦 Requirements

Install dependencies:
```bash
pip install opencv-python pyttsx3 numpy
▶️ How to Run
bash
python main.py
📊 CSV Logging
Each detection is saved to face_log.csv with:

Timestamp

Age

Gender (predicted or overridden)

Confidence

Emotion

🎓 Viva Notes
This dashboard is designed for academic presentation:

Modular and error-free

No TensorFlow dependency

Manual override and confidence filtering

Logs and snapshots for analysis

📌 Future Upgrades
Real emotion detection via PyTorch or ONNX

Gallery viewer for snapshots

Web hosting for demo

Auto-generated viva slides

Built and refined by Prema 💡

Code
---
Once you paste this into your `README.md`, run:
```bash
git add README.md
git commit -m "Add final README with features and viva notes"
git push

---


