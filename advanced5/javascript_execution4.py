from curses import window
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://letskodeit.teachable.com/"

class JavaScriptExecution():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(4)
        #driver.get(url)
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/';")
        sleep(20)
      
        # to scroll till page bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        driver.quit()


ff = JavaScriptExecution()
ff.test()