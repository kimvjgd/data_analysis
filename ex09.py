import pandas as pd
import numpy as np 

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)


# pivot table 
# 수많은 열과 행이 있는데 내가 원하는 열과 행만 보고 싶다.
# 그때 pivot table을 사용하면 된다.
# 여러개를 평균 내서 나온다.
print(pd.pivot_table(df, index='소속사', columns='혈액형', values='키'))
# aggfunc으로 어떻게 보여줄껀지 결정해준다.  -> np.mean을 주면 평균이 나온다.
print(pd.pivot_table(df, index='그룹', columns='혈액형', values='브랜드평판지수', aggfunc=np.sum))



