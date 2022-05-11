from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/index.htm")
#identify element
l= driver.find_elements(by=By.TAG_NAME, value='a')
#get list size with len
s = len(l)
# check condition, if list size > 0, element exists
if(s>0):
    for i in l:
        print("Element found - " + i.text)
else:
   print("Element not found")
driver.close()
driver.current_url

submit = driver.find_element(By.ID, "submit")
submit.submit()