import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv('/census.csv')

# Rename columns for better readability
df.columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
    'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
    'hours-per-week', 'native-country', 'income'
]

# Clean trailing whitespaces in 'sex' column
df['sex'] = df['sex'].str.strip()

# 1. Unique ages in dataset
print("Unique ages in the dataset:")
print(df['age'].unique())

# 2. Count of each gender
print("\nGender distribution:")
print(df['sex'].value_counts())

# 3. Count of each race
print("\nNumber of people of each race:")
print(df['race'].value_counts())

# 4. Average age of men
male_subset = df[df['sex'] == 'Male'][['sex', 'age']]
average_age_men = male_subset['age'].mean()
print("\nAverage age of men: {:.1f}".format(average_age_men))

# 5. Percentage of people with a Bachelor's degree
bachelors_df = df[df['education'].str.strip() == 'Bachelors']
percentage_bachelors = (bachelors_df.shape[0] / df.shape[0]) * 100
print("\nPercentage with Bachelors degrees: {:.1f}%".format(percentage_bachelors))

# 6. Percentage of people with advanced education earning >50K
adv_edu = ['Bachelors', 'Masters', 'Doctorate']
adv_grads = df[df['education'].str.strip().isin(adv_edu)]
high_earners_adv = (adv_grads['income'].str.strip() == '>50K').sum()
percentage_high_adv = (high_earners_adv / adv_grads.shape[0]) * 100
print("\nPercentage with advanced education earning >50K: {:.1f}%".format(percentage_high_adv))

# 7. Percentage of people without advanced education earning >50K
non_adv_grads = df[~df['education'].str.strip().isin(adv_edu)]
high_earners_non_adv = (non_adv_grads['income'].str.strip() == '>50K').sum()
percentage_high_non_adv = (high_earners_non_adv / non_adv_grads.shape[0]) * 100
print("Percentage without advanced education earning >50K: {:.1f}%".format(percentage_high_non_adv))

# 8. Minimum hours worked per week
min_hrs = df['hours-per-week'].min()
print("\nMinimum hours worked per week:", min_hrs)

# 9. Percentage of people working minimum hours who earn >50K
df_min_hrs = df[df['hours-per-week'] == min_hrs]
min_hrs_high_earners = (df_min_hrs['income'].str.strip() == '>50K').sum()
percentage_min_hrs_rich = (min_hrs_high_earners / df_min_hrs.shape[0]) * 100
print("Percentage of rich among those who work fewest hours: {:.1f}%".format(percentage_min_hrs_rich))

# 10. Country with highest percentage of high earners
rich = df[df['income'].str.strip() == '>50K']
rich_by_country = rich['native-country'].value_counts()
top_country = rich_by_country.idxmax()
top_country_count = rich_by_country.max()
print("\nCountry with highest number of people earning >50K:", top_country)
print("Number of high earners in that country:", top_country_count)

# 11. Most popular occupation for those who earn >50K in India
rich_indians = rich[rich['native-country'].str.strip() == 'India']
top_occupation_india = rich_indians['occupation'].value_counts().idxmax()
print("\nMost popular occupation for >50K earners in India:", top_occupation_india)
