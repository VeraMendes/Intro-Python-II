# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, key):
        self.name = name
        self.description = description
        self.key = key

    def __repr__(self):
        return f'{self.name}, {self.description}'
