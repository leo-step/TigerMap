'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path='C:\\Users\\Leo\\Downloads\\chromedriver_win32\\chromedriver.exe')

driver.get("https://registrar.princeton.edu/course-offerings/course-details?term=1232&courseid=002054")
time.sleep(1)
html = driver.page_source

print(html)
'''

import bs4
import os
import re
from files import *

code_to_id = {}
id_to_code = {}
labels = open(LABELS_FILE, 'r')
for line in labels.readlines():
    fields = line.split(',')
    id_to_code[int(fields[0])] = fields[1]
    code_to_id[fields[1]] = int(fields[0])

code_pattern = re.compile(r"[A-Z][A-Z][A-Z] \d\d\d")
no_space_pattern = re.compile(r"[A-Z][A-Z][A-Z]\d\d\d")
for path in ["1143.html"]:
    course = open(PAGES_DIR + '/' + path, 'r')
    soup = bs4.BeautifulSoup(course.read(), features="lxml")
    prereqs_div = soup.find("div", {"class": "prereqs-and-other-restrictions"})
    if prereqs_div:
        first_sentence = prereqs_div.find("span").text.split('.')[0]
        print(first_sentence)
        prereqs = code_pattern.findall(first_sentence)
        no_space = no_space_pattern.findall(first_sentence)
        prereqs.extend(list(map(lambda x: x[:3] + ' ' + x[3:], no_space)))
        for prereq in prereqs:
            course_id = int(path[:-5])
            if prereq == id_to_code[course_id]:
                continue
            elif prereq in code_to_id:
                print(prereq)
                #adjlist.write("{},{}\n".format(course_id, code_to_id[prereq]))
            else:
                print(prereq + " not found")
    course.close()