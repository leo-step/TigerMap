from flask import Flask, request
import mysql.connector
import os
from coursegraph import CourseGraph
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='frontend/build', static_url_path='/')
app.secret_key = os.getenv("APP_SECRET_KEY")

course_graph = CourseGraph(os.path.dirname(os.path.realpath(__file__)) + "/adjlist.txt")

@app.route("/")
def index():
    return app.send_static_file("index.html")

# clean this method up
def call_proc(name, args=[]):
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
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
    try:
        code = request.get_json()["code"]
        course_data = call_proc("get_course_data", [code])
        if not course_data:
            return {"course": None, "prereqs": None, "unlocks": None}
        id = course_data[0]["id"]
        prereqs = [str(i) for i in course_graph.get_prereqs(id)]
        unlocks = [str(i) for i in course_graph.get_unlocks(id)]
        prereqs_data = call_proc("get_courses_data", [','.join(prereqs)])
        unlocks_data = call_proc("get_courses_data", [','.join(unlocks)])
        return {"course": course_data[0], "prereqs": prereqs_data, "unlocks": unlocks_data}
    except:
        return {}

if __name__ == "__main__":
    app.run()