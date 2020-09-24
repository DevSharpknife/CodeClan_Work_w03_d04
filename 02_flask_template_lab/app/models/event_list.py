from app.models.event import *



event_1 = Event("2020-09-25", "Codeclan Lab", 2, "CodeClan HQ", "bumbling along nicely")
event_2 = Event("2020-09-26", "CodeClan Remote", 17, "Home", "all done on zoom")
events = [event_1, event_2]

def add_event(event):
    events.append(event)