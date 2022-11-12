import pandas as pd
import os

file_name = 'bioresorbable.xlsx'

df = pd.read_excel(file_name)

# print(df)
print(df.info())
