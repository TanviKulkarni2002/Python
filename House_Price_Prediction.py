# Using Multiple Linear Regression we will predict the price of a house based on its area.
from sklearn.datasets import fetch_california_housing
housing=fetch_california_housing()
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Initalisin a dataframe to handle the data
data=pd.DataFrame(housing.data)
data.columns=housing.feature_names

X=data
Y=housing.target #Median house price in California 

#Splitting data into train and test sets
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30)

#Standardize the dataset: only standardize input variables, never do standardization for output variables.
scaler=StandardScaler()
scaler.fit_transform(X_train) #fit_transform the training dataset
scaler.transform(X_test) #transform the test dataset
#fit_transform is used to transform/standardize/normalize the data to a form which is well suited for you model.
#transfrom is used to just standardize/normalize/transfrom the data.

#Defining linear regression object
reg=LinearRegression().fit(X_train,Y_train)

#Using cross validation: method to estimate the performance and accuracy o ML models
mse=cross_val_score(reg,X_train,Y_train,scoring='neg_mean_squared_error',cv=5)
#cv=Number of different data training accuracies (should be as low as possible)
mse=np.mean(mse) #(should be as low as possible)
#The above is the difference in the predicted and the original values of the target entity

#Now we will make redictions for out test datset (X_test)
Y_pred=reg.predict(X_test)
print(Y_pred)

#Visualize the Y_predicted and the Y_test in plot to undertsand how much offsets we have in predicted values.
g=sns.displot(Y_pred-Y_test,kind='kde')
plt.show()