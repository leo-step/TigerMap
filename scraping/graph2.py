from files import ADJLIST_FILE, LABELS_FILE
from coursegraph import CourseGraph

code_to_id = {}
id_to_code = {}
labels = open(LABELS_FILE, 'r')
for line in labels.readlines():
    fields = line.split(',')
    id_to_code[int(fields[0])] = fields[1]
    code_to_id[fields[1]] = int(fields[0])

graph = CourseGraph(ADJLIST_FILE)

while True:
    code = input("Enter a class code: ")
    print("Prereqs for {}: ".format(code), end='')
    print(list(map(lambda x: id_to_code[x], graph.get_prereqs(code_to_id[code]))))

    print("Unlocks for {}: ".format(code), end='')
    print(list(map(lambda x: id_to_code[x], graph.get_unlocks(code_to_id[code]))))