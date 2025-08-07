# ear_calculator.py

from scipy.spatial import distance as dist

def calculate_ear(eye):
    """
    eye: 눈의 6개 랜드마크 좌표 리스트 [(x1, y1), ..., (x6, y6)]
    EAR(Eye Aspect Ratio) 계산
    """
    # 수직 거리 2개
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # 수평 거리 1개
    C = dist.euclidean(eye[0], eye[3])

    ear = (A + B) / (2.0 * C)
    return ear
