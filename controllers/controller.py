from flask import render_template, request, redirect
from app import app
from models.event_list import events
from models.event import Event

@app.route("/events")
def index():
    return render_template("index.html", title="Events", events=events)

@app.route("/planner")
def planner():
    return render_template("planner.html", title="Event Planner")
