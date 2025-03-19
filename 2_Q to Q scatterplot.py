import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel(r"C:\Users\user\Downloads\height.xls")


# reshape into (-1, 3)
# assign variable
# show

array = df.to_numpy().reshape(-1, 3)
print(array)
# x_i1 = gender
# x_i2 = weight
# x_i3 = height
c = array[:, 0]  # gender
x = array[:, 1]  # weight
y = array[:, 2]  # height

# I do not know how to make x into color variables on scatterplot.
plt.scatter(x, y, c=c, cmap='viridis', s=100, alpha=0.7)
plt.xlabel("weight")
plt.ylabel("height")
plt.title('Scatter Plot of Height, Weight and gender')
plt.show()