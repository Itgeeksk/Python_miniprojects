# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# Selenium web drive setup
PATH = os.path.join(os.getcwd(), 'chromedriver.exe')
driver = webdriver.Chrome(PATH)
driver.get('https://facebook.com')

# Getting element of login form email field and pass field
username = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'pass')

# Putting username in the field
username.clear()
username.send_keys("username")
password.clear()
password.send_keys("password")

# Getting login button and click on it
submit = driver.find_element(By.NAME, 'login')
submit.send_keys(Keys.RETURN)
