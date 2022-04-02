from flask import Flask, request
from flask_cors import CORS
from coursegraph import CourseGraph
from secrets import *

app = Flask(__name__, static_folder='frontend/build', static_url_path='/')
app.secret_key = APP_SECRET_KEY
CORS(app) #comment this on deployment
'''
course_graph = CourseGraph("adjlist.txt")

code_to_id = {}
id_to_code = {}
labels = open("labels.txt", 'r')
for line in labels.readlines():
    fields = line.split(',')
    id_to_code[int(fields[0])] = fields[1]
    code_to_id[fields[1]] = int(fields[0])
'''

@app.route("/")
def index():
    return app.send_static_file("index.html")
    #return str(list(map(lambda x: id_to_code[x], course_graph.get_prereqs(code_to_id["COS 324"]))))

if __name__ == "__main__":
    app.run()