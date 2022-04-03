from flask import Flask, request
from flask_cors import CORS
import mysql.connector
import os
from coursegraph import CourseGraph
# from secrets import *

app = Flask(__name__, static_folder='frontend/build', static_url_path='/')
app.secret_key = os.environ.get("APP_SECRET_KEY")
# CORS(app) #comment this on deployment

course_graph = CourseGraph("../adjlist.txt")

@app.route("/")
def index():
    return app.send_static_file("index.html")

def call_proc(name, args=[]):
    db = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    cursor = db.cursor()
    cursor.callproc(name, args)
    db.commit()
    result = None
    for stored_result in cursor.stored_results():
        result = stored_result
        break
    output = []
    if result:
        columns = [data[0] for data in result.description]
        for row in result.fetchall():
            output.append(dict(zip(columns, row)))
    return output

@app.route("/api", methods=["POST"])
def api():
    code = request.get_json()["code"] # needs validation
    course_data = call_proc("get_course_data", [code])[0]
    id = course_data["id"] # what happens if course doesn't exist
    prereqs = [str(i) for i in course_graph.get_prereqs(id)]
    unlocks = [str(i) for i in course_graph.get_unlocks(id)]
    prereqs_data = call_proc("get_courses_data", [','.join(prereqs)])
    unlocks_data = call_proc("get_courses_data", [','.join(unlocks)])
    return {"course": course_data, "prereqs": prereqs_data, "unlocks": unlocks_data}

if __name__ == "__main__":
    app.run()