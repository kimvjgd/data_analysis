import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.arange(0, 10, 0.1)
y_1 = 1 + np.sin(x)

plt.plot(x, y_1, label='1+sin', color='blue', alpha=0.3, marker='o')


plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin and cos graph', fontsize=18)

plt.grid()

# plt.show()

# 2개 이상의 그래프 그리기
y_2 = 1+np.cos(x)
plt.plot(x, y_2, label='1+cos', color='red', alpha=0.7,linestyle=':')

plt.grid()
plt.legend()


plt.show()

