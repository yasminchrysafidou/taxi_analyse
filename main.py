
### kleine analyse
### über den taxis datensatz


import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("taxis")
sns.histplot(data=df, x="tip", hue="pickup_borough")

plt.show()