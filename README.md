# Real-Time Face Mesh Using MediaPipe & OpenCV

## 📌 Overview
This project implements a real-time face mesh detection using MediaPipe and OpenCV. It captures video from a webcam, processes face landmarks, and visualizes the face mesh on a black background.

## 🚀 Features
Detects 468 facial landmarks using MediaPipe.
Displays real-time face mesh overlay on a black background.
Works efficiently with real-time video feed.
Uses OpenCV for image processing and visualization.
🛠 Requirements
Ensure you have the following dependencies installed:

``` bash

pip install opencv-python mediapipe imutils numpy
```

📜 Usage
1️⃣ Clone the Repository
```bash
Edit
git clone https://github.com/alirzx/Realtime-Facemesh-Using-mediapipe.git
```
2️⃣ Run the Script
```bash
python face_mesh.py
```

3️⃣ Controls
Press X to exit the program.

## 📷 How It Works
Captures frames from the webcam using OpenCV.
Converts the image to RGB and processes it using MediaPipe FaceMesh.
Draws 468 facial landmarks using MediaPipe drawing utilities.
Displays the face mesh on a black background.

## 📌 Example Output
![realtime output](https://github.com/alirzx/Realtime-Facemesh-Using-mediapipe/blob/main/output.png?raw=true)


## 🔧 Code Explanation
### cv2.VideoCapture(0) → Captures video from the webcam.
### cv2.flip(image, 1) → Flips the image horizontally.
### mp_face_mesh.FaceMesh() → Detects face mesh landmarks.
### mp_drawing.draw_landmarks() → Draws the facial landmarks.
### cv2.imshow() → Displays the original and processed images.

## 📝 Future Improvements
### ✅ Add eye tracking
### ✅ Implement emotion detection
### ✅ Improve performance with multi-threading

🤝 Contributing
Feel free to fork this repository, create a new branch, and submit a pull request with improvements! 😊
