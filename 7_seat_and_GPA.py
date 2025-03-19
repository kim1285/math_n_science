import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r"C:\Users\user\Downloads\body_image.xls")
seat = df["Seat"].to_numpy()
GPA = df["GPA"].to_numpy()
print(seat)
print(GPA)

# handing missing data by replacing them with mean
GPA[GPA == "*"] = 0
GPA_mean = np.mean(GPA)
GPA[GPA == 0] = GPA_mean
GPAs = [[], [], []]
for i in range(len(seat)):  # seats are F, M, B
    if seat[i] == "F":
        GPAs[0].append(GPA[i])
    elif seat[i] == "M":
        GPAs[1].append(GPA[i])
    elif seat[i] == "B":
        GPAs[2].append(GPA[i])
print(len(GPAs[0]))
print(len(GPAs[1]))
print(len(GPAs[2]))  #236

print(len(GPA))  # check the total number of gpa and compare it with the sum of len(GPAs)[~]

plt.boxplot(GPAs)
plt.show()
# additionally report Q1, Q2, Q3, Q4, mean, min, max of each groups.