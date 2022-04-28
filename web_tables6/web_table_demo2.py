from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_automation_testing_with_python.web_tables6.web_table1 import WebTable
import unittest
import warnings
warnings.filterwarnings('ignore', category=ResourceWarning)
class Test(unittest.TestCase):
    def test_web_table(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)

        driver.get("https://chercher.tech/practice/table")
        w = WebTable(driver.find_element(By.XPATH,"//table[@id='webtable']"))

        print("------------------------------------")
        print("------------------------------------")
        print("No of rows : ", w.get_row_count())
        print("------------------------------------")
        print("No of cols : ", w.get_column_count())
        print("------------------------------------")
        print("Table size : ", w.get_table_size())
        print("------------------------------------")
        print("First row data : ", w.row_data(1))
        print("------------------------------------")
        print("First column data : ", w.column_data(1))
        print("------------------------------------")
        print("All table data : ", w.get_all_data())
        print("------------------------------------")
        print("presence of data : ", w.presence_of_data("Chercher.tech"))
        print("------------------------------------")
        print("Get data from Cell : ", w.get_cell_data(3, 3))
        print("------------------------------------")
        print("------------------------------------")

if __name__ == "__main__":
    unittest.main()