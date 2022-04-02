import bs4
import os
import shutil
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from files import *

download_links = []

fall_courses = open(FALL_COURSES_FILE, 'r')
soup = bs4.BeautifulSoup(fall_courses.read(), features="lxml")
td = soup.find("td", {"class": "class-info"})
fall_courses.close()

if os.path.exists(LABELS_FILE):
    os.remove(LABELS_FILE)

labels = open(LABELS_FILE, 'w')
course_id = 0
seen_codes = set()

for td in soup.find_all("td", {"class": "class-info"}):
    catalog_codes = td.find("small").text.strip().split(" / ")
    link_elem = td.find("a")
    for catalog_code in catalog_codes:
        if catalog_code not in seen_codes:
            labels.write("{},{},{},{}\n".format(course_id, catalog_code, link_elem["href"], link_elem.text))
            download_links.append((course_id, link_elem["href"]))
            course_id += 1
            seen_codes.add(catalog_code)

spring_courses = open(SPRING_COURSES_FILE, 'r')
soup = bs4.BeautifulSoup(spring_courses.read(), features="lxml")
td = soup.find("td", {"class": "class-info"})
spring_courses.close()

for td in soup.find_all("td", {"class": "class-info"}):
    catalog_codes = td.find("small").text.strip().split(" / ")
    link_elem = td.find("a")
    for catalog_code in catalog_codes:
        if catalog_code not in seen_codes:
            labels.write("{},{},{},{}\n".format(course_id, catalog_code, link_elem["href"], link_elem.text))
            download_links.append((course_id, link_elem["href"]))
            course_id += 1
            seen_codes.add(catalog_code)

labels.close()

if os.path.isdir(PAGES_DIR):
    shutil.rmtree(PAGES_DIR)
os.mkdir(PAGES_DIR)

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER_PATH)

for link in download_links:
    driver.get(link[1])
    time.sleep(1)
    html = driver.page_source
    file = open("{}/{}.html".format(PAGES_DIR, link[0]), 'w')
    file.write(html)
    file.close()

print("DONE")
