import pandas as pd
import matplotlib.pyplot as plt
f=pd.read_csv(r"C:\Users\Admin\OneDrive - Amity University\Documents\Python\Iris.csv")
blank=f.isnull().sum()
print("Blank values=",blank)

data = f.select_dtypes(include=['number'])

maxvalue=data.max()
minvalue=data.min()
avgvalue=data.mean()

print("Maximum Values in Each Column:", maxvalue)
print("Minimum Values in Each Column:", minvalue)
print("Average Values in Each Column:", avgvalue)

for column in f.columns:
    plt.figure(figsize=(10, 6))
    data[column].value_counts().plot(kind='bar', color='skyblue')
    plt.title(f'Bar Graph of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    