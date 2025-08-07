import cv2

# 얼굴 검출기 불러오기 (경로는 파일 위치에 맞게 수정)
face_cascade = cv2.CascadeClassifier('../data/haarcascade_frontalface_default.xml')

# 모자이크 비율
rate = 10

# 캠 열기 (0번은 기본 웹캠)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    pass
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 얼굴 검출: grayscale 변환 필요
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(60, 60)
    )

    # 얼굴마다 모자이크 처리
    for (x, y, w, h) in faces:
        # 얼굴 영역 자르기
        roi = frame[y:y+h, x:x+w]

        # 작게 줄였다가 다시 키워서 모자이크 효과
        small = cv2.resize(roi, (w // rate, h // rate))
        mosaic = cv2.resize(small, (w, h), interpolation=cv2.INTER_AREA)

        # 원본 프레임에 덮어쓰기
        frame[y:y+h, x:x+w] = mosaic

    # 화면에 출력
    cv2.imshow('Face Mosaic', frame)

    # ESC 누르면 종료 (키코드 27)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
