from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

url = ""
amount_of_tickets = ""
input_field_id = ""

time_scriptstart = datetime.now()
print("Script started running at: ", time_scriptstart.strftime("%H:%M:%S.%f"))

browser = webdriver.Chrome()
browser.get(url)

time_website_open = datetime.now()
print("Page was loaded at: ", time_website_open.strftime("%H:%M:%S.%f"))

element = browser.find_element(By.ID, input_field_id)
element.send_keys(amount_of_tickets)
element.submit()

time_submit_click = datetime.now()
print("Selection has been made at: ", time_submit_click.strftime("%H:%M:%S.%f"))