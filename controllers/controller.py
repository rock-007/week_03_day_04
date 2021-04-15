from flask import render_template, request
from app import app
from models.all_events import *
from models.event import Event


@app.route ('/')
def index():
    return render_template("index.html",title="Events", all_events=all_events)

@app.route('/', methods=["POST"])

def add_event():
    print(request.form)
    new_name = request.form['name']
    new_date = str(request.form['date'])
    new_guest = request.form['guest']
    new_room = request.form['room']
    new_desc = request.form['description']

    new_added_event = Event(new_date, new_name, new_guest, new_room, new_desc )
    add_new_event(new_added_event)

    return render_template('index.html', title="Events", all_events= all_events)

    
