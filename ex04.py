import pandas as pd

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)

print(df.head())

# column을 선택하는 법 3가지
# method 1    <- 무조건 그냥 이거써라
print(df['혈액형'])
# method 2
print(df.이름)


# 부분적으로 데이터를 가져오고 싶다.

print(df[:3])
# == df.head(3)

# loc 와 iloc를 자주 사용한다.
# loc     column[3:5] 이면 여기서는 3,4,5   이하 값을 모두 가져온다. 쫌 다르다.
print(df.loc[:, '이름'])       # ,를 기준으로 왼쪽은 행 오른쪽은 열
print(df.loc[:,['이름','생년월일']])
print(df.loc[3:8,['이름','혈액형']])

# iloc (position으로 색인)
print(df.iloc[:,[0,2]])
print(df.iloc[1:5,[0,2]])     # 1~4 여기서는 또 미만 값을 가져온다...

