from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

name_field = driver.find_element(By.NAME, value="fName")
name_field.send_keys("Erikson")

name_field = driver.find_element(By.NAME, value="lName")
name_field.send_keys("Santos")

name_field = driver.find_element(By.NAME, value="email")
name_field.send_keys("eriksonsantos@aol.com")

button = driver.find_element(By.XPATH, value='/html/body/form/button')
button.click()

