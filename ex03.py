import pandas as pd
import os


file_name = "korean-idol.csv"

# file = open(file_name, 'r', encoding="utf-8")

df = pd.read_csv(file_name)

# column을 한번에 볼 수 있다.
print(df.columns)
# # column이름을 재정의 하고 싶다?
# new_col = ['여기에다가 넣은다음']
# df.columns = new_col
# 이렇게 하면 된다.

print(df.index)

# df.info() : 주로 빠진 값(null 값)과 데이터 타입을 볼 때 활용한다.
print(df.info())

# 통계 정보 알아보기 (describe)
print(df.describe())

# 형태 알아보기
print(df.shape)
# (15, 8)   15행 8열

# 상위 5개
df.head()

# 하위 3개
df.tail(3)

# index 정렬
# 오름 차순정렬 
df.sort_index()
df.sort_index(ascending=False)# 내림차순 정렬

# value 정렬      값을 기준으로 정렬
print(df.sort_values(by='키', ascending=False))

# 여러가지 변수를 순서대로 sort하고 싶다.   키부터 sort하고 브랜드평판지수 sort
print(df.sort_values(by=['키', '브랜드평판지수'], ascending=False))






