import pandas as pd
import numpy as np 

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)

df.select_dtypes()

# object column
df.select_dtypes(include='object')
# 숫자형 column
df.select_dtypes(exclude='object')

# 문자열이 포함된 DataFrame의 연산으로 발생되는 error를 피하기 위해서
# 아래 2개는 에러가 뜬다.
# df + 10
# df.select_dtypes(include='object') + 10
# 이것은 숫자만 골랐어서 에러가 안뜬다.
df.select_dtypes(exclude='object') + 10

# 이렇게 하면 숫자형만 뽑아준다.
num_cols = df.select_dtypes(exclude='object').columns
df[num_cols]

