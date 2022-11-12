import pandas as pd
import numpy as np 

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)

print(df['생년월일'])
df['생년월일'] = pd.to_datetime(df['생년월일'])

print(df['생년월일'].dt)

print(df['생년월일'].dt.year)
print(df['생년월일'].dt.month)
print(df['생년월일'].dt.day)
print(df['생년월일'].dt.hour)
# 월욜 : 0 , 화욜 : 1 .... 일욜 : 6
print(df['생년월일'].dt.dayofweek)
df['생일_년'] = df['생년월일'].dt.year
df['생일_월'] = df['생년월일'].dt.month
df['생일_일'] = df['생년월일'].dt.day
print(df)


