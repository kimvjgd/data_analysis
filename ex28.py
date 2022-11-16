import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Area Plot -> line plot 인데 밑에를 다 채워줌

x = np.arange(1, 21, 0.1)
y= np.random.randint(low=5, high=10, size=20)
# y_2 = 1+np.sin(x)
# y_3 = 1+np.cos(x)

# 겹쳐그리기 가능
# plt.fill_between(x, y_2, color='red', alpha=0.1)
# plt.fill_between(x, y_2, color='blue', alpha=0.2)

plt.fill_between(x, y, color='green', alpha=0.3)
plt.plot(x, y, color='green', alpha=0.8)     # 선만 진하게 하고 싶으면 위에 덮는다.
plt.show()