# 1. LIST — ordered, changeable, allows duplicates

my_list = [1, 2, 3, 4]

print(my_list)

nums = [10, 20, 30]

nums.append(40)          # add at end
nums.insert(1, 15)       # insert at index
nums.remove(20)          # remove value
nums[0] = 99             # update index
print(nums[1])           # access


# Storing File paths 

data_files = ["img1.jpg", "img2.jpg", "img3.jpg"]

for f in data_files:
    print("Loading:", f)
