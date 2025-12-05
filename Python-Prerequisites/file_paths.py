## Listing Files and Directories in a Given Path
import os
items = os.listdir('.')
print(items)


# Joining paths 

dir_name = "folder"
file_name = "file.txt"
full_path = os.path.join(dir_name, file_name)
print(f"Full path: {full_path}")

dir_name = "folder"
file_name = "file.txt"
full_path = os.path.join(os.getcwd(),dir_name, file_name)
print(f"Full path: {full_path}")


path = "/home/user/docs/file.txt"
if os.path.exists(path):
    print(f"The path '{path}' exists.")
else:
    print(f"The path '{path}' does not exist.")

path2 = "/home/skarki/mlops-learn/Python-Prerequisites/"
if os.path.exists(path2):
    print(f"The path '{path2}' exists.")
else:
    print(f"The path '{path2}' does not exist.")    

# Splitting paths
path = "/home/user/docs/file.txt"
dir_name, file_name = os.path.split(path)
print(f"Directory: {dir_name}")
print(f"File Name: {file_name}")

# Checking if a path is a file or directory
path = "sample.txt"
if os.path.isfile(path):
    print(f"The path '{path}' is a file.")
elif os.path.isdir(path):
    print(f"The path '{path}' is a directory.")
else:
    print(f"The path '{path}' is neither a file nor a directory.")

# Getting absolute path
relative_path = "sample.txt"
absolute_path = os.path.abspath(relative_path)
print(f"Absolute path: {absolute_path}")
