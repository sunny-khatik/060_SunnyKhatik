

# importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data reading from file.
main_data = pd.read_csv('Data_for_Transformation.csv')

# 1st plot : scatter plot between age and salary.
print(main_data)
plt.scatter(main_data["Age"], main_data["Salary"])
plt.show()

# 2nd plot : salary Histogram
plt.hist(main_data["Salary"], bins=10, color="yellow")
plt.show()

# 3rd plot : country vs salarey
fig_size = plt.figure(figsize=(7, 5))
plt.bar(main_data["Country"], main_data["Salary"], color="green")
plt.xlabel("Salaries")
plt.ylabel("Countries")
plt.title("Bar chart of country vs salary")
plt.show()
