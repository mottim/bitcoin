__author__ = 'mmarom'

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys

import json

with open('config.json') as json_data:
    data = json.load(json_data)
    num_of_bitcoins = int(data["number_of_bitcoins"])

driver = webdriver.Chrome()
driver.get("http://preev.com")

previous_usd_value = -1

try:
    bc_value_field = driver.find_element_by_id("numField")
    print("The value of " + str(num_of_bitcoins) + " Bitcoin(s) in USD is: ")
    while True:
        time.sleep(1)
        current_usd_value = bc_value_field.get_attribute("value").replace(",", "")
        if previous_usd_value != current_usd_value:
            total_bit_value = num_of_bitcoins * int(current_usd_value)
            sys.stdout.write('\r' + "$" + str(total_bit_value))

except NoSuchElementException:
    print("Unable to find the bitcoin field")
    driver.quit()


