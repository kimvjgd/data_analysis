# Seaborn
# matplotlib을 기반으로 다양한 색상과 차트를 지원하는 라이브러리

import seaborn as sns

# 아름다운 디자인
# 통계 기능 기반의 차트 countplot, relplot, lmplot
# pandas, matplotlib 호환

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tips = sns.load_dataset("tips")
# sns.violinplot(x='day', y="total_bill", data=tips)
# plt.title('violin plot')
# plt.show()

# sns.countplot(tips['day'])
# plt.title('countplot')

# sns.relplot(x='tip',y='total_bill', data=tips)
# plt.title('relplot')

# sns.lmplot(x='tip',y='total_bill', data=tips)
# plt.title('lmplot')

# 이쁜 디자인
sns.barplot(x='day', y='total_bill', data=tips, palette='BrBG_r')

# pandas 데이터 프레임과 높은 호환성
# hue 옵션으로 bar를 구분
# x,y ticks&labels을 알아서 생성 -> legend도 자동생성 -> 신뢰구간도 알아서 계산 & 생성
sns.catplot(x='sex', y='total_bill', 
            hue='smoker',     # smoker로 barplot을 나누겠다.
            col='time',
            data=tips, kind='bar')

plt.show()