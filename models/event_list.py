from models.event import *
import datetime

event1 = Event(
    datetime.date(2023, 6, 16),
    "Board Game Friday",
    20,
    "Library",
    "An evening of board game madness! Bring your own games or choose some from the library's stock!",
    True
    )

event2 = Event(
    datetime.date(2023, 6, 21),
    "Summer Solstice 2023",
    100,
    "Campus Gardens",
    "Celebrate midsummer the pagan way - an interactive day of games, performances, and much more!",
    False
)

events = [event1, event2]

def add_new_event(event):
    events.append(event)