from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "https://courses.letskodeit.com/practice"

class SwitchTo():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get(url)
        
        #Find the parent handle --> Parent window
        parent_handle = driver.current_window_handle
        print("Parent Handle :", parent_handle)
        
        #Find open window button & click it
        open_window_button = driver.find_element(By.ID, "openwindow")
        open_window_button.click()
        
        #Find all handles, there should be two handles after clicking open window button
        handles = driver.window_handles
        for handle in handles:
            print("Handle :", handle)
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                print("Switched to window :: ", handle)
                driver.maximize_window()
                sleep(5)
                search_field = driver.find_element(By.ID, "search")
                ActionChains(driver).move_to_element(search_field).send_keys("Python").perform()
                                
                search_button = driver.find_element(By.XPATH, "//form[@id='search']/div/button")
                search_button.click()
                sleep(4)
                driver.close()
                break
        
        #Swtich back to the parent handle
        driver.switch_to.window(parent_handle)
        alert_text_field = driver.find_element(By.ID, "displayed-text")
        alert_text_field.send_keys("Selenium")
        driver.quit()


ff = SwitchTo()
ff.test()