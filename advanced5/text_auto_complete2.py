from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
class CalendarSelection():

    def test1(self):
        baseUrl = "https://www.southwest.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        depart_field = driver.find_element(By.ID,'LandingAirBookingSearchForm_originationAirportCode')
        depart_field.send_keys("New York")
        sleep(2)
        
        # Select the second option from the autocomplete
        driver.switch_to.active_element
        depart_field.send_keys(Keys.ARROW_DOWN)
        sleep(2)
        depart_field.send_keys(Keys.ARROW_DOWN)
        sleep(2)
        depart_field.send_keys(Keys.ENTER)

        driver.quit()

ff = CalendarSelection()
ff.test1()