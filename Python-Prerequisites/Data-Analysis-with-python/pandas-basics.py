# Pandas is a powerful data manipulation library in Python. It provides data structures like Series and DataFrame
# that make it easy to handle and analyze structured data.

import pandas as pd
import numpy as np

# Creating a Series - it is a one dimensional array-like object that can hold any data type. It is similar to a column in a table.
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Pandas Series:")
print(series)


# Creating a series from dictionary
data_dict = {'a': 100, 'b': 200, 'c': 300}
series_dict = pd.Series(data_dict)
print("\nPandas Series from Dictionary:")
print(series_dict)

data2 = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
output_series = pd.Series(data2, index=index)
print("\nPandas Series with Custom Index:")
print(output_series)

# DataFrame - it is a two dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).
# Create a DataFrame from a dictionary of lists
data_dataframe = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data_dataframe)
print("\nPandas DataFrame:")
print(df)
print(type(df))

numpy_arr_value = np.array(df)  # Converting DataFrame to Numpy Array 
print("\nDataFrame converted to Numpy Array:")
print(numpy_arr_value)

# Create a DataFrame from a list of dictionaries
data_list_of_dicts = [
    {'Name': 'David', 'Age': 28, 'City': 'Miami'},
    {'Name': 'Eva', 'Age': 22, 'City': 'Seattle'},
    {'Name': 'Frank', 'Age': 33, 'City': 'Boston'}
]
df_list_of_dicts = pd.DataFrame(data_list_of_dicts)     
print("\nPandas DataFrame from List of Dictionaries:")
print(df_list_of_dicts)


df = pd.read_csv('/home/skarki/mlops-learn/Python-Prerequisites/Data-Analysis-with-python/sample.csv')  # Reading data from CSV files
print("\nDataFrame from CSV file:")
print(df.head(7))  # Display first few rows of the DataFrame

# Accessing Data from DataFrame
print("\nAccessing 'Name' column:") 
print(df_list_of_dicts['Name'])  # Accessing a single column
print("\nAccessing 'Age' and 'City' columns:")
print(df_list_of_dicts[['Age', 'City']])  # Accessing multiple columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
print("\nAccessing first 3 rows:")
print(df_list_of_dicts.iloc[0:3])  # Accessing rows by index
print("\nAccessing rows where Age > 30:")
print(df_list_of_dicts[df_list_of_dicts['Age'] > 30])  # Filtering rows based on a condition    


# Accessing a specified element 
print("\nAccessing 'Name' column again:")
print(df_list_of_dicts['Name'])
print(df_list_of_dicts.at[1, 'Name'])  # Output: Eva


# Accessing a specified element using iloc
print("\nAccessing element at row index 2 and column index 0:")
print(df_list_of_dicts.iloc[2, 0])  # Output: Frank ( giving both row index and column index)

# Data Manipulation with DataFrame
# Adding a new column
df_list_of_dicts['Salary'] = [50000, 60000, 70000]
print("\nDataFrame after adding 'Salary' column:")
print(df_list_of_dicts)

# Modifying an existing column
df_list_of_dicts['Age'] = df_list_of_dicts['Age'] + 1
print("\nDataFrame after modifying 'Age' column:")
print(df_list_of_dicts)

# Deleting a column
df_list_of_dicts.drop('City', axis=1, inplace=True) # axis=1 indicates we are dropping a column, drop is temporalily unless inplace = True
print("\nDataFrame after deleting 'City' column:")
print(df_list_of_dicts)

# Dispalying data types of each column
print("\nData types of each column in the DataFrame:")
print(df_list_of_dicts.dtypes)

# Describe the DataFrame 
print("\nStatistical Summary of the DataFrame:")
print(df_list_of_dicts.describe())  
