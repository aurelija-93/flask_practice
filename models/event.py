class Event:
    def __init__(self, date, name, guest_number, location, description, recurring):
        self.date = date
        self.name = name
        self.guest_number = guest_number
        self.location = location
        self.description = description
        self.recurring = recurring