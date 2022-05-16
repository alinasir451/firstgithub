# step 1 import lib
import pandas as pd

# import data from file
chilla = pd.read_csv("data_viz.csv")
print(chilla)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)

# step 4 plot basic graph with 1 variable

# p = sns.countplot(x= "sex", data=kashti)
# plt.show()

# step 4 plot basic graph with 2 variable
p = sns.countplot (x= "Gender", data=chilla, hue="Age")
p.set_title("Tile Countplot")
plt.show()