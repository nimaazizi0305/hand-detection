import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
Hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while True:
    success,frame = cap.read()

    conveted_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = Hands.process(conveted_frame)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame,handlms,mpHands.HAND_CONNECTIONS)

    cv2.imshow("hand tracking", frame)

    if cv2.waitKey(1) == ord('q'):
        break