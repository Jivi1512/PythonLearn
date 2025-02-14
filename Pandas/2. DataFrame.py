import pandas as pd

data={'name':['x','y','z'],'calories':[100,200,300],'time':[10,20,30]}
df=pd.DataFrame(data,index=[1,2,3])
print(df,'\n')

#use loc to return one or more rows
print(df.loc[1])
print(df.loc[1:2]) # or loc[[1,2]]

