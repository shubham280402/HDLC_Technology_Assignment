# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Reading the csv file into a pandas dataframe
df = pd.read_csv('windpower.csv')

# Printing the top 10 rows
print(df.head(10))

# Printing the bottom 5 rows
print(df.tail(5))

# Displaying the structure of dataset with datatypes
print(df.info())

# Finding Mean, Standard deviation, Min, Max for the column wind speed
wind_speed_stats = df['wind speed'].describe()[['mean', 'std', 'min', 'max']]
print('Wind Speed Statistics:\n', wind_speed_stats)

# Filling the NULL values with the average value of that column
df['wind speed'].fillna(df['wind speed'].mean(), inplace=True)

# Creating a histogram plot for the column wind speed
plt.hist(df['wind speed'], bins=20)
plt.xlabel('Wind Speed')
plt.ylabel('Frequency')
plt.title('Wind Speed Distribution')
plt.show()

# Creating scatter plot between windspeed and Theoretical power curve
plt.scatter(df['wind speed'], df['Theoretical_Power_Curve'], alpha=0.5)
plt.xlabel('Wind Speed')
plt.ylabel('Theoretical Power Curve')
plt.title('Scatter plot of Wind Speed vs Theoretical Power Curve')
plt.show()

# Displaying the rows where windspeed < 5
print(df[df['wind speed'] < 5])

# Extracting the rows where wind direction > 200
print(df[df['wind direction'] > 200])