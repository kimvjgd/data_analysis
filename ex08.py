import pandas as pd

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)

print(df.describe())

print(df['키'].min())
print(df['키'].max())
print(df['키'].sum())
print(df['키'].mean())

# 분산과 표준편차
# 둘다 데이터가 평균으로부터 얼마나 떨어져 있는지 정도를 나타낸다.
# 분산은 (데이터-평균)**2
# 표준편차는 분산의 sqrt

import numpy as np
data_01 = np.array([1,3,5,7,9])
data_02 = np.array([3,4,5,6,7])

print(data_01.mean())
print(data_02.mean())
print('---분산---')
print(data_01.var())
print(data_02.var())
print('---표준편차---')
print(data_01.std())
print(data_02.std())

# 주로 표준편차를 많이 사용하며, 데이터가 평균으로부터 얼마나 퍼져있는지 정도를 나타내는 지표이다.
print(df['키'].var())
print(df['키'].std())

# 데이터의 갯수를 세는 count
print(df['키'].count())

# 중앙값 (오름차순으로 세운다음에 가운데)
df['키'].median()

# 최빈값 (mode)     - 제일 많이 출현한 값이다.
df['키'].mode()







