# Implement a class to hold item information. This should have name and
# description attributes.

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return self.name

class Food(Item):
    def __init__(self, name, description, energy):
        super().__init__(name, description)
        self.energy = energy
    

