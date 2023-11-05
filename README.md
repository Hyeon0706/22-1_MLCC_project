# 22-1_MLCC_project

## 기술 스택

![1](https://github.com/Hyeon0706/imageRepository/assets/83438780/1a456260-5a84-4087-8433-fc02b477ae10)

- Python
- OpenCV
- Tensorflow

## 핵심 기능

- 크기를 측정하여 검사
  - 정상 제품의 평균 크기에서 크게 벗어나면 불량 판정
- 밝기를 측정하여 검사
  - 평균치보다 밝기가 높거나 낮은곳을 측정하여 불량 판정
- AI를 활용하여 검사
  - 학습된 모델을 사용하여 AI가 불량 판정

![2](https://github.com/Hyeon0706/imageRepository/assets/83438780/249499bd-df7c-4e28-a7db-2c79abd167d4)

![3](https://github.com/Hyeon0706/imageRepository/assets/83438780/e75a8356-a77c-4984-a5fa-e19085050641)

![4](https://github.com/Hyeon0706/imageRepository/assets/83438780/eb2db6f4-bdbd-4610-967c-96e2c71cb974)

![5](https://github.com/Hyeon0706/imageRepository/assets/83438780/120486ee-7b77-4ca7-8c14-90a279b175be)

![6](https://github.com/Hyeon0706/imageRepository/assets/83438780/c00fe74e-56c3-46bf-a821-fc5c791cbc78)

![7](https://github.com/Hyeon0706/imageRepository/assets/83438780/cc913752-4022-471f-81f5-ccc376d3f7ec)

![8](https://github.com/Hyeon0706/imageRepository/assets/83438780/7ba04caa-7e1f-4d12-be9f-71d12e590849)

![9](https://github.com/Hyeon0706/imageRepository/assets/83438780/b3894bdd-b567-4677-b0f6-e74cadd6acdd)

![11](https://github.com/Hyeon0706/imageRepository/assets/83438780/04397bab-40cc-4a13-b31f-adeda1f78285)

![12](https://github.com/Hyeon0706/imageRepository/assets/83438780/baca54cf-4dd7-4cce-aac1-1f8e41d19937)

## 구현 방법

### 공통 기능

- 모든 방법은 공통으로 전처리 한 이미지를 사용하기 때문에 GrayScale로 전환

![13](https://github.com/Hyeon0706/imageRepository/assets/83438780/a5627644-1a31-4c45-8e4c-64a2970435ec)

### 크기 검사

1. GrayScale한 이미지를 2번의 이진화를 통해 MLCC 전체와 전극을 구분

![14](https://github.com/Hyeon0706/imageRepository/assets/83438780/e889f2d4-3569-4b1e-a550-cf892cab5ba0)

1. 구분 된 이미지에서 MLCC 전체와 전극을 감싸는 최소 크기의 사각형 생성

![15](https://github.com/Hyeon0706/imageRepository/assets/83438780/76682162-cda9-459a-8795-395d4fd7928d)

1. 미리 측정된 정상 제품들의 평균값, 최소값, 최대값을 이용하여 임계값을 설정하고, 임계값을 넘기거나, 작을경우 불량으로 판정

![16](https://github.com/Hyeon0706/imageRepository/assets/83438780/9eb3619b-1bf6-460f-bac6-171a5c4f67b5)

### 밝기 검사

1. MLCC를 양쪽 전극, 바디 부분으로 나누기 위해 윤곽선 검출한 후 이미지를 3개로 분리

![17](https://github.com/Hyeon0706/imageRepository/assets/83438780/224a36a7-899f-4929-bdc5-7d164d17ffb5)

![18](https://github.com/Hyeon0706/imageRepository/assets/83438780/09d12ff9-da3c-4c7c-b465-d2493f5e79c8)

1. 특이점이 존재하면 불량으로 판단

![19](https://github.com/Hyeon0706/imageRepository/assets/83438780/3b5e2d7e-4a07-49e6-b55f-71e3b5309e97)

![20](https://github.com/Hyeon0706/imageRepository/assets/83438780/00ba38a9-0121-4123-8ea7-c046fdd2ef29)

### AI 검사

- Tensorflow 활용
- 정상 제품 데이터 480장, 불량 제품 데이터 236장 학습

1. 기존의 받은 데이터의 양이 적어 Data Augmentation 과정을 거침

![21](https://github.com/Hyeon0706/imageRepository/assets/83438780/3faa7493-2b7a-4ac9-ab58-caf21a8defec)

![22](https://github.com/Hyeon0706/imageRepository/assets/83438780/502f38cf-f842-47f9-a303-d462f587e9b0)

## 결과

- 다음과 같이 불량이 확실한 이미지에 대해서는 불량 판별이 정확

![23](https://github.com/Hyeon0706/imageRepository/assets/83438780/3e01a1b0-017c-4cd8-8aea-ef48db646529)

- 하지만 아래의 불량 이미지는 회사측에서 불량이라 판별한 이미지지만, 불량 제품 이미지와 정상제품 이미지의 차이가 거의 없어 밝기 측정과 크기 측정에서는 검출에 어려움이 있음

![24](https://github.com/Hyeon0706/imageRepository/assets/83438780/76c08971-8ed2-424f-93cd-981d8ad99dce)

- 이후 AI 를 적용 후 재실험 해본 결과 불량제품 검출 정확도가 상승한 것을 확인할 수 있다.

![25](https://github.com/Hyeon0706/imageRepository/assets/83438780/d4428584-a1fe-4e73-bcdb-e2cc4c6f33d2)

AI 미사용

![26](https://github.com/Hyeon0706/imageRepository/assets/83438780/abbc3f5b-5eda-4548-aa04-f5c30e48bc17)

AI 사용
