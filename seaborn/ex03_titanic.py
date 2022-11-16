import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic.head())

sns.barplot(x='sex', y = 'survived', hue='pclass', data=titanic, palette='muted')
plt.show()

