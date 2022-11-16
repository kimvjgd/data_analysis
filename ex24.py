import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 한글 폰트를 유지시킴
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
###############################################################


plt.rc('font', family='NanumBarunGothic')
plt.rcParams["figure.figsize"]=(12,9)

np.random.rand(50)
np.arange(50)

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.arange(50)
area = x * y * 1000
plt.scatter(x, y, s=area, c=colors)     # s = size이다.
# plt.show()

# cmap, alpha
# cmap : 컬러를 지정하면 컬러 값을 모두 같게 가져갈 수 있다.
# alpha 값은 투명도를 나타낸다. (투명)0~1(불투명)
plt.subplot(131)
plt.scatter(x, y, s=area, cmap='blue', alpha=0.1)
plt.title('alpha=0.1')

plt.subplot(132)
plt.scatter(x, y, s=area, cmap='blue', alpha=0.5)
plt.title('alpha=0.5')

plt.subplot(133)
plt.scatter(x, y, s=area, cmap='blue', alpha=1.0)
plt.title('alpha=1')
    
plt.show()
