import pandas as pd
#csv file as input
file=pd.read_csv(r"C:\Users\Admin\OneDrive - Amity University\Documents\Python\Iris.csv")

#dictionary as table
data={'roll no.':[1,2,3],'name':['x','y','z'],'marks':[100,28,78]}
result=pd.DataFrame(data)
print(result,'\n')

#series(Series is a COLUMN, Dataframe is a TABLE)
a=pd.Series([1,2,3],)
print(a,'\n')

#adding custom labels
b=pd.Series([1,2,3], index=['x','y','z'])
print(b,'\n')

#dictionary keys as labels
c=pd.Series({'day1':100,'day2':200,'day3':300})
print(c,'\n') 

#Dataframe from Series
d=pd.DataFrame({'calories':[100,200,300],'time':[30,40,50]})
print(d,'\n')