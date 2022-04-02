from collections import defaultdict
from queue import Queue

class CourseGraph:
    def __init__(self, adjlist_file_path):
        self.prereq_graph = defaultdict(lambda: [])
        self.unlock_graph = defaultdict(lambda: [])
        adjlist = open(adjlist_file_path, 'r')
        for line in adjlist.readlines():
            fields = line.split(',')
            self.prereq_graph[int(fields[0])].append(int(fields[1]))
            self.unlock_graph[int(fields[1])].append(int(fields[0]))
    def get_prereqs(self, id):
        prereqs = []
        id_queue = Queue()
        seen = set()
        id_queue.put(id)
        while not id_queue.empty():
            course_id = id_queue.get()
            for prereq in self.prereq_graph[course_id]:
                if prereq not in seen:
                    id_queue.put(prereq)
                    seen.add(prereq)
                    prereqs.append(prereq)
        return prereqs
    def get_unlocks(self, id):
        return self.unlock_graph[id]