# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    n_to = ''
    s_to = ''
    e_to = ''
    w_to = ''
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f"Room: {self.name}\nDescription: {self.description}\nItems in Room: {[item.name for item in self.items]}"