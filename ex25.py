import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
y = [66,80,60,50,80,10]


plt.figure(figsize=(6,3))
# plt.bar(x,y, align='center', alpha=0.7, color='red')
# plt.xticks(x,rotation=60)
plt.barh(x,y, align='center', alpha=0.7, color='red')
plt.yticks(x)
plt.ylabel('Number of Stus.')
plt.title('Subject')
plt.show()


