import cv2
import os

# 설정
base_dir = './faces/'
target_cnt = 200
cnt = 0

# 사용자 입력
name = input("Insert Object Name (ex: bag): ")
id = input("Insert Object ID (ex: 1): ")
dir = os.path.join(base_dir, name + '_' + id)
if not os.path.exists(dir):
    os.makedirs(dir)

# Haar cascade 로드
cascade_path = '../data/bag_cascade.xml'  
object_cascade = cv2.CascadeClassifier(cascade_path)

# 카메라 시작
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects = object_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in objects:
        obj_crop = frame[y:y+h, x:x+w]
        obj_resize = cv2.resize(obj_crop, (200, 200))

        file_name_path = os.path.join(dir, str(cnt) + '.jpg')
        cv2.imwrite(file_name_path, obj_resize)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, str(cnt), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cnt += 1
        if cnt >= target_cnt:
            break

    cv2.imshow('object record', frame)

    if cv2.waitKey(1) == 27 or cnt >= target_cnt:  # ESC 눌러도 종료
        break

cap.release()
cv2.destroyAllWindows()
print("Collecting Samples Completed.")
