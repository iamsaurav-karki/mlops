# File Operation - Reading, Writing, and Managing Files in Python

# Read a whole file 
with open('sample.txt', 'r') as file:
    content = file.read()
    print("File Content:")
    print(content)

# Read file line by line
with open('sample.txt', 'r') as file:
    print("File Content Line by Line:")
    for line in file:
        print(line.strip())  # strip() removes leading/trailing whitespace

# Writing to a file(overwriting)
with open('output.txt', 'w') as file:   
    file.write("This is a new line.\n")
    file.write("This will overwrite existing content.\n")


# Writing to a file without overwriting (appending)
with open('output.txt', 'a') as file:   
    file.write("This line is appended.\n")
    file.write("Appending another line.\n")


# Writing a list of lines to a file
lines = ["First line\n", "Second line\n", "Third line\n"]
with open('output.txt', 'a') as file:   
    file.writelines(lines)

# Binary file operations
# Writing binary data to a file
with open('binary_file.bin', 'wb') as bin_file:
    bin_file.write(b'\x00\xFF\x7A\x3C\x1D')


# Reading binary data from a file
with open('binary_file.bin', 'rb') as bin_file:
    binary_content = bin_file.read()
    print("Binary File Content:")
    print(binary_content)


# Read a content form a source text file and write it to a destination text file
with open('sample.txt', 'r') as source_file:
    content = source_file.read()

with open('destination.txt', 'w') as dest_file:
    dest_file.write(content)

# Read the text file and count the number of lines , words and characters
with open('sample.txt', 'r') as file:
    content = file.read()
    lines = content.splitlines()
    num_lines = len(lines)
    num_words = len(content.split())
    num_characters = len(content)
    print(f"Lines: {num_lines}, Words: {num_words}, Characters: {num_characters}")

# Writing and then reading a file 

with open('test_file.txt', 'w+') as test_file:
# w+ mode allows both writing and reading , if the file does not exist it creates a new one and if it exists it overwrites the existing content
    test_file.write("Hello, this is a test file.\n")
    test_file.write("I am testing file operations in Python.\n")
    test_file.seek(0)  # Move the cursor to the beginning of the file
    content = test_file.read()
    print("Test File Content:")
    print(content)