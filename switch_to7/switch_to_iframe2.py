from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "https://courses.letskodeit.com/practice"

class SwitchToIframe():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(url)
        
        #Switch to frame using ID
        iframe_element = driver.find_element(By.ID, "courses-iframe")
        ActionChains(driver).move_to_element(iframe_element).perform()
        driver.switch_to.frame("courses-iframe")
        
        #Switch to frame using name
        #driver.switch_to.frame("iframe-name")
        
        # Switch to frmae using index
        #driver.switch_to.frmae(0)
        
        sleep(5)
        
        search_field = driver.find_element(By.XPATH, "//form[@name='search']/div/input")
        search_field.send_keys("Python")
        
        #search_button = driver.find_element(By.XPATH, "//form[@name="search"]/div/button")
        #search_button.click()
        
        #sleep(5)
        course_selection = driver.find_element(By.XPATH, "//div[@id='course-list']/div[1]")
        print(course_selection.text)
        
        #Switch back to the parent frame
        driver.switch_to.default_content()
        sleep(5)
        
        driver.quit()

ff = SwitchToIframe()
ff.test()