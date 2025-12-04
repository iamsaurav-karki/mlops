## For loop 
for i in range(5):
    print(i)

## While loop 
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

## Check Job Status                                             
status = "running"

while status != "completed":
    print("Training in progress...")
    # simulate job check
    status = "completed"

print("Training finished!")


# Looping through Dictionary
config = {
    "lr": 0.001,
    "epochs": 10,
    "batch_size": 32
}

for key, value in config.items():
    print(key, "=", value)

# Nested Loops 

lrs = [0.01, 0.001]
batch_sizes = [16, 32]

for lr in lrs:
    for bs in batch_sizes:
        print(f"Training model with lr={lr}, batch={bs}")
