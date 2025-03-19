import numpy as np  # Import NumPy for array manipulation
import pandas as pd  # Import pandas for reading Excel files
import matplotlib.pyplot as plt  # Import matplotlib for plotting


"""
This is an example of Categorical variable to Categorical variable relationship analysis

Objectives:
This code processes an Excel file with light exposure and myopia data, 
calculates occurrences of specific conditions,
displays the data in a table plot, 
and computes the percentage of children with myopia for the "lamp" and "no light" conditions.
"""


# Read Excel file into pandas DataFrame
df = pd.read_excel(r"C:\Users\user\Downloads\nightlight (1).xls")


# Convert DataFrame to NumPy array for easier manipulation
df = df.to_numpy()


# Print the raw data
print(df)


# Conditional filtering (Define conditions based on the values in the first two columns of the array)
condition_1 = (df[:, 0] == "lamp") & (df[:, 1] == "Yes")
condition_2 = (df[:, 0] == "lamp") & (df[:, 1] == "No")
condition_3 = (df[:, 0] == "night light") & (df[:, 1] == "Yes")
condition_4 = (df[:, 0] == "night light") & (df[:, 1] == "No")
condition_5 = (df[:, 0] == "no light") & (df[:, 1] == "Yes")
condition_6 = (df[:, 0] == "no light") & (df[:, 1] == "No")


# Conditional mapping (List of condition names and their corresponding boolean condition arrays)
list_names = ["lamp_yes", "lamp_no", "night_light_yes", "night_light_no", "no_light_yes", "no_light_no"]
list_values = [condition_1, condition_2, condition_3, condition_4, condition_5, condition_6]


# Loop (Loop through conditions, count and print the occurrences of each condition)
for i in range(len(list_values)):
    print(f"{list_names[i]} = {np.sum(list_values[i])}")  # Count True values (occurrences) and print


# Matrix creation (Create a matrix of counts by summing the conditions and reshaping the array for a 2D table)
tmp_array = np.array([np.sum(list_values[i]) for i in range(len(list_values))]).reshape(-1, 2)
# column is myopia yes no.
print(tmp_array)  # Print the counts as a 2D array


# Define the table columns and rows labels
columns = ['myopia=Yes', 'my opia=No']  # Possible responses
rows = ['lamp', 'night light', "no light"]  # Types of light


# Table config (Create and configure a plot for displaying the table)
fig, ax = plt.subplots()  # Create a new figure and axis
ax.axis('tight')  # Adjust axis to fit content tightly
ax.axis('off')  # Turn off the axis visibility


# Table creation
table = ax.table(cellText=tmp_array, rowLabels=rows, colLabels=columns, loc='center')  # Place the table in the center
plt.show()  # Display the table plot


# Descriptive analysis of shown data
print(f"percentage of children among nolight, who developed miopia ="
      f" {(((tmp_array[2][0]) / (tmp_array[2][0] + tmp_array[2][1])) * 100):.2f}%")

print(f"percentage of children among lamp, who developed miopia ="
      f" {(((tmp_array[0][0]) / (tmp_array[0][0] + tmp_array[0][1])) * 100):.2f}%")
