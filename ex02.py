import pandas as pd
import os


file_name = "korean-idol.csv"

# file = open(file_name, 'r', encoding="utf-8")

df = pd.read_csv(file_name)
# excel을 읽어올꺼면
# read_csv대신 read_excel을 쓴다.

# print(df)
# print(df.columns)
# print(df.index)
print(df.info())
print(type(df))