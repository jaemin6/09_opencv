# 💤 졸음 운전 감지 시스템 (Drowsiness Detection System)

졸음 운전은 매우 위험하며, 이를 예방하기 위한 **실시간 EAR(Eye Aspect Ratio) 기반 감지 시스템**을 구현한 프로젝트입니다.  
본 프로젝트는 `face_mesh` 기반 얼굴 랜드마크 검출 → 눈 감김 비율(EAR) 계산 → 시각화 및 경고음 재생의 흐름으로 구성됩니다.

---

## 📁 프로젝트 구조

opencv_tutorial/
└── 09_opencv/
├── src/
│ ├── calculate_and_plot_ear.py # EAR 계산 및 실시간 시각화
│ ├── face_landmark_utils.py # 얼굴 랜드마크, EAR 유틸 함수 모음
│ ├── alert_manager.py # 경고음, EAR 상태 관리 모듈
│ └── assets/
│ └── alert.wav # 경고음 사운드 파일
└── README.md # 프로젝트 설명서 (← 이 문서)

yaml
복사
편집

---

## ✅ 설치 및 실행 환경

- Python >= 3.8
- OpenCV
- MediaPipe
- NumPy
- SciPy
- Playsound (사운드 재생용)

```bash
pip install opencv-python mediapipe numpy scipy playsound
🧠 주요 기능 설명
1. 얼굴 랜드마크 검출 - face_landmark_utils.py
Mediapipe FaceMesh를 통해 눈 영역의 6개 랜드마크를 검출합니다.

EAR (Eye Aspect Ratio)를 계산하는 함수도 포함되어 있습니다.

python
복사
편집
from face_landmark_utils import get_eye_landmarks, calculate_ear
EAR 공식

EAR = \frac{‖p_2 - p_6‖ + ‖p_3 - p_5‖}{2 × ‖p_1 - p_4‖}
]

2. EAR 시각화 및 출력 - calculate_and_plot_ear.py
실시간 웹캠을 통해 눈 깜빡임과 감김 상태를 시각적으로 확인할 수 있습니다.

EAR 값을 그래프처럼 실시간으로 출력합니다.

경고 기준은 EAR < 0.2일 때입니다.

3. 경고음 시스템 - alert_manager.py
EAR가 일정 시간 이상 낮게 유지되면, 경고음을 재생합니다.

이전 EAR 값과 비교하여 졸음 상태를 판별하는 기능이 있습니다.

python
복사
편집
from alert_manager import EARManager
🖼️ 동작 화면 예시
👁️ 얼굴과 눈 랜드마크
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Face_Mesh.png/600px-Face_Mesh.png" width="400" />
📊 EAR 그래프 예시
(그래프 구현 예정 또는 Matplotlib 응용 가능)

⚠️ 경고 시스템 동작 원리
EAR가 0.2 이하로 떨어진 경우 → 잠재적 졸음으로 판단

EARManager 클래스가 EAR 값의 변화를 누적 관찰하고 alert.wav를 재생합니다.

해당 로직은 alert_manager.py에 정의되어 있습니다.

💡 향후 확장 아이디어
EAR 그래프 저장 및 분석 기능

졸음 감지시 차량 정지 기능 연동 (IoT)

Yawning(하품), 고개 떨굼까지 감지 확대

GUI 인터페이스 도입 (Tkinter or PyQt)

🎯 실행 방법
bash
복사
편집
# 프로젝트 폴더 이동
cd opencv_tutorial/09_opencv/src

# 실행
python calculate_and_plot_ear.py
🔊 경고음 예시
assets/alert.wav 파일은 기본 내장된 경고음입니다.

원하는 경고음으로 교체 가능합니다.

🙋‍♀️ 도움말 및 오류 해결
ImportError: cannot import name 'calculate_ear'
→ face_landmark_utils.py 내부에 calculate_ear() 함수가 존재하는지 확인

playsound 관련 오류 발생 시, 시스템에 적절한 오디오 드라이버 설치 필요

✍️ 참고 자료
MediaPipe FaceMesh 공식 문서

Tereza Soukupova & Jan Cech - Real-Time Eye Blink Detection

📌 제작자 코멘트
이 프로젝트는 졸음운전과 같은 생명을 위협하는 상황을 방지하는 데 도움을 주고자 제작되었습니다.
학습용/프로토타입으로 구현되었으며, 실제 제품 적용 전 충분한 테스트와 인증이 필요합니다.
