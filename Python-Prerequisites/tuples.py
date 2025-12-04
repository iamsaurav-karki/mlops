# 2. TUPLE — ordered, unchangeable, allows duplicates

my_tuple = (1, 2, 3)

# my_tuple[0] = 99  # ❌ error


# Return multiple values from function
def get_model_stats():
    accuracy = 0.94
    loss = 0.12
    return (accuracy, loss)

acc, loss = get_model_stats()
print(acc, loss)
