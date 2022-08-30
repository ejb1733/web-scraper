from selenium import webdriver
from selenium.webdriver.common.by import By

from logininfo import username, password

driver = webdriver.Chrome()
driver.get("https://ssc.adm.ubc.ca/sscportal/")
driver.implicitly_wait(5)

driver.find_element(By.XPATH, '//a[@href="/sscportal/servlets/SRVSSCFramework"]').click()

username_box = driver.find_element(By.ID, 'username')
password_box = driver.find_element(By.ID, 'password')
submit_box = driver.find_element(By.CLASS_NAME, 'btn-submit')

username_box.send_keys(username)
password_box.send_keys(password)
submit_box.click()