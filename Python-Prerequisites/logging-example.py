import logging 

# Configure logging settings
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a, b):
    logger.debug(f"Adding {a} and {b}")
    return a + b    

def subtract(a, b):
    logger.debug(f"Subtracting {b} from {a}")
    return a - b

def multiply(a, b):
    logger.debug(f"Multiplying {a} and {b}")
    return a * b

def divide(a, b):
    if b == 0:
        logger.error("Attempted to divide by zero")
        return None
    logger.debug(f"Dividing {a} by {b}")
    return a / b

add_result = add(10, 5)
logger.info(f"Addition Result: {add_result}")
subtract_result = subtract(10, 5)
logger.info(f"Subtraction Result: {subtract_result}")
multiply_result = multiply(10, 5)
logger.info(f"Multiplication Result: {multiply_result}")
divide_result = divide(10, 0)
if divide_result is not None:
    logger.info(f"Division Result: {divide_result}")

