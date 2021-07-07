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
import db



#   webdriver init

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

#   init an empty dict for storage
results = {}

#TODO get items from db instead of cmd line
#   iterate over items
args = sys.argv[1:] # cmd line args
for item in args:
    if "/" not in item:
        print(f"{item}: is not a valid lego item number format")
        continue
    item_split = item.split(sep="/")
    driver.get(f'https://www.lego.com/en-us/page/static/pick-a-brick?query={item_split[0]}%2F{item_split[1]}&page=1')
    try:
        time.sleep(.1)
        driver.find_element_by_css_selector('li.ElementsListstyles__Leaf-d5a7o-1:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)')
        results[item] = "1"
    except:
        results[item] = "0"

driver.quit()

print("#"*40)
for k, v in results.items():
    if v == "1":
        print(f"{k} : in stock!")
    else:
        print(f"{k} : out of stock :(")

#TODO insert into a db instead of stdout



def check(User):
    reuslts = {}    
    for item in User.items:
        result = {}
        if "/" not in item:
            print(f"{item}: is not a valid lego item number format")
            continue
        item_split = item.split(sep="/")
        driver.get(f'https://www.lego.com/en-us/page/static/pick-a-brick?query={item_split[0]}%2F{item_split[1]}&page=1')
        try:
            time.sleep(.1)
            driver.find_element_by_css_selector('li.ElementsListstyles__Leaf-d5a7o-1:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)')
            result[item] = "true"
        except:
            result[item] = "false"
        results["item"]= item
        results["status"]= 

    driver.quit()
            
        

#TODO get items from db instead of cmd line
#   iterate over items
args = sys.argv[1:] # cmd line args
for item in args:
    if "/" not in item:
        print(f"{item}: is not a valid lego item number format")
        continue
    item_split = item.split(sep="/")
    driver.get(f'https://www.lego.com/en-us/page/static/pick-a-brick?query={item_split[0]}%2F{item_split[1]}&page=1')
    try:
        time.sleep(.1)
        driver.find_element_by_css_selector('li.ElementsListstyles__Leaf-d5a7o-1:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)')
        results[item] = "1"
    except:
        results[item] = "0"

driver.quit()

print("#"*40)
for k, v in results.items():
    if v == "1":
        print(f"{k} : in stock!")
    else:
        print(f"{k} : out of stock :(")

#TODO insert into a db instead of stdout
