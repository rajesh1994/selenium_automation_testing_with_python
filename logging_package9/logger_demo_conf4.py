"""
Logger Demo
"""
import logging
import logging.config

class LoggerDemoConf():

    def testLog(self):
        # create logger
        logging.config.fileConfig('selenium_automation_testing_with_python/logging_package9/logging.conf')
        logger = logging.getLogger(LoggerDemoConf.__name__)

        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerDemoConf()
demo.testLog()