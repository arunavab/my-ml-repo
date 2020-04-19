from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# Reading Data from the iris csv file
iris = pd.read_csv("C:\Arunava\MyPythonProjects\Records\iris.csv")
print(iris.head())
x = np.arange(1, 11)
y = 2*x
y1 = 3*x
y2 = 5*x
# Plotting a line graph
plt.plot(x, y, color="green", linewidth=1.5, linestyle=":")
plt.plot(x, y1, color="orange", linewidth=1.5, linestyle=":")
plt.plot(x, y2, color="blue", linewidth=1.5, linestyle=":")
# Inserting names, labels in the graph
plt.title("Line Plot Sample")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
plt.grid("true")
student = {"Tony": 50, "Steve": 90, "Thor": 250}
names = list(student.keys())
marks = list(student.values())
# Plotting a Bar graph
plt.bar(names, marks, color="green", linewidth=25)
plt.title("Marks Distribution of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
x = np.random.randint(1, 100, 50)
y = np.random.randint(1, 100, 50)
y1 = np.random.randint(1, 100, 50)
# Plotting a scatter point graph
plt.scatter(x, y)
plt.scatter(x, y1, color="red")
plt.grid(1)
plt.show()
# Plotting a histogram
plt.hist(iris["sepal.length"], bins=20)
plt.show()
plt.interactive("False")
iris.boxplot(column="sepal.length", by="variety")
age = [35, 47, 72, 21, 53]
names = {"Arum", "Barun", "Kiran", "Mala", "Goja"}
plt.pie(age, labels=names, autopct="0.2%%")
plt.show()