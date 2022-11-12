import pandas as pd
import numpy as np 

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)

# GroupBy (그룹으로 묶어보기)
# 데이터를 그룹으로 묶어 분석할 때 사용한다.
df.groupby('소속사')

print(df.groupby('소속사').count())
print(df.groupby('소속사').mean())
print(df.groupby('소속사').sum())

print(df.groupby('성별').sum())


# 특정 열만 출력하고 싶다.
df.groupby('혈액형')['키'].mean()

# multi index
# 먼저 혈액형으로 나누고 그 다음에 성별로 나눈다.
print(df.groupby(['혈액형', '성별']).mean())

df2 = df.groupby(['혈액형','성별']).mean()
print(df2)
# row index 혈액형이 빠지면서 열 index로 변한다.
print(df2.unstack('혈액형'))

print(df2.unstack('성별'))

# 인덱스 초기화
# 일반 dataframe처럼 2차원으로 바꿔준다.
print(df2.reset_index())



