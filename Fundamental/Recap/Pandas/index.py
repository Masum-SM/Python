
import pandas as pt

df = pt.read_csv("diabetes.csv", index_col='Age')
print(df.describe()) # it shows--> count,mean,std,min,25%,50%,75%,max of all data.

df_head = df.head()
print(df_head) #it shows only first 5 data from all data
