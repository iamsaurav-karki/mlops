# 3. DICTIONARY — key-value pairs, ordered

person = {
    "name": "Saurav",
    "age": 23,
    "role": "DevOps"
}

print(person["name"])
print(person.get("age"))

person["age"] = 24
person["city"] = "Kathmandu"

# Looping through Dictionary
for key, value in person.items():
    print(key, value)


config = {
    "learning_rate": 0.001,
    "epochs": 10,
    "batch_size": 32,
}

for key, value in config.items():
    print(key, "=", value)


# Nested Dictionary
students = {
    "student1": {
        "name": "Alice",
        "age": 20
    },
    "student2": {
        "name": "Bob",
        "age": 22
    }
}   
for student_id, details in students.items():
    print(student_id)
    for key, value in details.items():
        print(f"  {key}: {value}")
        