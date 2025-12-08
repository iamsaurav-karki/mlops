import pandas as pd
from io import StringIO

Data = '{"employee_name":"John Doe","employee_age":30,"employee_salary":50000}\n{"employee_name":"Jane Smith","employee_age":25,"employee_salary":60000}\n{"employee_name":"Sam Brown","employee_age":28,"employee_salary":55000}'
df = pd.read_json(StringIO(Data), lines=True)
print("DataFrame from JSON data:")
print(df)

back_to_json = df.to_json()  # Convert DataFrame back to JSON format
print("\nDataFrame converted back to JSON format:")
print(back_to_json)

df.to_json('output.json', orient='records', lines=True)  # Save DataFrame to a JSON file
print("\nDataFrame saved to 'output.json' file.")

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)  # Reading data from URL

print("\nDataFrame from CSV URL:")
print(df.head())  # Display first few rows of the DataFrame

df.to_csv('wine.csv', index=False)  # Save DataFrame to a CSV file
print("\nDataFrame saved to 'output.csv' file.")

# Read data from html file 
url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
df = pd.read_html(url)  # This returns a list of DataFrames

print("\nDataFrames from HTML URL:")
print(df[0])  # 


another_url = 'https://en.wikipedia.org/wiki/Mobile_country_code'
headers = {
    "User-Agent": "Mozilla/5.0"
}
dfs = pd.read_html(another_url, match="Country", header=0, storage_options=headers)
print(dfs[0])