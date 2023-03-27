import os
import time

from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

print("Enter you first name")
first_name = input()
print("Enter your last name")
last_name = input()
print("Enter username of your choice")
username = input()
print("Enter a strong password")
password = input()

os.environ['PATH'] += r"C:\\driver"
driver = webdriver.Firefox()
driver.get("https://accounts.google.com/signup")