from flask import render_template, request, redirect
from app import app
from models.event_list import events, add_new_event
from models.event import Event
import datetime

@app.route("/events")
def index():
    return render_template("index.html", title="Events", events=events)

@app.route("/planner")
def planner():
    return render_template("planner.html", title="Event Planner")

@app.route("/events", methods=["POST"])
def add_event():
    event_date = request.form["date"]
    split_date = event_date.split("-")
    formatted_date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    event_name = request.form["name"]
    guest_number = request.form["guests"]
    event_location = request.form["location"]
    event_desc = request.form["description"]
    recurring_event = False
    if request.form.get("recurring"):
        recurring_event = True
    new_event = Event(formatted_date, event_name, guest_number, event_location, event_desc, recurring_event)
    add_new_event(new_event)
    return redirect("/events")

@app.route("/events/<index>")
def view_event(index):
    single_event = events[int(index)]
    return render_template("event.html", title="Event details", event=single_event)