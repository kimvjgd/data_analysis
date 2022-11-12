import pandas as pd
import numpy as np 

file_name1 = "korean-idol.csv"
file_name2 = "korean-idol-2.csv"
df = pd.read_csv(file_name1)
df2 = pd.read_csv(file_name2)

# concat는 그냥 단순하게 이어붙이는 것이라면
# merge는 특정 고유한 키(unique id)값을 기준으로 병합한다.

print(df.head())
print(df2.head())

# df와 df2는 이름이라는 column이 겹친다.
# 우리는 '이름'을 기준으로 합칠 것이다.

df_right = df2.drop([1,3,5,7,9], axis=0)
df_right = df_right.reset_index(drop=True)
print(df_right)

# concat으로 합쳤다면 이름과 상관없이 그냥 밑에 5개에 NaN이 들어갔을 것이다.
# 잘못됐다.
# 이래서 merge로 '이름'을 기준으로 합쳐야한다.


# 4가지 left, right, inner, outer

# on = 기준 column
# how -> left dataframe에 키 값이 존재하면 해당 데이터 유지  -> right는 NaN
print(pd.merge(df, df_right, on='이름', how='left'))
# 아까 drop한 5개 빼고 나온다.
print(pd.merge(df, df_right, on='이름', how='right'))

# inner, outer -> 교집합 or 합집합

# inner 교집합 -> 둘 다 있을 때만 남긴다.
print(pd.merge(df, df_right, on='이름', how='inner'))

# outer 합집합
print(pd.merge(df, df_right, on='이름', how='outer'))

# column명은 다르지만, 동일한 데이터인 경우?
# df_right의 이름은 -> 성함으로 바꾼다.
df_right.columns = ['성함', '연봉', '가족수']

# 이럴 때는
pd.merge(df, df_right, left_on='이름', right_on='성함', how='outer')

