import csv

rows = [[],[],[],[],[],[],[]] # 요일별

with open("passby_data.csv") as fcsv:           # csv파일 읽어오기
    reader = csv.DictReader(fcsv)
    day = hr = 0
    for row in reader:                          # 각 행을 row에 불러온다.
        rows[day].append(row)                   # 해당 day에 시간별 row추가하기
        hr += 1                                 # 그 다음 한시간으로 더해주기
        if (hr == 24):                          # 자정이 된 경우
            hr = 0                              # 시각 초기화
            day += 1                            # 다음 요일로 가기

hour_title = [  \
    '00-01', '01-02', '02-03', '03-04', '04-05', \
    '05-06', '06-07', '07-08', '08-09', '09-10', \
    '10-11', '11-12', '12-13', '13-14', '14-15', \
    '15-16', '16-17', '17-18', '18-19', '19-20', \
    '20-21', '21-22', '22-23', '23-24',] # 시간 별 x축 이름

avg = []                                        # 시간별 평균 유동인구
wavg = []                                       # 시간별 평균 여성유동인구
yavg = []                                       # 시간별 평균 30대이하 유동인구
for hr in range(24):                        # 각 시간별로 순회하여 구하기
    num = wnum = ynum = 0                       # 요일별 합 구할 임시변수
    for day in range(7):                    # 요일별 순회
        num += int(rows[day][hr]['num'])        # 해당 시간대 요일별 합 구하기
        wnum += int(rows[day][hr]['wnum'])
        ynum += int(rows[day][hr]['ynum'])
    avg.append(num/7)                           # 요일 수로 나누어 평균을 구해 추가
    wavg.append(wnum/7)
    yavg.append(ynum/7)

import matplotlib.pyplot as plot                # pyplot 라이브러리
from matplotlib import font_manager, rc         # font manager 라이브러리

font_name = font_manager.FontProperties(fname="malgun.ttf").get_name()
rc('font', family=font_name)                    #한글을 출력하기 위한 폰트 로딩

plot.title('시간별 유동인구 (평균)', fontsize=16)
plot.xlabel('시간 (n시 ~ n+1시)', fontsize=10)
plot.ylabel('유동 인구 수 (명)', fontsize=12)

plot.plot(hour_title, avg, label='총 유동인구')
plot.scatter(hour_title, avg)
plot.plot(hour_title, wavg, c='green', label='여성인구') # label로 legend와 연결
plot.scatter(hour_title, wavg, c='green')       # c로 색상 설정
plot.plot(hour_title, yavg, c='red', label='30대 이하 인구')
plot.scatter(hour_title, yavg, c='red')

plot.legend()                                   # legend 표시 (label로 연결 이후)
plot.show()