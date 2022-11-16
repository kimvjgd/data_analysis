import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.arange(50)
area = x * y * 1000

# plt.scatter(x,y, s=area,c=colors)
# plt.show()

sns.scatterplot(x, y, size=area, sizes=(area.min(), area.max()), hue=area, palette='coolwarm')
plt.show()
