import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# display scatterplot and correlation coefficient r of a dataset about
# gestation and longevity to see the relationship of the two.

# get data from excel
# convert into dataframe
# convert into numpy arrays
# create a scatterplot using plt

df = pd.read_excel(r"C:\Users\user\Downloads\animals.xls")
print("[show first couple of dataset]")
print(df.head())

array = df.iloc[:, [1, 2]].to_numpy()
print("[show first couple of dataset]")
print(array[:3, :2])

x = array[:, 0]
y = array[:, 1]

plt.scatter(x, y)
plt.xlabel("gestation")
plt.ylabel("longevity")
plt.show()

# correlation coefficient = (covariance of x and y) / (std of x)(std of y)
r = np.corrcoef(x, y)[0, 1]
# selecting x_01 is necessary because np.correcof results in correlation coefficient matrix.


print(np.max(x))
print(np.max(y))

print(np.where(x == 645))

new_array = np.delete(array, 14, 0)

x = new_array[:, 0]
y = new_array[:, 1]

plt.scatter(x, y)
plt.xlabel("gestation")
plt.ylabel("longevity")
plt.show()
new_r = np.corrcoef(x, y)[0, 1]
print(f"correlation coefficient = {r:.3}")
print(f"new correlation coefficient = {new_r:.3}")


