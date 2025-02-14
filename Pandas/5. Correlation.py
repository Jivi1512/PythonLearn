import pandas as pd 
d=pd.read_csv(r"C:\Users\Admin\OneDrive - Amity University\Documents\Python\Pandas\data.csv")
print(d.to_string())
print(d.corr())