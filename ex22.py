# EDA
# Exploratory Data Analysis
# 탐색적 데이터 분석 -> 수집한 데이터가 들어왔을 때, 이를 다양한 각도에서 관찰하고 이해하는 과정



import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# 한글 폰트를 유지시킴
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
###############################################################

file_name = "seoul_house_price.csv"
df = pd.read_csv(file_name)

df = df.rename(columns={'분양가격(㎡)': '분양가격'})
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

# df['분양가격'].plot()


# df['분양가'].plot()

# plt.plot(df['분양가격'])
# plt.show()

df_seoul = df.loc[df['지역명']=='서울']
df_seoul_year = df_seoul.groupby('연도').mean()
print(df_seoul_year)
# df_seoul_year['분양가격'].plot(kind='line')


# df.groupby('지역명')['분양가격'].mean().plot(kind='bar') # barh -> horizontal

# 히스토그램(hist)
# 분포-빈도를 시각화하여 보여줌
# df['분양가격'].plot(kind='hist')

# 커널 밀도 그래프
# 히스토그램과 유사하게 밀도를 보여주는 그래프이다.
# 히스토그램과 유사한 모양새를 갖추고 있다.
# 부드러운 라인을 가지고 있다.

# import scipy
# df['분양가격'].plot(kind='kde')

# Hexbin
# 고밀도 산점도 그래프
# x, y 키 값을 넣어줘야 한다.
# x, y값 모두 numeric 한 값을 넣어줘야한다.
# 데이터의 밀도를 추정
# df.plot(kind='hexbin', x='분양가격',y='연도', gridsize=20)

# 박스 플롯
# df_seoul = df.loc[df['지역명']=='서울']
# df_seoul['분양가격'].plot(kind='box')


# df.groupby('월')['분양가격'].count().plot(kind='line')
# line 아래가 색칠
# df.groupby('월')['분양가격'].count().plot(kind='area')


# pie plot
# 데이터의 점유율을 보여줄 때 유용하다.
# df.groupby('연도')['분양가격'].count().plot(kind='pie')

# scatter plot
df.plot(x='월', y='분양가격', kind='scatter')

plt.show()
