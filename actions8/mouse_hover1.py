from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "https://courses.letskodeit.com/practice"

class MouseOver():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(url)
        
        mouse_over_button = driver.find_element(By.ID, "mousehover")
        mouse_over_button.location_once_scrolled_into_view
        top_link = driver.find_element(By.XPATH, "//a[text()='Top']")
        reload_link = driver.find_element(By.XPATH, "//a[text()='Reload']")
                
        try:
            action = ActionChains(driver)
            action.move_to_element(mouse_over_button).perform()
            print("Mouse hover on element ")
            sleep(4)
            action.move_to_element(top_link).click().perform()
            print("Item clicked :")
        except:
            print("Mouse hover failed on element")  
        
        sleep(5)
        
        try:
            action = ActionChains(driver)
            action.move_to_element(mouse_over_button).perform()
            print("Mouse hover on element ")
            sleep(4)
            action.move_to_element(reload_link).click().perform()
            print("Item clicked :")
        except:
            print("Mouse hover failed on element")     
        
        sleep(5)
        driver.quit()

ff = MouseOver()
ff.test()