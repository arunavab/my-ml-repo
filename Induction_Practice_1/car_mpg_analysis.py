#Predicting the Price of Cars based on the different features
import pandas as pd
import numpy as np
import matplotlib as pt
import seaborn as sns
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 30)
mpg = pd.read_csv("C:\Arunava\MyPythonProjects\Records\\imports-85.data")
# mpg2 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data")
# Replace ? values with NaN
mpg["bore"] = mpg["bore"].replace({"?": np.nan})
mpg["stroke"] = mpg["stroke"].replace({"?": np.nan})
mpg["horsepower"] = mpg["horsepower"].replace({"?": np.nan})
mpg["peak-rpm"] = mpg["peak-rpm"].replace({"?": np.nan})
mpg["price"] = mpg["price"].replace({"?": np.nan})
# Changing the type of Columns to Float for calculation
mpg["bore"] = mpg["bore"].astype("float64")
mpg["stroke"] = mpg["stroke"].astype("float64")
mpg["horsepower"] = mpg["horsepower"].astype("float64")
mpg["peak-rpm"] = mpg["peak-rpm"].astype("float64")
mpg["price"] = mpg["price"].astype("float64")
# Replacing the columns with from string with numbers
mpg["num-of-cylinders"] = mpg["num-of-cylinders"].replace({"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "eight": 8, "ten": 10, "twelve": 12})
# Changing the type from String to Numbers for Cylinders
mpg["num-of-cylinders"] = mpg["num-of-cylinders"].astype("int64")
# Checking the data types of the columns of the Data Frame
print(mpg.dtypes)
# Replace all the ? with NaN
mpg = mpg.replace("?", np.nan)
print(mpg.head())
# Replacing the missing values with median values
mpg["bore"] = mpg["bore"].fillna(mpg["bore"].median())
mpg["stroke"] = mpg["stroke"].fillna(mpg["stroke"].median())
mpg["horsepower"] = mpg["horsepower"].fillna(mpg["horsepower"].median())
mpg["peak-rpm"] = mpg["peak-rpm"].fillna(mpg["peak-rpm"].median())
mpg["price"] = mpg["price"].fillna(mpg["price"].median())
print(mpg.head())
print(mpg.describe().transpose())
mpg_attr = mpg.iloc[:, 1:16]
print(mpg_attr)
#sns.pairplot(mpg_attr, diag_kind="KDE")
sns.pairplot(mpg, diag_kind="KDE")
