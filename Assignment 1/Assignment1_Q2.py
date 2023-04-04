#python program to read the given data.csv file(file is attached in mail) and perform the following
# Print the dataset.
# Print only the first 5 rows in the data.
# Remove the NULL values in the data.
# Analyze the data and find out count, Mean, Std, Min, Max, 25th percentile, 50th percentile, 75th percentile.


import pandas as pd #code to import pandas as name pd

#pandas module command to read  csv file
dataset = pd.read_csv("data.csv")

#command to print csv file
print(dataset)

#command to get first five rows of csv file we use .head() 
first_five =  dataset.head(5)

#command to print five rows
print(first_five)

#command to clean the data and to remove null values 
dataset.dropna(axis=0,inplace=True)

#code to print the dataset after cleaning 
print(dataset)

#command to describe the count,Mean,std,Min,25%,50%,75%,Max of the dataset
Data_Analysis = dataset.describe()

#command to print the Data_Analysis of the dataset
print(Data_Analysis)
