import cv2
import dlib
from imutils import face_utils
from ear_calculator import calculate_ear

# dlib 얼굴 탐지기와 랜드마크 예측기 로드
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# 웹캠 열기
cap = cv2.VideoCapture(0)

# imutils를 이용해 눈 랜드마크 인덱스 가져오기
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        # 랜드마크 예측 및 numpy 배열로 변환
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        # 눈 랜드마크 좌표 추출
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        # EAR 계산
        leftEAR = calculate_ear(leftEye)
        rightEAR = calculate_ear(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        # EAR 값 화면에 표시
        cv2.putText(frame, f"EAR: {ear:.2f}", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
    cv2.imshow("EAR Visualization", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()