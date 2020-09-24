from app import app
from flask import render_template, request, redirect
from app.models.todo_list import tasks, add_new_task
from app.models.task import *


@app.route('/')
def index():
    return render_template('index.html', title='Home', tasks=tasks)


@app.route('/add-task', methods=['POST'])
def add_task():
    task_title = request.form['title']
    task_description = request.form['description']

    new_task = Task(task_title, task_description, False)
    add_new_task(new_task)

    return redirect('/')

