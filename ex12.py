import pandas as pd
import numpy as np 

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)

# NaN이 있는 행을 제거
# dropna
df.info()
df.dropna()

# axis=0은 행을 드랍한다.
df.dropna(axis=0)     # 기존의 dropna()와 동일하다.
# axis=1은 열을 드랍한다.
df.dropna(axis=1)

# how option -> any: 한개라도 있는 경우 drop, all: 모두 NaN인 경우 drop
# default는 any이다.
df.dropna(axis=0, how='all')
df.iloc[10] = np.nan
print(df)
df.dropna(axis=0, how='all')

# column의 중복값 제거
# if 178이 있으면 뒤에 사람이 178이면 중복된 뒤의 178을 없애준다. NaN도 첫번째 빼고 중복된 것을 없애준다.
df['키'].drop_duplicates()
 
# keep option을 통해서 나중의 값을 남길 수도 있다.
df['키'] = df['키'].drop_duplicates(keep='last')
print(df)

# 행 전체 제거
# if 그룹 중에 겹치는 것이 있으면 행 전체를 날려준다.
df.drop_duplicates('그룹')
df.drop_duplicates('그룹',keep='last')

# 중복이 아니라 그냥 임의로 행과 열을 날려줄 수 있다.
# drop
# column을 제거
df.drop('그룹', axis=1)
df.drop(['그룹','소속사'], axis=1)

# row를 제거
df.drop(3, axis=0)
df.drop([3,5], axis=0)

