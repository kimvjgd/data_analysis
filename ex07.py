import pandas as pd

file_name = "korean-idol.csv"
df = pd.read_csv(file_name)


# row 추가
# append를 이용해서 data를 추가할 수 있다.
# ignore_index = True를 꼭 줘라 -> 에러막음
# 다시 df = df.append(...) 를 해줘야지 들어간다
df = df.append({'이름': '테디', '그룹':'테디그룹','소속사':'끝내주는 소속사','성별':'남자','생년월일':'1970-02-01','키':195.0,'혈액형':'O','브랜드평판지수': 12345678}, ignore_index=True)

print(df)

# column 추가
df['국적'] = '대한민국'
print(df.head())

# 이렇게 일부 데이터만 바꿀 수 있다.
df.loc[df['이름']=='지드래곤', '국적'] = 'korea'
print(df.head())

