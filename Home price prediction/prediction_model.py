#Step 1: Import Libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

#Step 2: Load dataset
df = pd.read_csv("homeprices_singlevariable_linear_regression.csv")
print(df.head())

#Step 3: Check statistics of dataset
# #shape of dataset
# print(df.shape)
# #check the missing values
# print(df.isnull().sum())
# #describe()
# print(df.describe())


#Step 4:Split dataset into X(input and Y axis)
# X = df['area'] #Input
# X = df.iloc[:,:-1]
X = df.drop(columns=['price'], axis=1)
y = df.price
print(y)

#Step 5: split the dataset into training and testin(SKIP, B'coz My dataset it small)

#Step  6:Call Model and Train the model
model = LinearRegression()
#train the model
model.fit(X,y)

#Step 7: prediction
pred = model.predict([[3666]])
print(f"The price of Home is {pred.item()}")

#To find coefficient
print(model.coef_)#135.78767123
#To find y-intercept
print(model.intercept_)#180616.43835616432

#y = mx + c
y = 135.78767123 * 3666 + 180616.43835616432
print(y)