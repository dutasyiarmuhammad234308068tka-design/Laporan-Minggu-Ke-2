import cv2 #library open cv untuk akses kamera, pengolahan gambar, dan tampilan video
import mediapipe as mp # library computer vision untukdeteksi pose, tangan, wajah, dll
mpose =mp.solutions.pose # shortcut modul pose dari mediapipe
pose = mpose.Pose() # mengaktifkan model deteksi pose tubuh
mdraw =mp.solutions.drawing_utils # utility untuk menggambar titik landmark tubuh
cap = cv2.VideoCapture(0) # mengaktifkan kamera pc

while True:
    success, img = cap.read()
    if not success:
        break
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = pose.process(imgrgb)
# Proses deteksi
    if hasil.pose_landmarks:
        mdraw.draw_landmarks(img, hasil.pose_landmarks, mpose.POSE_CONNECTIONS) # Skleton Tubuh
        lm = hasil.pose_landmarks.landmark

        left_shoulder =lm[mpose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder =lm[mpose.PoseLandmark.RIGHT_SHOULDER]
        left_wrist =lm[mpose.PoseLandmark.LEFT_WRIST]
        right_wrist =lm[mpose.PoseLandmark.RIGHT_WRIST]
# Deteksi tangan terangkat
        left_hand_up = left_wrist.y < left_shoulder.y
        right_hand_up = right_wrist.y < right_shoulder.y
        status = "Tidak Ada Tangan Terangkat"
        if left_hand_up and right_hand_up:
            status = "Dua Tangan Terangkat"
        elif left_hand_up:
            status = "Tangaan Kiri Terangkat"
        elif right_hand_up:
            status = "Tangan Kanan Terangkat"
        cv2.putText(img, status, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        for id, lm in enumerate (hasil.pose_landmarks.landmark):
            print(id, lm.x, lm.y)
    cv2.imshow("webcam", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

