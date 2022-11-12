import pandas as pd
import numpy as np 

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)


# apply는 Series나 DataFrame에 좀 더 구체적인 로직을 적용하고 싶은 경우에 활용한다.
# if 남자 -> 1, 여자 -> 0 으로 바꾸고 싶다??

# method 1
# df.loc[df['성별']=='남자', '성별'] = 1
# df.loc[df['성별']=='여자', '성별'] = 0
# 단점 -> 남자 여자로 나뉘는 경우는 쉽다. 우리가 이미 2개 다 알고 있다. 만약 group이 많으면 힘들다.

# 구체적인 logic을 사용하려면
def male_or_female(x):
  if x == '남자':
    return 1
  if x == '여자':
    return 0

print(df['성별'].apply(male_or_female))
df['성별_NEW'] = df['성별'].apply(male_or_female)

# cm당 브랜드 평판지수를 구해보자
# if 키 = 178 브랜드평판지수 = 99000
# 값 99000/178
# 이번에는 dataframe 전체를 넘겨준다.
def cm_to_brand(df):
  value = df['브랜드평판지수'] / df['키']
  return value

df.apply(cm_to_brand, axis=1)


# lambda 함수의 적용
# lambda는 1줄로 작성하는 간단 함수식이다.
print(df['성별'].apply(lambda x: 1 if x== '남자' else 0))

# 실제로는 간단한 계산식을 적용하려는 경우에 많이 사용한다.
df['키'].apply(lambda x: x/2)
df['키'].apply(lambda x: x**2)

my_map = {'남자':1, '여자':0}
print(df['성별'].map(my_map))