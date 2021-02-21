# 원본 이미지 파일 읽어오기

# 외부 모듈 읽어오기
import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image                    # 이미지 처리를 하기 위한 외부 이미지

# image file 읽어오기
imgBG = Image.open("lake.jpg")            # 배경 이미지 열기
imgFG1 = Image.open("lena.png")               # 사진 이미지1  열기
imgFG2 = Image.open("mandrill.png")           # 사진 이미지2  열기

imgFG2 = imgFG2.convert('RGB')

pix1 = np.array(imgBG)                        # image data를 numpy array로 구성

# 사진을 이어붙이기 위해 배경에 맞추어 변경할 크기 계산하기
# 만약 배경 화면의 가로 크기가 홀수이면 첫번째 이미지의 가로 크기를 반올림하기
resize1 = resize2 = pix1.shape[1]//2          # 홀수인지 체크
if (pix1.shape[1] % 2 > 0) :                  # 홀수인 경우
    resize1 += 1

# 사진 2장을 나란히 붙이기 위해 배경 이미지의 절반씩 차지하도록 크기 변경하기
imgFG1 = imgFG1.resize((resize1, pix1.shape[0]))     # 첫번째 사진 크기 변경
pix2 = np.array(imgFG1)

imgFG2 = imgFG2.resize((resize2, pix1.shape[0]))     # 두번째 사진 크기 변경
pix3 = np.array(imgFG2)

# 사진 2개를 옆으로 나란히 붙이기(axis값을 0으로 하면 세로로 설정됨.)
pix4 = np.concatenate((pix2, pix3), axis = 1)             # 두 사진을 가로 방향으로 붙이기

# 이미지를 블렌딩하기 위해 각 픽셀의 RGB 값을 (0~1)의 실수 범위로 정규화(normalize)
pix1 = (1/255)*pix1
pix4 = (1/255)*pix4 

weight = 0.7                                           # 가중치 정하기
pix5 = pix4 * weight + pix1 * (1-weight)
# 가중치를 적용하기 위해 원본 이미지 행렬에 가중치를 실수배하여 합하기

pix5 = pix5*255
out = Image.fromarray(pix5.astype(np.uint8))
out.save("Blended70.png")

plt.show()

