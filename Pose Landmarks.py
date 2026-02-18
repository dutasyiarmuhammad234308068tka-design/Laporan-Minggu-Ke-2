import cv2
import mediapipe as mp
mpose =mp.solutions.pose
pose = mpose.Pose()
mdraw =mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgrgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = pose.process(imgrgb)

    if hasil.pose_landmarks:
        mdraw.draw_landmarks(img, hasil.pose_landmarks, mpose.POSE_CONNECTIONS)
        for id, lm in enumerate(hasil.pose_landmarks.landmark):
            print(id, lm.x, lm.y)
    cv2.imshow("webcam",img)
    cv2.waitKey(10)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

