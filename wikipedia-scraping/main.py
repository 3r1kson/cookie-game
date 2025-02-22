from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# articles.click()

# articles = driver.find_element(By.LINK_TEXT, value='Content portals')
# articles.click()

# Open using buttons if the page is not full screen
# search = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')
# search.click()
#
# search_field = driver.find_element(By.NAME, value='search')
# search_field.send_keys('Python')
#
# button = driver.find_element(By.XPATH, value='//*[@id="searchform"]/div/button')
# button.click()

# Search if page is fullscreen
# search = driver.find_element(By.NAME, value='search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)