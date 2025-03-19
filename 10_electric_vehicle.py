import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_df = pd.read_csv(r"C:\0.Kangsan_Kim\My_programs\effort_game\effort_game"
                    r"\Data_analysis\dataset\Electric_Vehicle_Population_Data.csv")
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)


def s_to_df_sort(series, columns, column_to_sort_by, ascending):
    # accepts list of columns, Boolean on ascending sorting
    df_tmp = series.reset_index()
    df_tmp.columns = columns
    df_tmp = df_tmp.sort_values(by=column_to_sort_by, ascending=ascending)
    df_tmp = df_tmp.reset_index(drop=True)
    return df_tmp


def combine_df_except_top_n_rows(dataframe, n, category_column_name, column_name_to_add_rows):
    # accepts sorted dataframe with target columns to select 10 rows.
    # split df into top and bottom
    df_top = dataframe.loc[dataframe.index <= n]
    df_bottom = dataframe.loc[dataframe.index > n]

    # combine bottom rows
    bottom_sum = round(df_bottom[column_name_to_add_rows].sum(), 2)
    df_bottom = pd.DataFrame({category_column_name: ["Others"], column_name_to_add_rows: [bottom_sum]})

    # concatenate two dataframes vertically
    df_tmp = pd.concat([df_top, df_bottom])
    df_tmp = df_tmp.reset_index(drop=True)

    return df_tmp


def mean_df_except_top_n_rows(dataframe, n, category_column_name, column_name_to_add_rows):
    # accepts sorted dataframe with target columns to select 10 rows.
    # split df into top and bottom
    df_top = dataframe.loc[dataframe.index <= n]
    df_bottom = dataframe.loc[dataframe.index > n]

    # combine bottom rows
    bottom_sum = round(df_bottom[column_name_to_add_rows].mean(), 2)
    df_bottom = pd.DataFrame({category_column_name: ["Others"], column_name_to_add_rows: [bottom_sum]})

    # concatenate two dataframes vertically
    df_tmp = pd.concat([df_top, df_bottom])
    df_tmp = df_tmp.reset_index(drop=True)

    return df_tmp


# print(my_df)

# check for any missing values
# print(my_df.isnull().values.any())

# check for sum of missing value count per column
# print(my_df.isnull().sum())

# check the number of rows with any missing entries
# print(my_df[my_df.isnull().any(axis=1)])

# calculate the percentage of rows with missing entries
# print(round(my_df[my_df.isnull().any(axis=1)].shape[0]/(my_df.shape[0]), 6))

# remove all rows with missing entries
deleted_df = my_df.dropna()

# find the mean of all nonzero entries of columns and replace 0 with them.
range_mean = np.mean(deleted_df[deleted_df["Electric Range"] > 0]["Electric Range"])
df_a = deleted_df
df_a.loc[df_a["Electric Range"] == 0, ["Electric Range"]] = range_mean
"""
try:
    print(df_a.loc[:, ["Electric Range"]])
except:
    print("no values")
print("done")
"""


def pd_impute_column_mean(df, column_name):  # imputes 0 with mean of non-zero mean in a column in pandas
    # the mean of nonzero in a column
    col_mean = np.mean(df.loc[df[column_name] != 0, [column_name]])
    df_2 = df
    df_2.loc[df[column_name] == 0, [column_name]] = col_mean
    return df_2


df_2 = pd_impute_column_mean(deleted_df, "Electric Range")
df_3 = pd_impute_column_mean(df_2, "Base MSRP")


# columns with categorical variables:
categorical_columns = ["County", "City", "State", "Model Year", "Make",
                                 "Model", "Electric Vehicle Type",
                                 "Clean Alternative Fuel Vehicle (CAFV) Eligibility", "Electric Utility"]
numerical_columns = ["Electric Range", "Base MSRP"]

# Calculate distribution of categorical variables
categorical_distribution = {}
for i in categorical_columns:
    categorical_distribution[i] = df_3[i].value_counts()
# print("Categorical distribution")
# print(categorical_distribution)
# print("-" * 60)

# Calculate the distribution of numerical variables
numerical_distribution_mean = df_3.loc[:, numerical_columns].mean()
# print("numerical_distribution_mean")
# print(numerical_distribution_mean)
# print("-" * 60)

numerical_distribution_median = df_3.loc[:, numerical_columns].median()
# print("numerical_distribution_median")
# print("-" * 60)

numerical_distribution_max = df_3.loc[:, numerical_columns].max()
# print(numerical_distribution_max)
# print("-" * 60)

numerical_distribution_min = df_3.loc[:, numerical_columns].min()
# print("numerical_distribution_min")
# print("-" * 60)

numerical_distribution_std = df_3.loc[:, numerical_columns].std()
# print("numerical_distribution_std")
# print(numerical_distribution_std)
# print("-" * 60)

# pivot table for summary
# bin ranges into long, medium, short.
# expecting dataset to be left skewed. since it is skewed will use median.
# split into 3 groups using count and add additional column.
num_of_vehicles = df_3.shape[0]
# print("num_of_vehicles")
# print(num_of_vehicles)
# print("-" * 60)

range_indexing = sorted(df_3["Electric Range"], reverse=True)
long_value_index = round(num_of_vehicles * 0.33333)
medium_value_index = round(num_of_vehicles * 0.66666)
long_range_value = range_indexing[long_value_index]
medium_range_value = range_indexing[medium_value_index]
electric_ranges_tmp = df_3["Electric Range"]
binned_range_feature = []
for i in electric_ranges_tmp:
    if i >= long_range_value:
        binned_range_feature.append("long")
    elif long_range_value > i >= medium_range_value:
        binned_range_feature.append("medium")
    else:
        binned_range_feature.append("short")

