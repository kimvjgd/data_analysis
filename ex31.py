# box plot
# 필요할 때 강의를 보자


# 3d 시각화
# 필요할 때 강의를 보자


# imshow
# 이미지 데이터와 유사하게 행과 열을 가진 2차원의 데이터를 시각화할 때는 imshow를 활용한다.
from sklearn.datasets import load_digits
digits = load_digits()
X=digits.images[:10]
print(X[0])

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, axes = plt.subplots(nrows=2, ncols=5, sharex=True, figsize=(12, 6), sharey=True)

for i in range(10):
  axes[i//5][i%5].imshow(X[i], cmap='Blues')
  axes[i//5][i%5].set_title(str(i), fontsize=20)
plt.tight_layout()
plt.show()