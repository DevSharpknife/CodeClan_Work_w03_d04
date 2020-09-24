from app import app
from flask import render_template
from app.models.todo_list import tasks


@app.route('/')
def index():
    return render_template('index.html', title='Home', tasks=tasks)