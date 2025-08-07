# eye_tracker.py
import cv2
import dlib
from imutils import face_utils
from ear_calculator import calculate_ear  # ← 우리가 만든 모듈 사용

# 얼굴 탐지기와 랜드마크 예측기 불러오기
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")  # 모델 파일 필요

# EAR 계산 시 사용할 눈 인덱스 (왼쪽, 오른쪽 눈)
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# 캠 열기
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        # 왼쪽, 오른쪽 눈 좌표
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        # EAR 계산
        leftEAR = calculate_ear(leftEye)
        rightEAR = calculate_ear(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        # EAR 값을 시각화
        cv2.putText(frame, f"EAR: {ear:.2f}", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # 눈 윤곽 그리기
        for (x, y) in leftEye:
            cv2.circle(frame, (x, y), 2, (0, 255, 255), -1)
        for (x, y) in rightEye:
            cv2.circle(frame, (x, y), 2, (0, 255, 255), -1)

    cv2.imshow("Eye Tracker", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
