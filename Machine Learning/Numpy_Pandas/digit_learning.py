from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix


digits = load_digits()
# print(digits.data.size)
# print(dir(digits))
# print(digits.data[0])

""" plt.gray()
for i in range(0,3):
    plt.matshow(digits.images[i]) 
    plt.show()
     
 """

X = digits.data
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)

# print(X_train.shape)
# print(X_test)
model = LogisticRegression()
model.fit(X_train,y_train)
""" 
#Manual spot testing
print()
print()
print('target value of this test', digits.target[1709])

result = model.predict([digits.data[1709]])
print('test result',result) 
"""

accuracy = model.score(X_test,y_test)
# print('Model accuracy',accuracy)
y_predicted = model.predict(X_test)
confusion = confusion_matrix(y_test,y_predicted)
# print(confusion)
plot_confusion_matrix(model,X_test,y_test)
plt.show()