# new feature_1
year_old = -(df_3["Model Year"] - 2025)
# new feature_2
df_4 = pd.DataFrame(
    {"Binned range": binned_range_feature,
     "Vehicle Age": year_old}
)

df_5 = pd.concat([df_3, df_4], axis=1)

# Summary using Pivot table
# average range and price by maker
df_6 = df_5.pivot(columns="Make", values="Electric Range").mean()

# EVs per state
# print("EVs per state")
# print(df_5["State"].value_counts())
# print("-" * 60)
# only Washington

# distribution of EV maker in washington
df_7 = df_5["Make"].value_counts() / (df_5.shape[0]) * 100

# distribution of EV ranges
df_8 = df_5["Binned range"].value_counts()

# distribution of EV ages
df_9 = df_5["Vehicle Age"].value_counts() / (df_5.shape[0]) * 100

# average price by maker
df_10 = df_5.pivot(columns="Make", values="Base MSRP").mean()
df_11 = df_10.sort_values(ascending=False)

# number of EV makers
df_13 = list(df_5["Make"].value_counts())
df_14 = len(df_13)

# number of EV models
df_15 = list(df_5["Model"].value_counts())
df_16 = len(df_15)

# most common EV model
df_17 = df_5["Model"].value_counts()


print("number of EVs on washington")
print(df_3.shape[0])
print("-" * 60)
print("number of EV models")
print(df_16)
print("-" * 60)
print("number of EV makers")
print(df_14)
print("-" * 60)
print("distribution of EV ranges")
print(df_8)
print("-" * 60)
print("Only washington EVs")
print("-" * 60)


# ev age pie, df_9
# combine others except top 3
# type:
# pandas.core.series.Series; result of value.counts()
# print(df_9)
ev_age_tmp = s_to_df_sort(df_9, ['Age', 'Percentage'], ['Percentage'], False)
ev_age_tmp = combine_df_except_top_n_rows(ev_age_tmp, 5, 'Age', 'Percentage')


# top 10 ev ranges by maker - ev6
# print(type(df_6))
# print(df_6)
my_df_tmp_4 = s_to_df_sort(df_6, ['Make', 'Range'], ['Range'], False)
my_df_tmp_4 = my_df_tmp_4[my_df_tmp_4.index <= 3]




# distribution of EV maker in washington - pie
# print(df_7)
# print(type(df_7))  # series (result of dataframe[column].value_counts

my_df_tmp_1 = s_to_df_sort(df_7, ['Make', 'Percentage'], ['Percentage'], False)
ev_distribution = combine_df_except_top_n_rows(my_df_tmp_1, 10, 'Make', 'Percentage')
# print(ev_distribution)


# Model counts - pie
# print(type(df_17))
# Series
# print(df_17)

my_df_tmp = s_to_df_sort(df_17, ['Model', 'Count'], ['Count'], False)
my_df_tmp = combine_df_except_top_n_rows(my_df_tmp, 10, 'Model', 'Count')


# "Age Distribution with Percentages"
ax1 = my_df_tmp_4.plot.bar(
    x="Make",
    y="Range",
    color='skyblue',  # Set color of the bars
    figsize=(10, 6),  # Set figure size
    legend=False,  # Turn off legend (not needed in this case)
    edgecolor='black'  # Add black edges to the bars for contrast
)
# Adding Title and Labels
plt.title("Top 4 average EV Ranges by Maker", fontsize=16, fontweight='bold')
plt.xlabel("Make", fontsize=12)
plt.ylabel("Range (miles)", fontsize=12)

# Customize x-axis ticks (rotate labels for better readability)
plt.xticks(rotation=45, ha='right')

# Optional: Add a grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()  # Adjust layout to ensure everything fits
plt.show()


ax = ev_age_tmp.plot.pie(
    y="Percentage",  # Values to plot
    labels=ev_age_tmp['Age'],  # Labels for each pie slice
    autopct='%1.1f%%',  # Display the percentage on each slice
    startangle=90,  # Rotate the pie chart to start at the top
    legend=False,  # Hide the legend
    figsize=(8, 8),  # Set the size of the plot
    colors=['#66b3ff', '#99ff99', '#ffb3e6', '#ff6666'],  # Set custom colors
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}  # Add border around the slices
)

# Add title to the chart
plt.title("Age Distribution with Percentages in Washington")

# Show the pie chart
plt.show()


# "Electric Vehicle ratio by Maker"
ax2 = ev_distribution.plot.pie(
    y="Percentage",  # Values to plot
    labels=ev_distribution['Make'],  # Labels for each pie slice
    autopct='%1.1f%%',  # Display the percentage on each slice
    startangle=90,  # Rotate the pie chart to start at the top
    legend=False,  # Hide the legend
    figsize=(8, 8),  # Set the size of the plot
    colors=['#66b3ff', '#99ff99', '#ffb3e6', '#ff6666'],  # Set custom colors
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}  # Add border around the slices
)
plt.title("Electric Vehicle Ratio by Maker in Washington")
plt.show()


# "Model popularity"
ax3 = my_df_tmp.plot.pie(
    y="Count",  # Values to plot
    labels=my_df_tmp['Model'],  # Labels for each pie slice
    autopct='%1.1f%%',  # Display the percentage on each slice
    startangle=90,  # Rotate the pie chart to start at the top
    legend=False,  # Hide the legend
    figsize=(8, 8),  # Set the size of the plot
    colors=['#66b3ff', '#99ff99', '#ffb3e6', '#ff6666'],  # Set custom colors
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}  # Add border around the slices
)
plt.title("EV Model Distribution in Washington")
plt.show()