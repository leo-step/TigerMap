from coursegraph import CourseGraph
from dotenv import load_dotenv
from flask import Flask, request
import pymongo
import os

load_dotenv()

app = Flask(__name__, static_folder='frontend/build', static_url_path='/')
app.secret_key = os.getenv("APP_SECRET_KEY")

db = pymongo.MongoClient(os.getenv("DB_CONN_STRING")).courses
course_graph = CourseGraph(db.graphs.find_one({"_id": "prereq"}),
                           db.graphs.find_one({"_id": "unlock"}))

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/api", methods=["POST"])
def api():
    try:
        code = request.get_json()["code"]
        course = db.data.find_one({"code": code})
        if not course:
            return {"course": None, "prereqs": None, "unlocks": None}
        id = course["_id"]
        prereq_ids = course_graph.get_prereqs(id)
        unlock_ids = course_graph.get_unlocks(id)
        prereqs = list(db.data.find({"_id": { "$in": prereq_ids }}))
        unlocks = list(db.data.find({"_id": { "$in": unlock_ids }}))
        return {"course": course, "prereqs": prereqs, "unlocks": unlocks}
    except:
        return {}

if __name__ == "__main__":
    app.run()