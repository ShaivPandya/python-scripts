# Machine user login tracking script

# Event class contains
    # the date when the event happened,
    # the name of the machine where it happened,
    # the user involved,
    # and the event type (login and logout)

# Attributes
    # Date
    # User
    # Machine
    # Type (string)
        # Login
        # Logout

def get_event_date(event):
    return event.date
    
def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        if event.user in machines[event.machine]:
            if event.type == "logout":
                machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

with open("events.txt", "r") as f:
    events = f.readlines()

"""
# Sample set of events

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]
"""

users = current_users(events)
generate_report(users)
