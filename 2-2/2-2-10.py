import numpy as np

myImg = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 0, 0, 0],
                  [1, 1, 1, 1, 1, 0, 0, 0],
                  [0, 1, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]])

yrImg = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]])

result = myImg-yrImg
result *= 2
print(result)

import turtle                                  # Possibly requires 'python3-tk' (sudo apt install python3-tk)
# (x,y) 위치에 pSize 크기의 픽셀을 pCol 색으로 그리는 함수
def putPixel(x, y, pSize, pCol):               # 메인 소스 코드에서 호출하는 픽셀 채우기 함수
    turtle.penup()                             # 좌표 이동을 위해 펜기능을 비활성화   
    turtle.goto(x*pSize,(-1)*y*pSize)               # 주어진 좌표로 이동
    turtle.pendown()                           # 펜기능을 다시 활성화
    turtle.begin_fill()                        # 다각형을 그릴 때 내부를 채우기
    turtle.fillcolor(pCol)                     # 다각형의 채움색 설정하기
    turtle.setheading(45)                      # 시작 각도
    turtle.circle(pSize/2, steps = 4)          # 정사각형 픽셀 도출하기
    turtle.end_fill()                          # 채우기 끝

for y in range (0, 8):
    for x in range (0, 8):
        if (result[y][x] > 0):
            putPixel(x,y,10, "blue")
        else:
            putPixel(x,y,10, "white")
