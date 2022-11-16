import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)
y = 1 + np.sin(x)

# plt.plot(x, y)


sns.set_style('darkgrid')
sns.lineplot(x, y)
plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin graph', fontsize=18)

# seaborn area plot을 지원하지 않는다.

# histogram
N = 100000
bins = 30

# x = np.random.randn(N)
# plt.hist(x, bins=bins)

# kde : 밀도를 표현
sns.distplot(x, bins=bins, kde=False, hist=True, color='g')
# vertical : 가로로
sns.distplot(x, bins=bins, kde=True, hist=True, vertical=True, color='g')

# sns.boxplot(data, orient='v',width=0.2)


titanic = sns.load_dataset('titanic')
titanic.head()
sns.boxplot(x='pclass', y='age',hue='survived',data=titanic)

plt.show()
