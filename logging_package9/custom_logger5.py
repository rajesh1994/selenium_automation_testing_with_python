import inspect
import logging

def customLogger(logLevel):
    #Get the name of the class/method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    
    #By defualt log all messages
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler("{0}.log".format(logger_name), mode='w')
    file_handler.setLevel(logLevel)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
