import pandas as pd
import numpy as np 

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)


df = pd.DataFrame({'통계': [60,70,80,85,75], '미술': [50,55,80,100,95], '체육': [70,65,50,95,100]})
print(df)

print(df['통계'] + df['미술'])

print(df['통계'] + 100)

print(df.mean(axis=1))
print(df)

print(df.sum(axis=1))

# NaN 값이 존재할 경우 연산
df = pd.DataFrame({'통계': [60,70,80,85,75], '미술': [50,55,80,100,95], '체육': [70,65,50,95,100]})
print(df['통계']/np.nan) #-> 모두 NaN 값이 나온다.

df1 = pd.DataFrame({'미술':[10,20,30,40,50,60], '통계':[60,70,80,90,100,110]})
df2 = pd.DataFrame({'미술':[10,20,30,40,50], '통계':[60,70,80,90,100]})
# 빈 값은 -> NaN으로 들어간다.




