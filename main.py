import cv2
import numpy as np
from hand_tracker import HandTracker
from canvas_utils import draw_line, clear_canvas

cap = cv2.VideoCapture(0)
tracker = HandTracker()
canvas = None
prev_x, prev_y = None, None


while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if canvas is None:
        canvas = np.zeros_like(frame)

    frame, landmarks = tracker.find_hands(frame)

    if landmarks:
        index_x, index_y = None, None
        index_pip_y = None

        for point in landmarks:
            id, x, y = point
            if id == 8:  # index finger tip
                index_x = x
                index_y = y
            if id == 6:  # index finger joint
                index_pip_y = y

        if index_y is not None and index_pip_y is not None:
            if index_y < index_pip_y:
                if prev_x is None and prev_y is None:
                    prev_x, prev_y = index_x, index_y

                canvas = draw_line(
                    canvas,
                    (prev_x, prev_y),
                    (index_x, index_y)
                )
                prev_x, prev_y = index_x, index_y
            else:
                prev_x, prev_y = None, None
    else:
        prev_x, prev_y = None, None

    combined = cv2.add(frame, canvas)
    cv2.imshow("Air Canvas", combined)
    key = cv2.waitKey(1)
    if key == ord('c'):
        canvas = clear_canvas(canvas)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()