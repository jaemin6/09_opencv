# drowsiness_detector.py

from ear_calculator import calculate_ear

# 졸음 감지에 사용할 임계값과 프레임 수 설정
EAR_THRESHOLD = 0.25    # EAR이 이 값보다 작으면 눈 감은 것으로 판단
CONSEC_FRAMES = 20      # 이만큼 연속으로 EAR이 낮아야 졸음으로 판단

# 졸음 감지를 위한 상태 변수
counter = 0      # EAR이 연속으로 낮은 프레임 수
alarm_on = False

def detect_drowsiness(left_eye, right_eye):
    """
    좌우 눈 랜드마크를 받아서 EAR 계산 후 졸음 여부 판단
    졸음이면 True, 아니면 False 반환
    """
    global counter, alarm_on

    # EAR 계산
    left_ear = calculate_ear(left_eye)
    right_ear = calculate_ear(right_eye)
    ear = (left_ear + right_ear) / 2.0

    if ear < EAR_THRESHOLD:
        counter += 1

        if counter >= CONSEC_FRAMES:
            alarm_on = True
            return True, ear
    else:
        counter = 0
        alarm_on = False

    return False, ear
