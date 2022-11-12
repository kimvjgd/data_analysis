import pandas as pd
import numpy as np 

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)

# fillna(결측값을 채워준다.)

df['키']

# NaN값을 -1로 바꾼다.
df['키'].fillna(-1)

df2 = df.copy()
print(df2)

# method 1
# inplace 를 대입함과 동시에 덮어 씌워준다.
df2['키'].fillna(-1, inplace=True)
print(df2)

# method 2        <- 그냥 이게 나을 것 같다.
df2['키'] = df2['키'].fillna(-1)
print(df2)

# -1 말고 평균값을 넣어주고 싶다?
df3 = df.copy()
height = df3['키'].mean()
df3['키'] = df3['키'].fillna(height)
print(df3)

