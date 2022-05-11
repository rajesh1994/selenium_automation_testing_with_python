from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "https://jqueryui.com/droppable/"

class DragAndDrop():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(url)
        
        #Switching to ifrmae
        driver.switch_to.frame(0)
        
        #Identifiying drag & drop field elements
        drag_field = driver.find_element(By.XPATH, "//div[@id='draggable']")
        drop_field = driver.find_element(By.XPATH, "//div[@id='droppable']")
        sleep(4)
        
        try:
            action = ActionChains(driver)
            
            #Performing drag & drop by using drag_and_drop() function
            #action.drag_and_drop(drag_field, drop_field).release().perform()
            
            #Performing drag & drop by using click_and_hold() and move_to_element() function
            action.click_and_hold(drag_field).move_to_element(drop_field).release().perform()
            dropped_text = driver.find_element(By.XPATH, "//div[@id='droppable']/p").text
            
            if dropped_text == "Dropped!":
                print("Drag & drop element successfull")
            sleep(4)
            
        except:
            print("Drag & drop failed on element")
        
        driver.quit()
ff = DragAndDrop()
ff.test()