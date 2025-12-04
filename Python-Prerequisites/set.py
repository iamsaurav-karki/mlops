# 4. SET — unordered, unique values, no duplicates

my_set = {1, 2, 3, 3}
print(my_set)   # {1, 2, 3}

my_set.add(4)
my_set.remove(1)


# Unique labels in set 

labels = ["cat", "dog", "cat", "cow", "dog"]

unique_labels = set(labels)
print(unique_labels)

# Looping through Set
for label in unique_labels:
    print("Label:", label)
    
# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}   
union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)   

print("Union:", union_set)
print("Intersection:", intersection_set)
difference_set = set_a.difference(set_b)
print("Difference (A-B):", difference_set)  

