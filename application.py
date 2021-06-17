import git
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/about")
def about():
    return "This is the About page."


@app.route("/update_server", methods=["POST"])
def update_server():
    repo = git.Repo()
    origin = repo.remotes.origin
    origin.pull()
    return "success"
