import git
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/update_server", methods=["POST"])
def webhook():
    repo = git.Repo("EsXAcademy")
    origin = repo.remotes.origin
    origin.pull()
    return "success"
