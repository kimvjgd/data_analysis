import pandas as pd
import numpy as np 

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)


# one hot encoding 원 핫 인코딩
# 원핫인코딩은 한개의 요소는 True 나머지 요소는 False로 만들어주는 기법이다.
df.head()

blood_map={
  'A':0,
  'B': 1,
  'AB': 2,
  'O':3,
}

df['혈액형_code'] = df['혈액형'].map(blood_map)
print(df)

# 우리가 만약 df['혈액형_code']를 머신러닝 알고리즘에 그대로 넣어 데이터를 예측하라 한다면 문제가된다.
# 1+2=3 -> B + AB = O 라는 관계를 이상하게 뽑아준다.

print(pd.get_dummies(df['혈액형_code']))

print(pd.get_dummies(df['혈액형_code'], prefix='혈액형'))
