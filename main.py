#importing selenium
import selenium
#from selenium importing web driver using version 4.12
from selenium import webdriver
from selenium.webdriver.common.by import By

#selecting Chrome as driver for our test
driver= webdriver.Chrome()
#Here I use a log in page of "HCL tech" web application for the test.
driver.get('https://www.hcltech.com/user/login')

# by inspecting the web page we get the values of username and password for this page which are alredy written in textbox.


#now we find name by using a method "find_element_by_name"
# inserting our values by using method ".send_keys" in driver
driver.find_element(By.NAME,"name").send_keys("usermname@123")
#similarly for password
driver.find_element(By.NAME,"pass").send_keys("pass@123")
# by inspecting find element of login button as name/id/type.
# here .click() action submit the entered details.
driver.find_element(By.NAME,"name").click()

#compairing thee resultant and the expected output
actual_title=driver.title
exp_title="HCL Tech"

#check wheather testcase gets passed or not
if actual_title==exp_title:
    print("yahooo..."
          "Test Passed")
else:
    print("Ooo.. No"
          "Test Not Passed Try again!!!")

#end of process and show result
driver.close()