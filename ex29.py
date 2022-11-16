import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# histogram - 데이터의 밀도를 볼 때

N = 100000
bins = 30     # 구간을 몇개로 설정할 것이냐?
x=np.random.randn(N)
plt.hist(x, bins=bins)
print(x)
# plt.show()

# 다중 histogram 그리기
fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=True)

fig.set_size_inches(12,5)

axs[0].hist(x, bins=bins)       # bins가 커질수록 y가 낮아진다. 범위가 많아진다.
axs[1].hist(x, bins=bins*2)
axs[2].hist(x, bins=bins*4)

# plt.show()
# 다중 histogram 그리기
fig, axs = plt.subplots(1, 2, tight_layout=True)

fig.set_size_inches(9,3)


# 범위에 몇 % 있는지 보고싶으면 density=True
axs[0].hist(x, bins=bins*2, density=True,cumulative=True) 
axs[1].hist(x, bins=bins*4, density=True)

plt.show()

