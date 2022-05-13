from collections import defaultdict
from queue import Queue

class CourseGraph:
    def __init__(self, prereq, unlock):
        self.prereq_graph = defaultdict(lambda: [])
        self.unlock_graph = defaultdict(lambda: [])
        for edge in prereq["adjlist"]:
            self.prereq_graph[edge[0]].append(edge[1])
        for edge in unlock["adjlist"]:
            self.unlock_graph[edge[0]].append(edge[1])
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