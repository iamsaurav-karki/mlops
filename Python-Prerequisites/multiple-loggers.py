import logging 

# create a logger for module 1

logger1 = logging.getLogger('module1')
logger1.setLevel(logging.DEBUG)

# create a logger for module 2
logger2 = logging.getLogger('module2')
logger2.setLevel(logging.ERROR)

# create a logger for module 3
logger3 = logging.getLogger('module3')
logger3.setLevel(logging.WARNING)

# configure logging setting 

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)


# log messages using different loggers
logger1.debug("This is a debug message from module 1")
logger1.info("This is an info message from module 1")
logger2.error("This is an error message from module 2")
logger2.warning("This is a warning message from module 2")  # This won't be logged
logger3.warning("This is a warning message from module 3")
logger3.critical("This is a critical message from module 3")
logger3.info("This is an info message from module 3")  # This won't be logged
logger1.error("This is an error message from module 1")

