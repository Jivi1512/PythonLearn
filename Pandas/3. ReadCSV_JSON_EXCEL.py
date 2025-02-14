import pandas as pd
df=pd.read_csv(r"C:\Users\Admin\OneDrive - Amity University\Documents\Python\Iris.csv")
print(df.to_string(),'\n')
#use to_string() to print the entire DataFrame.
print(df,'\n')

'''In my system the number is 60, which means that if the DataFrame contains more than 60 rows,
 the print(df) statement will return only the headers and the first and last 5 rows.
 
 You can change the maximum rows number with the same statement.'''
print(pd.options.display.max_rows)
pd.options.display.max_rows=200

#JSON
#Big datasets are often stored/extracted as JSON
jd=pd.read_json(r"C:\Users\Admin\OneDrive - Amity University\Documents\Python\Pandas\data.js")
print(jd.to_string())

#EXCEL
d=pd.read_excel(r"C:\Users\Admin\OneDrive - Amity University\Documents\Python\Pandas\book.xlsx")
print(d)