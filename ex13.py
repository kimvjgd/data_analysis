import pandas as pd
import numpy as np 

file_name1 = "korean-idol.csv"
file_name2 = "korean-idol-2.csv"
df = pd.read_csv(file_name1)
df2 = pd.read_csv(file_name2)


# dataframe을 합칠 수 있다.
# concat (단순한 방법으로 합친다.)

df_copy = df.copy()

# row에 합칠 때는 pd.concat에 합칠 데이터프레임을 list로 합쳐준다.
# row기준으로 합칠 때는 sort=False 옵션을 주어 순서가 유지되도록 합니다.
df_concat = pd.concat([df, df_copy], sort=False)
# 이렇게 하면 index가 꼬인다. reset_index()를 통해서 index를 초기화 해줘야한다.

print(df_concat.reset_index())

# but index라는 column이 들어와버렸다.
df_concat = pd.concat([df, df_copy], sort=False)
print(df_concat.reset_index(drop=True))


# column 기준으로 옆으로 합치기
print(pd.concat([df, df2], axis=1))

# 만약 여기에 행의 갯수가 안맞으면?
# 에러가 안뜨고 비어있는 값에 NaN이 들어간다.
# 그냥 편하게 써도 되겠구나...!

