# Air Canvas using OpenCV & MediaPipe

A simple computer vision project that allows you to **draw in the air using your index finger** detected through a webcam.

The system tracks hand landmarks using MediaPipe and converts the **index finger movement into drawing strokes** on a virtual canvas.

---

## 🚀 Features

* Real-time **hand tracking**
* Draw using **index finger movement**
* **Air drawing canvas**
* Clear canvas with keyboard shortcut
* Smooth drawing using frame tracking

---

## 🧠 How It Works

1. Webcam captures live video frames.
2. MediaPipe detects the **hand landmarks (21 points)**.
3. The program tracks the **index finger tip (landmark 8)**.
4. When the index finger is raised, the system draws lines following the finger movement.
5. The drawing is displayed on a virtual canvas over the webcam feed.

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

---

## 📂 Project Structure

```
Aircanvasproject/
│
├── main.py            # Main application logic
├── hand_tracker.py    # Hand detection and landmark tracking
├── canvas_utils.py    # Drawing utilities
├── requirements.txt   # Project dependencies
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/GouravK1107/air-canvas-project.git
```

Move into the project folder:

```
cd air-canvas-project
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the main program:

```
python main.py
```

---

## 🎮 Controls

| Key   | Function                  |
| ----- | ------------------------- |
| **Q** | Quit the application      |
| **C** | Clear the canvas          |
| **S** | Save the current drawing  |
| **E** | Enable eraser mode        |
| **B** | Switch back to brush mode |
| **+** | Increase brush size       |
| **-** | Decrease brush size       |

### ✋ Gesture Controls

* **Index finger up** → Draw on the canvas
* **Two fingers up** → Stop drawing
* **Touch the top toolbar with your finger** → Change drawing color

---

## 📸 Demo

The program opens the webcam and allows users to **draw in the air using finger gestures**.

---

## 💡 Future Improvements

* Gesture-based **color selection**
* **Eraser mode**
* Save drawing as **image**
* Multi-hand gesture support

---

## Implemented Improvements

* Real-time hand tracking with MediaPipe
* Gesture-based drawing using index finger
* Smooth stroke rendering
* Gesture color selection
* Eraser mode
* Save drawing as image
* Multi-hand support

## 👨‍💻 Author

**Gourav K**

GitHub:
https://github.com/GouravK1107

---

## ⭐ If you like this project

Give it a **star ⭐ on GitHub**!
