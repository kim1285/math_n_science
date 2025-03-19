# row 0 = Gender, row 5 = WtFeel
# find the mode value of WtFeel among the rows also with Gender = Female
# find the mode value of WtFeel among the rows also with Gender = Male
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# This can be just done using pivot table in pandas better.

df = pd.read_excel(r"C:\Users\user\Downloads\body_image.xls")
print(df.shape)

gender = df["Gender"].to_numpy().reshape(-1, 1)
WtFeel = df["WtFeel"].to_numpy().reshape(-1, 1)

matrix_1 = np.column_stack((gender, WtFeel))
print(matrix_1)
print(type(matrix_1))
# values, counts = np.unique(matrix_1, return_counts=True)
# print(values)
# print(counts)

element_list = set((type(element) for element in matrix_1[:, 1]))
# checking the types of entries in WtFeel column or column 1.
print(element_list)

my_list = [0, 0, 0, 0]
# AboutRt, OverWt, nan, UnderWt

for element in matrix_1[:, 1]:
    if element == "AboutRt":
        my_list[0] += 1
    elif element == "OverWt":
        my_list[1] += 1
    elif element == "nan":
        my_list[2] += 1
    elif element == "UnderWt":
        my_list[3] += 1
print(my_list)
mode_i = np.argmax(my_list)

matrix_1[matrix_1 == "nan"] = "AboutRt"  # missing value is assigned mode value "AboutRt".

# now creating two-way table.
column_1 = matrix_1[:, 0]
column_2 = matrix_1[:, 1]

table = pd.crosstab(column_1, column_2)
print(table)

table_percentage = table.div(table.sum(axis=1), axis=0) * 100

print("Crosstab (Percentage Table):")
print(table_percentage)

