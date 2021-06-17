import os

import git
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

try:
    app.config.from_object("config")
except:
    app.config.from_object("default_config")

db = SQLAlchemy(app)

from models import Comment, User

for sql_file_name in sorted(os.listdir("sql")):
    with open(f"sql/{sql_file_name}") as sql_file:
        db.engine.execute(sql_file.read())


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST" and (body := request.form["body"].strip()):
        Comment.save_from_dict(
            {
                "user_id": User.query.filter_by(ip=request.form["ip"]).first()._id,
                "body": body,
            }
        )

    return render_template(
        "index.html", comments=Comment.query.order_by(Comment.updated_at.desc())
    )


@app.route("/update_server", methods=["POST"])
def update_server():
    git.Repo().remotes.origin.pull()

    return "success"


@app.route("/save_user", methods=["POST"])
def save_user():
    data = requests.get(f"http://ip-api.com/json/{request.form['ip']}").json()
    data["_as"] = data.pop("as")
    data["ip"] = data.pop("query")

    if user := User.query.filter_by(ip=data["ip"]).first():
        data["_id"] = user._id

    User.save_from_dict(data)

    return "success"
