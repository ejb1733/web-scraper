from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=CPSC&course=304&section=2W1')

def seatsummary(n, delay):
    for i in range(n):
        seat_info = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/table[4]').text

        f = open('scraped.txt', 'a')
        f.write(f'\n{seat_info}\n---')
        f.close()
        print(seat_info)

        time.sleep(delay)

seatsummary(3, 5)