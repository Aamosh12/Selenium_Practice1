import os
import time

from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

print("Enter your email or phone number")
data = input()
print("Enter your password")
password = input()

os.environ['PATH'] += r"C:\\driver"
driver = webdriver.Firefox()
driver.get("https://accounts.google.com/signin")