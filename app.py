from flask import Flask, request
from coursegraph import CourseGraph

app = Flask(__name__)

course_graph = CourseGraph("adjlist.txt")

code_to_id = {}
id_to_code = {}
labels = open("labels.txt", 'r')
for line in labels.readlines():
    fields = line.split(',')
    id_to_code[int(fields[0])] = fields[1]
    code_to_id[fields[1]] = int(fields[0])

@app.route("/")
def index():
    return str(list(map(lambda x: id_to_code[x], course_graph.get_prereqs(code_to_id["COS 324"]))))

if __name__ == "__main__":
    app.run()