import pandas as pd

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)

print(df.head())

# 이렇게 하면 안된다. => new_df를 바꿔도 df가 바뀐다.
# new_df = df         # 메모리를 복제해주는 것이다.
# new_df['이름'] = 0
# print(df.head())

# 이렇게 copy 해야한다.
copy_df = df.copy() 
copy_df['이름'] = 0
print(df.head())
# print(copy_df.head())