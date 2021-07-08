#!/usr/bin/python3
import sys
import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options
import psycopg2
import connect

def check(User):
    reuslts = []
    for item in User.items:
        result = {}
        result["item"] = item
        if "/" not in item:
            print(f"{item}: is not a valid lego item number format")
            return
        item_split = item.split(sep="/")
        driver.get(f'https://www.lego.com/en-us/page/static/pick-a-brick?query={item_split[0]}%2F{item_split[1]}&page=1')
        try:
            time.sleep(.1)
            driver.find_element_by_css_selector('li.ElementsListstyles__Leaf-d5a7o-1:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)')
            result[item] = "true"
        except:
            result[item] = "false"
        results.append(result)
    return models.StockReport(User.uid, User.uname, *results) 




cur, conn  = connect.db_connect()
#       headless
#options = Options()
#options.headless = True
#driver = webdriver.Firefox(options=options)

driver = webdriver.Firefox()

#   dealing with cookie agreements
driver.get('https://www.lego.com/en-us/page/static/pick-a-brick')
continue_button = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element_by_css_selector('button.Button__Base-sc-1jdmsyi-0:nth-child(4)') )
continue_button.click()
accept_all_button = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element_by_css_selector('button.aKFCv:nth-child(2)'))
accept_all_button.click()

rows = models.get_all_users(cur)
for row in rows:
    user = models.User(*row)
    stock_report = check(user)
    stock_report.insert(cur, conn)


        


driver.quit()
cur.close()
conn.close()
