class Event():
    def __init__(self, date, name, guest, room, description,recurring = False ):
        self.date = date
        self.name = name 
        self.guest = guest
        self.room = room
        self.description = description
        self.recurring = recurring


