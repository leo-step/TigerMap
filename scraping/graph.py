from collections import defaultdict
from files import *

code_to_id = {}
id_to_code = {}
labels = open(LABELS_FILE, 'r')
for line in labels.readlines():
    fields = line.split(',')
    id_to_code[int(fields[0])] = fields[1]
    code_to_id[fields[1]] = int(fields[0])

prereq_graph = defaultdict(lambda: [])
unlock_graph = defaultdict(lambda: [])
adjlist = open(ADJLIST_FILE, 'r')
for line in adjlist.readlines():
    fields = line.split(',')
    prereq_graph[int(fields[0])].append(int(fields[1]))
    unlock_graph[int(fields[1])].append(int(fields[0]))

# e.g. get all prereqs for COS 484 - nlp
# these are doing dfs right now but should be bfs probably?
# write these methods properly, possibility of duplicates
# need to maintain sets and stuff

def get_prereqs_wrapper(id):
    prereqs = []
    get_prereqs(id, prereqs)
    return prereqs

def get_prereqs(id, prereqs):
    class_prereqs = prereq_graph[id]
    prereqs.extend(class_prereqs)
    for class_prereq in class_prereqs:
        get_prereqs(class_prereq, prereqs)

def get_unlocks_wrapper(id):
    unlocks = []
    get_unlocks(id, unlocks)
    return unlocks

def get_unlocks(id, unlocks):
    class_unlocks = unlock_graph[id]
    unlocks.extend(class_unlocks)
    for class_prereq in class_unlocks:
        get_unlocks(class_prereq, unlocks)

while True:
    code = input("Enter a class code: ")
    print("Prereqs for {}: ".format(code), end='')
    print(list(map(lambda x: id_to_code[x], get_prereqs_wrapper(code_to_id[code]))))

    print("Unlocks for {}: ".format(code), end='')
    print(list(map(lambda x: id_to_code[x], get_unlocks_wrapper(code_to_id[code]))))