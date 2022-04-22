import os
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://courses.letskodeit.com/practice"

class ListOfElements():
    def test(self):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        
        class_elements = driver.find_elements(By.CLASS_NAME, "inputs")
        lenth_of_class = len(class_elements)
        if class_elements is not None:
            print("Size of the class elements is ", + lenth_of_class)
        
        tag_elements = driver.find_elements(By.TAG_NAME, 'a')
        lenth_of_tag = len(tag_elements)
        if tag_elements is not None:
            print("Size of the anchor tag elements is ", +lenth_of_tag)
        driver.quit()


ff = ListOfElements()
ff.test()