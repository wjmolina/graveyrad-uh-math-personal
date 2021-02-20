import git
from flask import Blueprint, render_template
from flask.globals import request
from flask.helpers import flash, url_for
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from . import db
from .models import Problem, User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    problems = Problem.query.all()
    return render_template('index.html', problems=sorted(problems, key=lambda problem: problem.difficulty))


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@main.route('/problem/<id>')
def problem(id):
    return render_template('problem.html', problem=Problem.query.filter_by(id=id).first())


@main.route('/problem/<id>', methods=['POST'])
def problem_post(id):
    problem = Problem.query.filter_by(id=id).first()
    if problem.answer == request.form.get('answer'):
        current_user.problems.append(problem)
        db.session.commit()
        flash('Success!', 'is-info')
    else:
        flash('Try Again', 'is-danger')
    return render_template('problem.html', problem=Problem.query.filter_by(id=id).first())


@main.route('/create_problem')
@login_required
def create_problem():
    if current_user.id == 1:
        return render_template('create_problem.html')
    return redirect(url_for('main.index'))


@main.route('/create_problem', methods=['POST'])
@login_required
def create_problem_post():
    if current_user.id == 1:
        db.session.add(Problem(
            title=request.form['title'],
            text=request.form['text'],
            answer=request.form['answer'],
            difficulty=request.form['difficulty'],
        ))
        db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/update_server', methods=['POST'])
def webhook():
    repo = git.Repo('EsXAcademy')
    origin = repo.remotes.origin
    origin.pull()
    return 'successful webhook'


@main.route('/leaderboard')
def leaderboard():
    people = sorted(
        User.query.all(),
        key=lambda person: len(person.problems),
        reverse=True
    )
    return render_template('leaderboard.html', people=people)
