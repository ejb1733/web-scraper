from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ejb1733.github.io/landing-page/")
driver.implicitly_wait(30)
useeeer = driver.find_element(By.CLASS_NAME, "button4")
useeeer.click()