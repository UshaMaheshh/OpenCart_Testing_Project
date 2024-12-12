import logging
import os
@staticmethod
def loggen():
# Define log file path
    log_directory = 'C:\\Users\\usha5\\PycharmProjects\\Opencart_Project\\logs'
    log_file = os.path.join(log_directory, 'test_log.log')

# Ensure log directory exists
    if not os.path.exists(log_directory):
       os.makedirs(log_directory)

# Set up logging
    logging.basicConfig(
       filename=log_file,
       level=logging.INFO,  # Set log level
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
       filemode='a')

# Test logging
    logger = logging.getLogger('root')
    return logger



