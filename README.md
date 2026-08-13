# ✋ Air Canvas — Draw in the Air using OpenCV & MediaPipe

A computer vision project that lets you **draw in thin air** using just your index finger, tracked live through your webcam. MediaPipe detects hand landmarks in real time and converts index-finger movement into smooth drawing strokes on a virtual canvas overlaid on the camera feed.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?style=for-the-badge&logo=google&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

---

## 🚀 Features

- ✋ Real-time hand tracking (21 landmark points via MediaPipe)
- ✏️ Draw using index-finger movement
- 🎨 Gesture-based color selection — touch the on-screen toolbar to switch colors
- 🧽 Eraser mode, toggle back to brush anytime
- 📏 Adjustable brush size (increase/decrease on the fly)
- 💾 Save your drawing as an image
- 👐 Multi-hand support
- 🧼 Clear the entire canvas with a single keypress
- 🎬 Smooth stroke rendering via frame-by-frame tracking

---

## 🧠 How It Works

1. The webcam captures live video frames
2. MediaPipe detects hand landmarks (21 points per hand)
3. The program tracks the **index finger tip** (landmark 8)
4. When the index finger is raised, the system draws lines following its movement
5. The drawing renders on a virtual canvas layered over the live webcam feed

---

## 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy

---

## 📂 Project Structure

```
air-canvas-project/
│
├── main.py             # Main application logic
├── hand_tracker.py     # Hand detection and landmark tracking
├── canvas_utils.py     # Drawing utilities
├── requirements.txt    # Project dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

**Clone the repository**
```
git clone https://github.com/GouravK1107/air-canvas-project.git
cd air-canvas-project
```

**Install dependencies**
```
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```
python main.py
```

---

## 🎮 Controls

| Key | Function |
|---|---|
| **Q** | Quit the application |
| **C** | Clear the canvas |
| **S** | Save the current drawing |
| **E** | Enable eraser mode |
| **B** | Switch back to brush mode |
| **+** | Increase brush size |
| **-** | Decrease brush size |

### 🖐️ Gesture Controls

- **Index finger up** → Draw on the canvas
- **Two fingers up** → Stop drawing
- **Touch the top toolbar with your finger** → Change drawing color

---

## 📸 Demo

Run the program, let it access your webcam, and start drawing in the air with your index finger — the canvas layers live on top of your camera feed in real time.

---

## 💡 Future Improvements

- 🔺 Shape recognition (auto-detect circles, lines, rectangles from strokes)
- 🖼️ Export drawings as a timelapse/GIF of the drawing process
- 🌐 Web-based version using MediaPipe's JS runtime
- 🤝 Collaborative multi-user air-drawing over a shared canvas
- 🎯 Gesture-based undo/redo

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.
Fork → create a branch → commit → push → open a pull request.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

## 👨‍💻 Author

**Gourav R**
Backend Developer | Applied AI Developer — exploring Computer Vision & AI systems

GitHub: https://github.com/GouravK1107
Portfolio: https://gouravk1107.github.io/my-portfolio/

---

Made with ❤️ and a lot of finger-waving.
