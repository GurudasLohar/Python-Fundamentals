# Logging in Python

# Logging is essential for debugging, monitoring, and maintaining applications.
# The logging module is part of Python's standard library.

import logging
import logging.handlers
import sys

print("=== Logging in Python - Enhanced Guide ===\n")

# 1. Basic Configuration
print("=== 1. Basic Logging Setup ===")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.debug("This is a debug message (won't show by default)")
logging.info("Application started")
logging.warning("Low disk space warning")
logging.error("Failed to connect to database")
# logging.critical("Critical system failure!")

# 2. Logging to File + Console
print("\n=== 2. Logging to File ===")

# Create a logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)

# File handler (rotating logs)
file_handler = logging.handlers.RotatingFileHandler(
    'app.log', maxBytes=1024*1024, backupCount=5
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(console_format)
logger.addHandler(file_handler)

logger.info("This message goes to both console and file")
logger.debug("Debug information saved to file")

# 3. Logging Levels
print("\n=== 3. Logging Levels (from lowest to highest) ===")
print("""
DEBUG    - Detailed information for diagnosing problems
INFO     - General information about program execution
WARNING  - Something unexpected happened (potential issue)
ERROR    - Serious problem, function couldn't execute
CRITICAL - Critical error, program may not continue
""")

# 4. Advanced: Custom Logger with Function Decorator
print("\n=== 4. Logging Decorator Example ===")

def log_execution(func):
    """Decorator to log function execution"""
    def wrapper(*args, **kwargs):
        logger.info(f"Starting {func.__name__} with args: {args}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Completed {func.__name__} successfully")
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise
    return wrapper

@log_execution
def divide(a, b):
    return a / b

try:
    divide(10, 2)
    divide(10, 0)   # This will log an error
except ZeroDivisionError:
    pass

# 5. Best Practices
print("\n=== 5. Logging Best Practices ===")
print("""
1. Use different log levels appropriately
2. Log to files with rotation for production
3. Include timestamps and meaningful messages
4. Avoid logging sensitive information
5. Use structured logging (JSON) for large applications
6. Configure logging once at application startup
""")

print("\n=== Good logging makes debugging and monitoring much easier! ===")
print("Check 'app.log' file for logged messages.")