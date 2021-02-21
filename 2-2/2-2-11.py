import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("parrots.png")
pix = np.array(img)
print(pix.shape)

# pix array에서 각각 R(0), G(1), B(2) 성분 값 외에는 0으로 만들어서
# 원본 이미지에서 R, G, B에 해당하는 배열 만들기 
pixR = pix.copy()
pixG = pix.copy()
pixB = pix.copy()
pixR[:, :, (1,2)] = 0
pixG[:, :, (0,2)] = 0
pixB[:, :, (0,1)] = 0

# 원본 이미지인 pix 행렬을 이미지 데이터로 출력
plt.subplot(141)
plt.imshow(pix)
plt.axis("off")
plt.title("RGB")

# pix 행렬에서 이미지 데이터의 R 채널을 출력
plt.subplot(142)
plt.imshow(pixR)
plt.axis("off")
plt.title("R")

# pix 행렬에서 이미지 데이터의 G 채널을 출력
plt.subplot(143)
plt.imshow(pixG)
plt.axis("off")
plt.title("G")

# pix 행렬에서 이미지 데이터의 B 채널을 출력
plt.subplot(144)
plt.imshow(pixB)
plt.axis("off")
plt.title("B")

plt.show()