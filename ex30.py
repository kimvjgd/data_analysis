import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# pie chart : 점유율 표현할때
# explode : 파이에서 툭 튀어져 나온 비율
# autopct : 퍼센트 자동으로 표기
# shadow : 그림자 표기
# startangle : 파이를 그리기 시작할 각도
labels = ['Sam','Jua','App', 'Xia', 'Opp', 'Etc']
sizes = [20,16,10,12,7,36]
explode = (0.3,0,0,0,0,0)

patches, texts, autotexts = plt.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Smartphone pie', fontsize=15)

# label 텍스트에 대한 스타일 적용
for t in texts:
  t.set_fontsize(12)
  t.set_color('gray')
# pie 위의 텍스트에 대한 스타일 적용
for t in autotexts:
  t.set_color('white')
  t.set_fontsize(19)
plt.show()


