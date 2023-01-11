# 01 - Import Libraries 
import pandas as pd
#02 -  Import Data From File 
chilla = pd.read_csv("data_viz.csv")
print(chilla)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True)
p=sns.countplot(x= "Gender" , hue="Age" , data = chilla)
plt.show()
