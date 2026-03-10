import cv2
import mediapipe as mp

class HandTracker:

    def __init__(self, detection_conf=0.7, track_conf=0.7):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=detection_conf,
            min_tracking_confidence=track_conf
        )
        self.mp_draw = mp.solutions.drawing_utils


    def find_hands(self, frame):

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        landmarks_points_list = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, _ = frame.shape
                    cx = int(lm.x * w)
                    cy = int(lm.y * h)
                    landmarks_points_list.append((id, cx, cy))

                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

        return frame, landmarks_points_list