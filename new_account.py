import os
import time

from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

print("Enter your first name")
first_name = input()
print("Enter your last name")
last_name = input()
print("Enter username of your choice")
username = input()
print("Enter a strong password")
password = input()
print("Enter your phone number")
phone_num = input()

os.environ['PATH'] += r"C:\\driver"
driver = webdriver.Firefox()
driver.get("https://accounts.google.com/signup")

f_name = driver.find_element(By.ID, "firstName")
f_name.send_keys(first_name)

l_name = driver.find_element(By.ID, "lastName")
l_name.send_keys(last_name)

user = driver.find_element(By.ID, "username")
user.send_keys(username)

passwd = driver.find_element(By.NAME, "Passwd")
passwd.send_keys(password)

confirm_pass = driver.find_element(By.NAME, "ConfirmPasswd")
confirm_pass.send_keys(password)