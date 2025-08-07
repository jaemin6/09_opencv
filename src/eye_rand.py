import cv2
import dlib
import numpy as np

# 설정
LEFT_EYE_IDX = list(range(36, 42))   # 왼쪽 눈
RIGHT_EYE_IDX = list(range(42, 48))  # 오른쪽 눈

# 얼굴 검출기 및 랜드마크 예측기 로드
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

# 웹캠 열기
cap = cv2.VideoCapture(0)

def get_eye_region(shape, eye_indices):
    points = [(shape.part(i).x, shape.part(i).y) for i in eye_indices]
    return np.array(points, dtype=np.int32)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        shape = predictor(gray, face)

        # 눈 좌표 가져오기
        left_eye = get_eye_region(shape, LEFT_EYE_IDX)
        right_eye = get_eye_region(shape, RIGHT_EYE_IDX)

        # 눈 윤곽 그리기
        cv2.polylines(frame, [left_eye], True, (0, 255, 255), 1)
        cv2.polylines(frame, [right_eye], True, (0, 255, 255), 1)

        # 중심점 계산
        left_center = np.mean(left_eye, axis=0).astype(int)
        right_center = np.mean(right_eye, axis=0).astype(int)

        # 중심점 표시
        cv2.circle(frame, tuple(left_center), 3, (0, 255, 0), -1)
        cv2.circle(frame, tuple(right_center), 3, (0, 255, 0), -1)

        # 눈 바운딩 박스 그리기
        lx, ly, lw, lh = cv2.boundingRect(left_eye)
        rx, ry, rw, rh = cv2.boundingRect(right_eye)
        cv2.rectangle(frame, (lx, ly), (lx+lw, ly+lh), (255, 0, 0), 1)
        cv2.rectangle(frame, (rx, ry), (rx+rw, ry+rh), (255, 0, 0), 1)

    cv2.imshow("Step2 - Eye Detection", frame)

    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
