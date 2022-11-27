import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
data = pd.read_csv('HR_comma_sep.csv')

# Step 01 : checking missing data for any row and colomn
# print(data.isnull().values.any())

# Step 02: Check data type 
# print(data.dtypes)

#Step 03 : check unique values
# print(data.salary.unique())
# print(data.Department.unique())

clean_up_values = {
    "salary":{
        'low' : 1,
        'medium' : 2,
        'high' :3
    }
}
data.replace(clean_up_values, inplace=True)
# print(data.salary)

# step 4 : get dummies for the Department•
dummy_data = pd.get_dummies(data.Department)
# print(dummy_data)

# step 5 : merge dummies (dummy columns) with the original data

merged = pd.concat([data,dummy_data],axis='columns')
# print(merged)


# step 6 : Drop unnecessary columns
final_data = merged.drop(['Department','technical'],axis = 'columns')
# print('Department' in list(final_data))
# print('Department' in list(merged))
print(final_data.columns)

# step 7 : plot data set to see the data set
# plt.scatter(x = final_data.satisfaction_level,y = final_data.left)
plt.scatter(x = final_data.time_spend_company,y = final_data.left)
# plt.show()

# step 8 : draw model 
X = final_data.drop('left',axis='columns')
y = final_data.left
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train,y_train)
accuracy = model.score(X_test,y_test)
print(accuracy)