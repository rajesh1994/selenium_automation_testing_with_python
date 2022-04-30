from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, time

url = "https://jqueryui.com/slider/"

class Sliders():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get(url)
        
        frame = driver.switch_to.frame(0)
        
        slider_element = driver.find_element(By.XPATH, "//div[@id='slider']/span")
        sleep(4)
        
        try:
            action = ActionChains(driver)
            action.drag_and_drop_by_offset(slider_element, 500, 0).perform()
            print("Sliding element successfully")
            action.drag_and_drop_by_offset(slider_element, -2000, 0).perform()
            print("Sliding element successfully")
            sleep(6)
        except:
            print("Sliding failed on element")
        driver.quit()

ff = Sliders()
ff.test()