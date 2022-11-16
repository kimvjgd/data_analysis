import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x_label = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
x = np.arange(len(x_label))
y_1 = [66,80,60,50,80,10]
y_2 = [55,90,40,60,70,20]

# 넓이 지정
width = 0.35

# subplot 생성
fig, axes = plt.subplots()

# 넓이 설정
axes.bar(x-width/2, y_1, width,align='center', alpha=0.5)
axes.bar(x+width/2, y_2, width,align='center', alpha=0.8)

# xtick 설정
plt.xticks(x)
axes.set_xticklabels(x_label,rotation=30)
plt.ylabel('Number of Stus')
plt.title('Subjects')
plt.legend(['john','peter'])
plt.show()

