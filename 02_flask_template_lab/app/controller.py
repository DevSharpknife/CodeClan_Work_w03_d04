from app import app
from flask import render_template, request, redirect
from app.models.event_list import events, add_event
from app.models.event import *


@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events)


@app.route('/add-event', methods=['POST'])
def add_new_event():
    date = request.form['date']
    name = request.form['name']
    attendees = request.form['attendees']
    location = request.form['location']
    description = request.form['description']

    new_event = Event(date, name, attendees, location, description)
    add_event(new_event)

    return redirect('/')
