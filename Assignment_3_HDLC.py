# ASSIGNMENT NO.3 
#ASSIGNMENT DONE BY SHUBHAM SONI

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("insurance.csv")

print(df)

# Remove the rows which have NULL values
new_df = df.dropna(inplace=True)
print(new_df)


# Fill empty cells in the "charges" column with Mean, Median, and Mode
mean = df['charges'].mean()
median = df['charges'].median()
mode = df['charges'].mode().values[0]

df['charges'].fillna(mean, inplace=True)  # Fill with Mean
df['charges'].fillna(median, inplace=True)  # Fill with Median
df['charges'].fillna(mode, inplace=True)  # Fill with Mode

# Replace values greater than 60 in the "age" column with 50
df.loc[df['age'] > 60, 'age'] = 50

# Remove duplicates
df.drop_duplicates(inplace=True)

# Find the correlation between the columns
corr = df.corr()

# Draw a scatter plot between "age" and "bmi"
df.plot.scatter(x='age', y='bmi')
plt.show()

# Draw a histogram plot on "age" column
df['age'].plot.hist(bins=20)
