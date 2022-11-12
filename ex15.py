import pandas as pd
import numpy as np 

file_name1 = "korean-idol.csv"
# file_name2 = "korean-idol-2.csv"
df = pd.read_csv(file_name1)
# df2 = pd.read_csv(file_name2)

# print(df.info())
print(df['키'].dtypes)
# type 변환
# df['키'].astype(int)
# 그 전에 NaN값을 바꿔줘야한다.
df['키'] = df['키'].fillna(-1)
print(df['키'].astype(int))

