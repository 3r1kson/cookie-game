import os
import platform
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value='cookie')
total = driver.find_element(By.ID, value='money')

cursor_price = 0
grandma_price = 0
factory_price = 0
mine_price = 0
shipment_price = 0
alchemy_price = 0
portal_price = 0
time_machine_price = 0

def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def get_prices():
    global cursor_price, grandma_price, factory_price, \
        mine_price, shipment_price, alchemy_price, \
        portal_price, time_machine_price

    all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")

    for i in all_prices:
        text = i.text.strip()
        if text:
            x = text.split()
            if len(x) > 2:
                item_name = x[0]
                price = int(x[-1].replace(',', ''))

                match item_name:
                    case "Cursor":
                        cursor_price = price
                    case "Grandma":
                        grandma_price = price
                    case "Factory":
                        factory_price = price
                    case "Mine":
                        mine_price = price
                    case "Shipment":
                        shipment_price = price
                    case "Alchemy":
                        alchemy_price = price
                    case "Portal":
                        portal_price = price
                    case "Time":
                        time_machine_price = price

start_timer = time.localtime().tm_min
start_time = time.time()
counter = time.localtime().tm_sec
print("STARTING")

def buy():
    clear_console()

    value = int(total.text.replace(',', '').strip())

    if value < grandma_price:
        driver.find_element(By.ID, value='buyCursor').click()
        print("cursor")

    elif value < factory_price:
        print("grandma")

        driver.find_element(By.ID, value='buyGrandma').click()
    elif value < mine_price:
        print("factory")
        driver.find_element(By.ID, value='buyFactory').click()
    elif value < shipment_price:
        print("mine")
        driver.find_element(By.ID, value='buyMine').click()
    elif value < alchemy_price:
        print("shipment")
        driver.find_element(By.ID, value='buyShipment').click()
    elif value < portal_price:
        print("alchemy")
        driver.find_element(By.ID, value='buyAlchemy lab').click()
    elif value < time_machine_price:
        print("portal")
        driver.find_element(By.ID, value='buyPortal').click()
    else:
        print("time machine")
        driver.find_element(By.ID, value='buyTime machine').click()


def check():
    global counter
    if counter + 5 == time.localtime().tm_sec:
        print("5 secs passed")
        counter = time.localtime().tm_sec
        get_prices()
        buy()

while time.time() - start_time < 60:
    cookie.click()
    if time.time() - start_time >= 5:
        get_prices()
        buy()
        start_time = time.time()
