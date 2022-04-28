from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://courses.letskodeit.com/practice"

class ScrollingElement():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get(url)
        
        #Scroll down
        driver.execute_script("window.scrollBy(0, 800);")
        sleep(5)
        
        #Scroll up
        driver.execute_script("window.scrollBy(0, -800);")
        sleep(5)
        
        #Scroll element into view
        mouse_over_field = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", mouse_over_field)
        sleep(3)
        driver.execute_script("window.scrollBy,(0, -100);")
        
        #Native way to scroll element into view
        sleep(3)
        driver.execute_script("window.scrollBy(0, -1000);")
        print("Mouse over field location in the web page: ", str(mouse_over_field.location_once_scrolled_into_view))
        driver.execute_script("window.scrollBy(0, -150);")
        sleep(5)
        
        driver.quit()

ff = ScrollingElement()
ff.test()