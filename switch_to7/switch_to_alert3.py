from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://courses.letskodeit.com/practice"

class SwitchToAlert():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(url)
        
        alert_text_field = driver.find_element(By.ID, "name")
        alert_text_field.send_keys("Vijay")
        sleep(5)
        
        #By clicking OK button accepting the JavaScript alert
        alert_button = driver.find_element(By.ID, "alertbtn")
        alert_button.click()
        sleep(5)
        driver.switch_to.alert.accept()
        sleep(5)
        
        #By clicking OK button dismissing the JavaScript alert
        alert_text_field.send_keys("Vijay")
        alert_button = driver.find_element(By.ID, "alertbtn")
        sleep(5)
        alert_button.click()
        sleep(5)
        driver.switch_to.alert.dismiss()
        
        #By clicking OK button confirming the JavaScript alert
        sleep(5)
        alert_text_field.send_keys("Vijay")
        sleep(5)
        confirm_button = driver.find_element(By.ID, "confirmbtn")
        sleep(5)
        confirm_button.click()
        sleep(5)
        driver.switch_to.alert.accept()
        sleep(5)
        
        #By clicking Cancel button Cancelling the JavaScript alert
        alert_text_field.send_keys("Vijay")
        sleep(5)
        confirm_button = driver.find_element(By.ID, "confirmbtn")
        confirm_button.click()
        sleep(5)
        driver.switch_to.alert.accept()
        sleep(5)
        
        driver.quit()

ff = SwitchToAlert()
ff.test()