import cv2
import mediapipe as mp
import time


mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

# cap = cv2.VideoCapture(0) # To use webcam
cap = cv2.VideoCapture("resources/front-0.mov") # path to video file 
# cap = cv2.VideoCapture("resources/side-0.mov") # path to video file 

# spf = 0.01669727834 #segundos 

fps = 59.89 # f/s => s/f 
spf = 1/fps
t = 0

t_array = []


while True:
    t_array.append(t)

    print(f"t(s) = {t}")
    t = t + spf
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pose.process(img_rgb)

    if result.pose_landmarks:
        mp_draw.draw_landmarks(img, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        # print(f'x={result.pose_landmarks.landmark[24].x}')
        for id, lm in enumerate(result.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# ,tiempo,posicion,vm
# 0,0,0,0.0
# 1,1,2,2.0
# ...
#  .csv