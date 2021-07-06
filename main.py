import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options

#   command line arguments
args = sys.argv[1:]

#   webdriver init

#       headless
#options = Options()
#options.headless = True
#driver = webdriver.Firefox(options=options)

driver = webdriver.Firefox()

#   traversal
results = {}
driver.get('https://www.lego.com/en-us/page/static/pick-a-brick')
continue_button = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element_by_css_selector('button.Button__Base-sc-1jdmsyi-0:nth-child(4)') )
continue_button.click()
accept_all_button = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element_by_css_selector('button.aKFCv:nth-child(2)'))
accept_all_button.click()

for item in args:
    search_field = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element_by_css_selector('#pab-search'))
    search_apply = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element_by_css_selector('.iEXjfw'))
    search_field.clear()
    search_field.send_keys(item)
    search_apply.click()
    try:
        time.sleep(.1)
        driver.find_element_by_css_selector('li.ElementsListstyles__Leaf-d5a7o-1:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)')
        results[item] = "in stock"
    except:
        results[item] = "out of stock"

driver.quit()
for k, v in results.items():
    print(f"{k} : {v}")
