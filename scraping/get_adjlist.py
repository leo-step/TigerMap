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

if os.path.exists(ADJLIST_FILE):
    os.remove(ADJLIST_FILE)

adjlist = open(ADJLIST_FILE, 'w')
code_pattern = re.compile(r"[A-Z][A-Z][A-Z] \d\d\d")
no_space_pattern = re.compile(r"[A-Z][A-Z][A-Z]\d\d\d")
for path in os.listdir(PAGES_DIR):
    course = open(PAGES_DIR + '/' + path, 'r')
    soup = bs4.BeautifulSoup(course.read(), features="lxml")
    prereqs_div = soup.find("div", {"class": "prereqs-and-other-restrictions"})
    if prereqs_div:
        first_sentence = prereqs_div.find("span").text.split('.')[0]
        prereqs = code_pattern.findall(first_sentence)
        no_space = no_space_pattern.findall(first_sentence)
        prereqs.extend(list(map(lambda x: x[:3] + ' ' + x[3:], no_space)))
        for prereq in prereqs:
            course_id = int(path[:-5])
            if prereq == id_to_code[course_id]:
                continue
            elif prereq in code_to_id:
                adjlist.write("{},{}\n".format(course_id, code_to_id[prereq]))
            else:
                print(prereq + " not found")
    course.close()
adjlist.close()