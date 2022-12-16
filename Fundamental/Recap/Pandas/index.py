
import pandas as pt

df = pt.read_csv("diabetes.csv", index_col='Age')
print(df.describe()) # it shows--> count,mean,std,min,25%,50%,75%,max of all data.

df_head = df.head()
print(df_head) #it shows only first 5 data from all data


print(df_head.groupby('HighBP').sum()) #sum for individual value

print(df_head.groupby('HighBP').mean()) #mean for individual value

print(df_head['CholCheck'].value_counts()) # how many types of number & how many number in same type in a column CholChek,it shows

print(df_head['Education']) # finding single column

df_head.sort_values('Income',ascending=True, inplace= True) # inplace = True means it change the main data set. and inplace false means ,it do not change the main dataset.it returns a new data set that sort in_order to Income.
# print(df_head)


# -------------------------------> Data Cleaning dropna(),fillna() <--------------------------------
"""  
dropna()--> it found NaN in any coloumn, dropna drop the coloumn.
fillna()--> if found NaN in any row, fillna will fill the place with any number.
"""

print(df_head.dropna())
print(df_head.fillna(0))
