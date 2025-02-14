import pandas as pd
df=pd.read_csv(r'C:\Users\Admin\OneDrive - Amity University\Documents\Python\Iris.csv')
"""
CHEATSHEAT:
d.dropna():                             REMOVE ROWS WITH NULL VALUES
d.fillna(value):                        REPLACE EMPTY VALUES
d.loc[row_num,'column_name']=newvalue:  REPLACING DATA
d.dropna():                             DELETE ROWS WITH NULL VALUES
d.drop(subset=["column_name"])          DELETE ROWS WITH NULL VALUES IN SPECIFIC COLUMN
x=d["column_name"].mean()		        AVERAGE VALUE
x=d["column_name"].mode()[0]            MOST OCCURING VALUE
print(d.duplicated)                     RETURNS TRUE IF DUPLICATE ROW
d.drop_duplicates                       DELETE DUPLICATES
"""
print(df.head(6)) #default is 5 rows
print(df.tail(6),'\n')

print("INFO\n",df.info(),'\n')

#DATA CLEANSING
'''Bad data can include empty cells, wrong format, duplicates'''
d=pd.read_excel(r"C:\Users\Admin\OneDrive - Amity University\Documents\Python\Pandas\book.xlsx")

#REMOVE ROWS WITH NULL VALUES
newd=d.dropna() #returns new dataframe, does not change the original
print("REMOVE NULL VALUES\n",newd.to_string(),'\n')
#use inplace=True to change original dataframe

#REPLACE EMPTY VALUES
d.fillna(60,inplace=True)
print("REPLACE EMPTY VALUES\n",d,'\n')

#REPLACING DATA 
d.loc[5, 'Weight_(kg)']=90
print("REPLACING DATA\n",d.to_string,'\n')

#For large datasets set boundary, for ex:
for x in d.index:
    if d.loc[x,"Weight_(kg)"]>100:
        d.loc[x,"Weight_(kg)"]=120
print("Weight above 100 as 120\n")
print(d.to_string)
#You can also delete outliers
for x in d.index:
    if d.loc[x,"Weight_(kg)"]>100:
        d.drop(x, inplace=True)
print("Delete outliers\n")
print(d.to_string)

x=d['BMI'].mean()
y=d["Weight_(kg)"].mode()[0]
print(x,y)