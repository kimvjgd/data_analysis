from pydoc import describe
import pandas as pd
import numpy as np 

file_name = "seoul_house_price.csv"
df = pd.read_csv(file_name)

# 너무 어려운 column명은 재정의해준다.
df = df.rename(columns={'분양가격(㎡)': '분양가격'})
# print(df.describe())
# print(df.info())

# df['분양가격'].astype(int)
# df.loc[df['분양가격'] == '  ']

df['분양가격'] = df['분양가격'].str.strip()

print(df.loc[df['분양가격']==''])

# 빈 공백이 있는 데이터는 0으로 넣어주겠다.
df.loc[df['분양가격']=='', '분양가격'] = 0
df['분양가격'] = df['분양가격'].fillna(0)

# 숫자 1개에 , 가 들어가 있다.
df['분양가격'] = df['분양가격'].str.replace(',','')
df['분양가격'] = df['분양가격'].fillna(0)

# 어떤 것들은 - 으로 되어있다.
df['분양가격'] = df['분양가격'].str.replace('-','')
df['분양가격'] = df['분양가격'].fillna(0)

df.loc[df['분양가격']=='','분양가격'] = 0

df['분양가격']=df['분양가격'].astype(int)

print(df.info())

# '전용면적' 제거
df['규모구분']=df['규모구분'].str.replace('전용면적', '')

# 지역명별로 평균 분양가격을 확인해보자
print(df.groupby('지역명')['분양가격'].mean())

# 분양가격이 100보다 작은 행 제거 -> 0들을 없앤다.
idx = df.loc[df['분양가격'] < 100].index

print(idx)

df.drop(idx, axis=0)


df.groupby('연도')['분양가격'].mean()

# pivot 테이블로 만들어보자
print(pd.pivot_table(df, index='연도',columns='규모구분',values='분양가격'))

print(df.groupby(['연도','규모구분']).mean())

# 행을 잘 맞추기 위해
# DataFrame으로 바꿔준다.
print(pd.DataFrame(df.groupby(['연도','규모구분']).mean()))

