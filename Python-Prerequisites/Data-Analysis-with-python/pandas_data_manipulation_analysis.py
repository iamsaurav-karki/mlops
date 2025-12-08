'''
Data Manipulation and Analysis is a key taks in data science and pandas library in Python
provides powerful tools to handle and analyze data efficiently.
This code demonstrates various data manipulation techniques using pandas DataFrame.

'''
import pandas as pd
df = pd.read_csv('/home/skarki/mlops-learn/Python-Prerequisites/Data-Analysis-with-python/sample.csv')  # Reading data from CSV files

# Fetch the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head(5))
print(df.tail(5))  # Fetch the last 5 rows of the DataFrame

# DataFrame Information
print("\nDataFrame Information:")
print(df.info())
print("\nDataFrame Description (Statistical Summary):")
print(df.describe())

print(df.dtypes)  # Display data types of each column

# Handling Missing Values 
df.isnull().sum()  # Check for missing values in each column
df.fillna(method='ffill', inplace=True)  # Fill missing values using forward fill
df.dropna(inplace=True)  # Drop rows with missing values
print("\nDataFrame after handling missing values:")
print(df)

# Renaming Columns
df.rename(columns={'name': 'Full_Name', 'age': 'Age_in_Years'}, inplace=True)
print("\nDataFrame after renaming columns:")
print(df)

# Converting Salary to float 
df['salary'] = df['salary'].astype(float)
print("\nDataFrame after converting 'salary' to float:")
print(df)

# Sorting DataFrame by Age
df.sort_values(by='Age_in_Years', ascending=True, inplace=True)
print("\nDataFrame sorted by 'Age_in_Years':")
print(df)

# Adding new column New_value as double of salary
df['New_value'] = df['salary'] * 2
print("\nDataFrame after adding 'New_value' column:")
print(df)

# Data Aggregating and Grouping 

grouped_df = df.groupby('Age_in_Years').agg({'salary': 'mean', 'New_value': 'sum'})
print("\nGrouped DataFrame by 'Age_in_Years':")
print(grouped_df)

grouped_sum = df.groupby(['Age_in_Years', 'Full_Name']).agg({'salary': 'sum'})
print("\nGrouped DataFrame by 'Age_in_Years' and 'Full_Name':")
print(grouped_sum)

# Merging and Joining DataFrames
data1 = {
    'ID': [1, 2, 3],
    'Department': ['HR', 'Finance', 'IT']
}
data2 = {
    'ID': [1, 2, 4],
    'Location': ['New York', 'Chicago', 'San Francisco']
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(df2)
merged_df = pd.merge(df1, df2, on='ID', how='inner')  # Inner join
print("\nMerged DataFrame (Inner Join):")
print(merged_df)

merged_df = pd.merge(df1, df2, on='ID', how='outer')  # Outer join
print("\nMerged DataFrame (Outer Join):")
print(merged_df)

merged_df = pd.merge(df1, df2, on='ID', how='left')  # Left join
print("\nMerged DataFrame (Left Join):")
print(merged_df)

merged_df = pd.merge(df1, df2, on='ID', how='right')  # Right join
print("\nMerged DataFrame (RIght Join):")
print(merged_df)