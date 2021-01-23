from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

time.sleep(15)

print('Scanning is complete...')

user_name = 'Whatsapp user Name'

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()

messages_box = driver.find_element_by_xpath('//div[@class= "class name"]')  #Xpath class Name messages box 
messages_box.send_keys("Hey I am Your Whatsapp bot")

messages_button = driver.find_element_by_xpath('//button[@class= "class name"]') #Xpath class Name send button
messages_button.click()