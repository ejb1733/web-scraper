from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import linecache

COURSE_SITE = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=CPSC&course=304&section=2W1'

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(COURSE_SITE)

course_name = driver.find_element(By.TAG_NAME, 'h4').text

def seatsummary(n, delay):
    last_num_registered = getCurrRegisteredFromFile()
    for i in range(n):
        seat_info = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/table[4]/tbody').text

        to_print = f'\nSeat Summary for [{course_name}]\n@ {time.ctime()} @\n{seat_info}\n---'
        f = open('scraped.txt', 'a')
        f.write(to_print)
        f.close()
        print(last_num_registered)

        next_num_registered = int(driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/table[4]/tbody/tr[2]/td[2]/strong').text)

        if (last_num_registered < next_num_registered):
            print(f'{next_num_registered - last_num_registered} person(s) registered in the course!')
        elif (last_num_registered > next_num_registered):
            print(f'{last_num_registered - next_num_registered} person(s) dropped the course!')
        last_num_registered = next_num_registered

        driver.refresh()
        time.sleep(delay)

def getCurrRegisteredFromFile():
    num_lines = sum(1 for line in open('scraped.txt'))
    last_registered_line = linecache.getline('scraped.txt', num_lines - 3)
    empty_string = ''
    for char in last_registered_line:
        if char.isdigit():
            empty_string += char
    return int(empty_string)

seatsummary(5, 5)