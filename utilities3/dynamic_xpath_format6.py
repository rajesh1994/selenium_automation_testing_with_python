import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://letskodeit.teachable.com/courses"

class DynamicXPathFormat():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        
        """    # Login - Lecture "How to click and type on a web element"
        login_link = driver.find_element(By.LINK_TEXT, "Login")
        login_link.click()
        
        email_field = driver.find_element(By.XPATH, "//input[@id='email']")
        email_field.send_keys("test@email.com")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("abcabc")
        
        login_field = driver.find_element(By.XPATH, "//input[contains(@value,'Login')]")
        login_field.click() """

        # Search for courses -> You don't need to search the course
        # You can select it without searching also
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("JavaScript")

        # Select Course
        _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()
        sleep(5)
        
        driver.quit()


ff = DynamicXPathFormat()
ff.test()
        
        