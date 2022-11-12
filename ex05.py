import pandas as pd

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)

# boolean index로 뽑아낼 수 있다.
print(df['키'] > 180)

print(df[df['키']>180])

print(df[df['키']>180][['이름', '키']])   # 2차원 리스트로 묶어줘야한다.

# 위처럼 말고 loc를 사용하자
print(df.loc[df['키']>180, '이름'])
print(df.loc[df['키']>180, ['이름','키']])

# isin을 활용한 색인
my_condition = ['플레디스', 'SM']
df['소속사'].isin(my_condition)
df.loc[df['소속사'].isin(my_condition)]
print(df.loc[df['소속사'].isin(my_condition),'소속사'])


# 결측값null() 알아보기
# pandas 에서는 Null을 NaN => Not a Number로 표기된다.
print(df)
# 빠진 데이터를 보여준다.
print(df.info())
# 빠진 값을 true로 보여준다.
print(df.isna())

print(df['그룹'].isnull())
# 우리는 비어있지 않은 값들이 중요하다.
print(df['그룹'][df['그룹'].notnull()])

# 비어있는 애를 보자 loc를 잘 이용하자
print(df.loc[df['그룹'].isnull(),['키', '혈액형']])
