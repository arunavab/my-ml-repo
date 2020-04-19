import pandas as pd
# Series
# UnIndexed Series
s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)
# Indexed Series
s3 = pd.Series([3, 5, 7, 11, 35, 69], index=["aPon", "b_@pon", "c0uki", "Capon", "Oal", "Dol"])
print(s3)
# Series from Pre-defined key-pair values. First is the key and Second is the value.
d1 = {"k1": 10, "k2": 20, "k3": 30}
s5 = pd.Series(d1)
print(s5)
# Date_Frames
# Creating a DataFrame of Student names and Marks obtained.
studentData = ({"Student": ["Tony", "Steve", "Bruce", "Clint", "Natasha"], "Marks": [90, 45, 89, 55, 70]})
dfStudent = pd.DataFrame(studentData)
print(dfStudent)
# Creating a DataFrame from a csv file.
iris = pd.read_csv("C:\Arunava\MyPythonProjects\Records\iris.csv")
# To get the list of first items use DataFrame.head(n) function. Default is 5 for more type in number in n.
print(iris.head())
# To get the list of last items use DataFrame.tail(n) function. Default is 5 for more type in number in n.
print(iris.tail())
# To get basic understanding about the different features of the data use describe function.
print(iris.describe())