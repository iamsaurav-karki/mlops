# Working with CSV Files in Python
import csv
'''
CSV (Comma Separated Values) is a common data format used for storing tabular data. Python provides a 
built-in module called 'csv' to work with CSV files.
'''
# Writing to a CSV file
with open('example.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Hari', 30, 'Nepalgunj'])
    writer.writerow(['Ram', 25, 'Pokhara'])
    writer.writerow(['Shyam', 35, 'Banepa'])
    
print("Data written to 'example.csv'.")
# Reading from a CSV file
with open('example.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
