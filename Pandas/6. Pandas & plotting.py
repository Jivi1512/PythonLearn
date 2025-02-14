import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Admin\OneDrive - Amity University\Documents\Python\Pandas\data.csv")
df.plot()
plt.show()

df.plot(kind="scatter", x="Duration", y="Calories")
plt.show()

df["Duration"].plot(kind="hist")
plt.show()
