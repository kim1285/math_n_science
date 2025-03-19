import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = r"C:\Users\user\Downloads\body_image.xls"
df = pd.read_excel(path)
print(df.head())
# I need 2nd and 3rd columns
array = df[['GPA','HS GPA']].to_numpy()
print(array.shape)

# I need to remove the empty values, asterisks
# if any  value of a row is asterisk, remove that row
row_to_remove = []
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        if array[i][j] == "*":
            row_to_remove.append(i)
row_to_remove = list(set(row_to_remove))
print(row_to_remove)

new_array = np.delete(array, row_to_remove, axis=0)  # now there is no missing values.
print()
print(new_array)
x = new_array[:, 1]
y = new_array[:, 0]

plt.scatter(x, y, color='blue')
plt.ylabel("college gpa")
plt.xlabel("high school gpa")
plt.title("scatter plot of high school and college gpa")
plt.show()

# now find the