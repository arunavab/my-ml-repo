# A basic analysis of the iris DataSet using pandas
import pandas as pd
iris = pd.read_csv("C:\Arunava\MyPythonProjects\Records\iris.csv")
print(iris)
# Reading the first and last sections of the data frame
print(iris.head())
print(iris.tail())
# Describing the data
print(iris.describe())
# Breaking DataSet based on conditions
# Filtering out the data where petal width is > 1.5
irisPL = iris[(iris['petal.length'] > 1.5)]
print(irisPL)
# Filtering based on more conditions
iris_complex = iris[((iris['petal.length'] > 1.5) | (iris['petal.length'] < 3)) & (iris['variety'] == "Virginica")]
print(iris_complex)
# Breaking data into train and test data
print("IRIS TRAIN DATA")
iris_train = iris.head(60)
print(iris_train)
print("IRIS TEST DATA")
iris_test = iris.tail(90)
print(iris_test)