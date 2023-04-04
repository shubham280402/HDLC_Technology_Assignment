#python code to create the following table of data using 
#dataframe and count the number of rows and colums

import pandas as pd  #code to import pandas module

# Python dictionary 
d = {'COl-1': [10,20,30],
     'COl-2': [40,50,60],
     'COl-3': [70,80,90], 
     'COl-4': [100,110,120]
     }

#code to print the table using pandas 
df = pd.DataFrame(data=d)

print(df)

#shape[0] command to get the value no of rows
count_row = df.shape[0]

#shape[1] command to get the value no of column
count_column = df.shape[1]


print("The number of rows:",count_row)

print("The number of columns:",count_column)