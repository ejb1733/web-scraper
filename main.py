from selenium import webdriver
from selenium.webdriver.common.by import By
import time

COURSE_SITE = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=CPSC&course=304&section=2W1'

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(COURSE_SITE)

course_name = driver.find_element(By.TAG_NAME, 'h4').text

def seatsummary(n, delay):
    for i in range(n):
        seat_info = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/table[4]/tbody').text

        to_print = f'\nSeat Summary for [{course_name}]\n@ {time.ctime()} @\n{seat_info}\n---'
        f = open('scraped.txt', 'a')
        f.write(to_print)
        f.close()
        print(to_print)

        time.sleep(delay)

seatsummary(3, 5)