from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://letskodeit.teachable.com/"

class WindowSize():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(4)
        
        screen_height = driver.execute_script("return window.innerHeight;")
        screen_width = driver.execute_script("return window.innerWidth;")
        
        print("Height & Width of the screen: " + str(screen_height), " X ", str(screen_width))
        
        sleep(5)
        driver.quit()

ff = WindowSize()
ff.test()