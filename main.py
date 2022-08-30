from selenium import webdriver
from selenium.webdriver.common.by import By
from emailing import sendMail
import time
import linecache

COURSE_SITE = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=CPSC&course=304&section=2W1'

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(COURSE_SITE)

course_name = driver.find_element(By.TAG_NAME, 'h4').text

def seatsummary(n, delay):
    last_num_saved = getCurrRegisteredFromFile()
    print(last_num_saved)
    for i in range(n):
        seat_summ = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/table[4]/tbody').text

        next_num_saved = int(driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/table[4]/tbody/tr[2]/td[2]/strong').text)

        curr_write_time = time.ctime()

        to_write = f'\nSeat Summary for [{course_name}]\n@ {curr_write_time}:\n{seat_summ}\n--------------------------------'
        f = open('scraped.txt', 'a')
        f.write(to_write)
        f.close()

        if (last_num_saved < next_num_saved):
            sendMail(course_name, 'registered in', last_num_saved, next_num_saved, to_write)
        elif (last_num_saved > next_num_saved):
            sendMail(course_name, 'dropped', last_num_saved, next_num_saved, to_write)
        last_num_saved = next_num_saved

        print(last_num_saved)

        driver.refresh()
        time.sleep(delay)

def getCurrRegisteredFromFile():
    num_lines = sum(1 for line in open('scraped.txt'))
    if (num_lines == 0):
        return -1
    last_registered_line = linecache.getline('scraped.txt', num_lines - 3)
    last_num_registered = ''
    for char in last_registered_line:
        if char.isdigit():
            last_num_registered += char
    return int(last_num_registered)

# !!! BUG
# def getTimeFromFile():
#     nlines = sum(1 for line in open('scraped.txt'))
#     last_time = linecache.getline('scraped.txt', nlines - 5)
#     print(last_time)
#     return last_time

seatsummary(1000, 120)