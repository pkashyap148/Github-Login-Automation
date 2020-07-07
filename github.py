from selenium import webdriver
from selenium.webdriver.common.keys import Keys

u = input("Enter Email: ")
p = input("Enter Password: ")

driver = webdriver.Chrome()
driver.get("https://github.com/login")

username = driver.find_element_by_name('login')
username.click()
username.send_keys(u)

pwd = driver.find_element_by_name('password')
pwd.click()
pwd.send_keys(p)

submit = driver.find_element_by_name('commit')
submit.click()

x = input("Enter Verification code: ")

otp = driver.find_element_by_name('otp')
otp.click()
otp.send_keys(x)

log = driver.find_element_by_xpath('//*[@id="login"]/div[3]/form/button')
log.click()
