import matplotlib.pyplot as plt

# 장점
# 파이썬 표준 시각화 도구라고 불릴만큼 다양한 기능을 지원
# 보다 다양한 그래프를 그릴 수 있다.
# pandas와 연동이 용이

# 단점
# 한글에 대한 완벽한 지원 x
# 세부 기능이 많으나, 사용성이 복잡

# 한글 폰트를 유지시킴
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
###############################################################

import numpy as np

data = np.arange(1, 100)
# print(data)

# plt.plot(data)
# plt.show()

# 다중 그래프
# data = np.arange(1,51)
# data2 = np.arange(51, 101)

# plt.plot(data)
# plt.figure()      # figure는 새로운 그래프를 생성한다.
# plt.plot(data2)
# plt.plot(data2+50)
# plt.show()

# 여러개의 plot을 그리는 방법 subplot

# data = np.arange(100, 201)
# plt.subplot(1,2,1)    # 2행 1열 중 1번째
# # plt.subplot(121)  # 이렇게 표기해도 된다.
# plt.plot(data)

# data2 = np.arange(200,301)
# plt.subplot(2,1,2)
# plt.plot(data2)

# plt.show()


# 여러개의 plot을 그리는 방법 (subplot) -s 가 더 붙는다.
# data = np.arange(1,51)
# # 밑그림
# fig, axes = plt.subplots(2,3)

# axes[0,0].plot(data)
# axes[0,1].plot(data*data)
# axes[0,2].plot(data**3)
# axes[1,0].plot(data % 10)
# axes[1,1].plot(-data)
# axes[1,2].plot(data // 20)
# plt.tight_layout()      # tight하게 이쁘게...!
# plt.show()


# plt.plot([1,2,3],[3,6,9])
# plt.plot([1,2,3],[2,4,9])
# plt.title('이것은 타이틀입니다.', fontsize=20)
# plt.xlabel('사람숫자', fontsize=10)
# plt.ylabel('가족숫자', fontsize=10)


# 마커 marker
plt.plot(np.arange(10),np.arange(10)*2, marker='o',markersize=5, color='b')
plt.plot(np.arange(10),np.arange(10)**2,linestyle='--')
plt.plot(np.arange(10),np.log(np.arange(10)),linestyle=':')


# tick 설정
plt.xticks(rotation=90)
plt.yticks(rotation=30)

# 범례 legend 설정
plt.legend(['10*2', '10**2', 'log'])

# x, y limit 설정
plt.xlim(0,5)
plt.ylim(0.5, 10)

# grid 옵션 추가
plt.grid()


# 이미지 저장
# plt.savefig('my_graph', dpi=300)      # dpi : 해상도

plt.show()



