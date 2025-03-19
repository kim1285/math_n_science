# get data from excel
# convert it into arrays
# display using sctterplot
# calculate the linear equation using least square method and also display it in the scatterplot


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = r"C:\Users\user\Downloads\olympics.xls"

df = pd.read_excel(path)
print(df.head())
array = df.to_numpy()
print(array.shape)
print(array[:2][:])

x = array[:, 0].reshape(-1)  # year
y = array[:, 1].reshape(-1)  # time
print()
print(x)
plt.scatter(x, y, color='blue', label='datapoints')


# formula for least squares in linear regression.
# for y = ax + b,
# a(slope) = r * (str_y / str_x)
# b(intercept) = mean_y - a * mean_x

# calculate correlation coefficient r
r = np.corrcoef(x, y)[0][1]
str_y = np.std(y)
str_x = np.std(x)
mean_y = np.mean(y)
mean_x = np.mean(x)
a = r * (str_y / str_x)
b = mean_y - a * mean_x

# x_i = np.arange(1896, 2001, 1).reshape(1, -1)

y_line = a * x + b

plt.plot(x, y_line, color='red', label=f'prediction = {y_line}')
plt.xlabel("year")
plt.ylabel("time in seconds")
plt.title("finishing time of runnning on olympics")
plt.show()

# find the outlier manually
print(x.shape)
print(y.shape)
y_max = np.max(y)
index_of_outlier = np.where(y == y_max)
print(index_of_outlier)
print(y[index_of_outlier])
print(x[index_of_outlier])

# remove the outlier and try again the scatterplot and least square,
# and compare the result.

new_x = x[1:]
new_y = y[1:]

print(new_x.shape)
print(new_y.shape)

plt.scatter(new_x, new_y, color='blue', label='datapoints')

new_r = np.corrcoef(new_x, new_y)[0][1]
new_str_y = np.std(new_y)
new_str_x = np.std(new_x)
new_mean_y = np.mean(new_y)
new_mean_x = np.mean(new_x)
new_a = new_r * (new_str_y / new_str_x)
new_b = new_mean_y - new_a * new_mean_x

new_y_line = new_a * new_x + new_b
plt.plot(new_x, new_y_line, color='red', label=f'new_prediction = {new_y_line}')
plt.xlabel("year")
plt.ylabel("time in seconds")
plt.title("finishing time of runnning on olympics")
plt.show()
print(f"prediction with outlier: y = {a:.2f}x + {b:.2f}")
print(f"prediction without outlier: y = {new_a:.2f}x + {new_b:.2f}")
