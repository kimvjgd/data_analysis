import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트를 유지시킴
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
###############################################################

titanic = sns.load_dataset('titanic')
print(titanic)

#countplot
#distplot, hist
# heatmap
# pairplot
# violinplot
# lmplot
# relplot
# jointplot
# 필요할 떄 강의를 찾아볼 것 fastcampus