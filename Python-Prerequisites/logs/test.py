from logger import logging

def add(a, b):
    logging.debug(f"Adding {a} and {b}")

    return a + b

logging.debug("This addition function is added")
result = add(5, 3)
print(f"Result: {result}")
