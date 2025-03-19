import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# This script
# The "randomly" preselected  is business


df = pd.read_excel(r"C:\Users\user\Downloads\student_survey.xls")
print(df.head)


# Data preprocessing: imputation of missing data with mean on Verbal column.
scores = []

# Get mean of SAT verval score except missing values
# check the datatype of entries
print("datatype:")
print(type(df["Verbal"][0]))
print("value:")
print(df["Verbal"][0])


print("datatype:")
print(type(df["Verbal"][1128]))
print("value:")
print(df["Verbal"][1128])

for score in df["Verbal"]:
    if isinstance(score, int):
        scores.append(score)

# calculate mean of values.
verbal_m = round(np.mean(scores), 2)
print(f"mean of verbal score: {verbal_m}")

# impute missing value with mean.
# if the value == str then replace those value with mean value.
# options? 1. function in pandas, 2. function in numpy, 3. custom function.
# 1.
pd.set_option('future.no_silent_downcasting', True)
df_new = df.replace("*", verbal_m,)
print(df_new.head)

# calculate the distribution of variables for total population and business population
# handedness: left or right
# sex: male and female
# since age is right skewed, use median to compare. 0.5 years difference is documented
# for score, use mean as it follows roughly normal distribution. 10 point difference is documented.


# total distribution calculation
# counting sex and handedness: options? 1. loop, 2. vectorization using numpy if 2,
# then converting portion of df into np is needed.
# loop has less overhead.

# count of male.
total_sex_count = 0


counter = 0
for i in df["Sex"]:
    if i == "male":
        total_sex_count += 1
    else:
        pass
    counter += 1
if counter == 1129:
    print("the sex has been all counted.")
else:
    print("the sex has not all been counted.")

print(f"total_sex_count: {total_sex_count}")

# count of handedness.
# right handedness
total_hand_count = 0
counter = 0
for i in df["Handed"]:
    if i == "right":
        total_hand_count += 1
    else:
        pass
    counter += 1
if counter == 1129:
    print("the handedness has been all counted.")
else:
    print("the handedness has not all been counted.")

tmp_age = tuple(df_new["Age"])

data_types = []
i_of_non_ints = []
for count, i in enumerate(tmp_age):
    data_types.append(type(i))
    if isinstance(i, str):
        i_of_non_ints.append(count)

# check the datatypes of entries
data_types = set(data_types)
print(data_types)
print(i_of_non_ints)

# calculate the median of total age:
total_age_median = np.median(df_new["Age"])
print(total_age_median)

# calculate the mean of score:
total_score_mean = round(np.mean(df_new["Verbal"]),2)
print(total_score_mean)


# distribution of variables on business majors.
# options: 1. create a new df or np.array where course column value is business, and then do the same;
# 2. on the original df, use conditions to select needed values. try option 2 because may be more efficient.

# handedness of business major:
# count only if the major is business and handedness is right.
business_hand = 0  # right handedness.
for i in range(len(df_new["Course"])):
    if df_new["Course"][i] == "Business" and df_new["Handed"][i] == "right":
        business_hand += 1
    else:
        pass
print(business_hand)

# test if the condition is correct:
if not df_new["Course"][4] == "Business" and df_new["Handed"][4] == "right":
    print("the condition is correct")
else:
    print("the condition is incorrect")

# sex of business major:
# male
business_sex = 0
for i in range(len(df_new['Sex'])):
    if df_new["Course"][i] == "Business" and df_new["Sex"][i] == "male":
        business_sex += 1
    else:
        pass
print(business_sex)


# mean of verbal score of business majors
business_verbal = []
for i in range(len(df_new['Verbal'])):
    if df_new['Course'][i] == "Business":
        business_verbal.append(df_new['Verbal'][i])
    else:
        pass
business_verbal_mean = round(np.mean(business_verbal), 2)
print(business_verbal_mean)

# median of business majors
business_age_median = []
for i in range(len(df_new['Age'])):
    if df_new['Course'][i] == "Business":
        business_age_median.append(df_new["Age"][i])

business_age_median = round(np.median(business_age_median), 2)
print(business_age_median)


# Compare the distribution of values in total and business major.

# handedness_total
total_student_count = len(df_new["Handed"])
print(total_student_count)
print(total_hand_count)

total_handedness_comp_list = [total_hand_count, (total_student_count - total_hand_count)]
print(f"total handedness list: {total_handedness_comp_list}")
# handedness_business
business_student_count = 0
for i in df_new["Course"]:
    if i == "Business":
        business_student_count += 1
    else:
        pass

business_handedness_comp_list = [business_hand, (business_student_count - business_hand)]


# total_sex
total_sex_comp_list = [total_sex_count, (total_student_count - total_hand_count)]
print(f"total sex list: {total_sex_comp_list}")

# business_sex
business_sex_comp_list = [business_sex, (business_student_count - business_sex)]
print(f"business sex list: {business_sex_comp_list}")

# total verbal
print(f"total verbal mean: {verbal_m}")

# business verbal
print(f"business verbal mean: {business_verbal_mean}")

# total_age
print(f"total age median: {total_age_median}")

# business_age
print(f"total age median: {business_age_median}")

