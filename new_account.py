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
DOB = input("Enter your date of birth like this 2002 5 27: \n").split()
year = DOB[0]
month = DOB[1]
day = DOB[2]
gender = input("Enter 1 if you are male, 2 if you are female, 3 if you don't want to reveal, 4 if other(custom) \n")


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

Next_field = driver.find_elements(By.CLASS_NAME, "VfPpkd-LgbsSe")[1]
Next_field.click()

time.sleep(5)
phone_number = driver.find_element(By.ID, "phoneNumberId")
phone_number.send_keys(phone_num)

Next_field1 = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
Next_field1.click()

verfication_num = print("Enter the recent code you got in the number that you have entered earlier: ")
verfication_num = input()

verify_num = driver.find_element(By.NAME, "code")
verify_num.send_keys(verfication_num)

verify_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
verify_button.click()

time.sleep(5)
year_field = driver.find_element(By.ID, "year")
year_field.click()
year_field.send_keys(year)

month_field = Select(driver.find_element(By.ID, 'month'))
month_field.select_by_value(month)

day_field = driver.find_element(By.ID, "day")
day_field.click()
day_field.send_keys(day)

gender_field = Select(driver.find_element(By.ID, "gender"))
gender_field.select_by_value(gender)

Next_field2 = driver.find_elements(By.CLASS_NAME, "VfPpkd-LgbsSe")[0]
Next_field2.click()