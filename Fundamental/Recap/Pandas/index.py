
import pandas as pt

df = pt.read_csv("diabetes.csv", index_col='Age')
print(df.describe()) # it shows--> count,mean,std,min,25%,50%,75%,max of all data.

df_head = df.head()
print(df_head) #it shows only first 5 data from all data


print(df_head.groupby('HighBP').sum()) #sum for individual value

print(df_head.groupby('HighBP').mean()) #mean for individual value

print(df_head['CholCheck'].value_counts()) # how many types of number & how many number in same type in a column CholChek,it shows

print(df_head['Education']) # finding single column
