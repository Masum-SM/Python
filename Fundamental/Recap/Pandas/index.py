
import pandas as pt

df = pt.read_csv("diabetes.csv", index_col='Age')
print(df.describe()) # it shows--> count,mean,std,min,25%,50%,75%,max of all data.
