# Logging is a standard way to track events that happen when some software runs.
# The logging module in Python provides a flexible framework for emitting log messages from Python programs.

import logging

# ## Configure the basic logging  settings
# logging.basicConfig(level=logging.DEBUG)

# ## Log messages  with different severity levels
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")


# Configuring logging 
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filename = 'app.log',
    filemode = 'w'  # 'w' to overwrite the log file each time
)

logging.info("Logging configured with custom format")
logging.error("This is an error message with timestamp")
logging.debug("This is a debug message with timestamp")
logging.warning("This is a warning message with timestamp")
logging.critical("This is a critical message with timestamp")

