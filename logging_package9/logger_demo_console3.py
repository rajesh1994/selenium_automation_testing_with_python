import logging

class LoggerDemoConsole():
    def testLog(self):
        #Create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)
        
        #Create console handler and set level to info
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        #Create formatter
        formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        
        #Add formatter to console handler
        console_handler.setFormatter(formatter)
        
        #Add console handler to logger
        logger.addHandler(console_handler)
        
        #Logging message
        logger.info("Info message")
        logger.debug("Debug message")
        logger.error("Error message")
        logger.warning("Warning message")
        logger.critical("Critical message")

demo = LoggerDemoConsole()
demo.testLog()