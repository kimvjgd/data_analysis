import pandas as pd

# Create Series 1차원 배열
# method1
pd.Series([1,2,3,4])

# method2
# a = [1,2,3,4]
# pd.Series(a)


# Create DataFrame 2차원 배열
# method1
company1 = [['삼성', 2000, '스마트폰'],
            ['현대', 1000, '자동차'],
            ['네이버', 500, '포털']]

pd.DataFrame(company1)
df1 = pd.DataFrame(company1)
print(df1)
df1.columns = ['기업명', '매출액', '업종']

print(df1)

# method2
company2 = {'기업명':['삼성','현대','네이버'],
            '매출액':[2000,1000,500],
            '업종':['스마트폰','자동차','포털']}
df2 = pd.DataFrame(company2)
print(df2)


# Index를 특정 column으로 지정하기
df1.index = df1['기업명']
print(df1)

# DataFrame은 Series의 모음이다.
print(type(df1['매출액']))