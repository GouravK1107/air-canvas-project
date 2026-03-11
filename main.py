import cv2
import numpy as np
import mediapipe as mp
import time
import os

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# Canvas
canvas = np.zeros((480,640,3),dtype=np.uint8)

# Drawing settings
draw_color = (255,0,0)
brush_thickness = 6
eraser_thickness = 40
eraser_mode = False

# Previous coordinates for smooth drawing
prev_x, prev_y = 0,0

# Create output folder
os.makedirs("outputs",exist_ok=True)

cap = cv2.VideoCapture(0)


def draw_toolbar(frame):

    cv2.rectangle(frame,(0,0),(640,65),(40,40,40),-1)

    cv2.rectangle(frame,(40,10),(100,60),(255,0,0),-1)
    cv2.rectangle(frame,(120,10),(180,60),(0,255,0),-1)
    cv2.rectangle(frame,(200,10),(260,60),(0,0,255),-1)
    cv2.rectangle(frame,(280,10),(340,60),(0,255,255),-1)
    cv2.rectangle(frame,(360,10),(420,60),(255,255,255),-1)

    cv2.putText(frame,"Press E = Eraser",(440,40),
                cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)


def get_color(x,y):

    if y <= 65:

        if 40 < x < 100:
            return (255,0,0)

        elif 120 < x < 180:
            return (0,255,0)

        elif 200 < x < 260:
            return (0,0,255)

        elif 280 < x < 340:
            return (0,255,255)

        elif 360 < x < 420:
            return (255,255,255)

    return None


while True:

    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame,1)

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    draw_toolbar(frame)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            h,w,c = frame.shape

            x = int(hand_landmarks.landmark[8].x * w)
            y = int(hand_landmarks.landmark[8].y * h)

            cv2.circle(frame,(x,y),8,(255,255,255),-1)

            # finger states
            index_up = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
            middle_up = hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y

            selected_color = get_color(x,y)

            if selected_color is not None:
                draw_color = selected_color
                eraser_mode = False

            elif index_up and not middle_up:

                if prev_x == 0 and prev_y == 0:
                    prev_x,prev_y = x,y

                if eraser_mode:

                    cv2.circle(frame,(x,y),eraser_thickness,(255,255,255),2)

                    cv2.line(canvas,
                             (prev_x,prev_y),
                             (x,y),
                             (0,0,0),
                             eraser_thickness)

                else:

                    cv2.line(canvas,
                             (prev_x,prev_y),
                             (x,y),
                             draw_color,
                             brush_thickness)

                prev_x,prev_y = x,y

            else:

                prev_x,prev_y = 0,0

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    # Merge canvas and frame
    frame = cv2.addWeighted(frame,1,canvas,1,0)

    if eraser_mode:
        cv2.putText(frame,"ERASER MODE",(450,100),
                    cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    cv2.imshow("Air Canvas",frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    if key == ord('c'):
        canvas[:] = 0

    if key == ord('e'):
        eraser_mode = not eraser_mode

    if key == ord('s'):

        filename = f"outputs/drawing_{int(time.time())}.png"

        cv2.imwrite(filename,canvas)

        print("Saved:",filename)


cap.release()
cv2.destroyAllWindows()