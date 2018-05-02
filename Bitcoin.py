__author__ = 'mmarom'

from selenium import webdriver
import time
import sys

driver = webdriver.Chrome()
driver.get("http://preev.com")
usd_value = driver.find_element_by_id("numField")

num_of_bitcoins = input("Please enter the number of bitcoins: ")

print("The value of " + num_of_bitcoins + " Bitcoin(s) in USD is:")
while True:
    time.sleep(1)
    total_bit_value = int(num_of_bitcoins) * int(usd_value.get_attribute("value").replace(",", ""))
    sys.stdout.write('\r' + str(total_bit_value))
