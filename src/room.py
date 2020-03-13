# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, key, items=[]):
        self.name = name
        self.description = description
        self.key = key
        self.items = items

    def inventory(self):
        print("Room's inventory has:")
        if self.items == []:
            print("no items!")
        else:   
            print(f'{self.items}')


    def __str__(self):
        # empty list
        if self.items == []:
            return f'{self.name}\n\n {self.description}\n\n This room has no items\n'
        else:
            item_names = ''
            for item in self.items:
                item_names += item.name + ' '
        # list with items
            return f'{self.name}\n\n {self.description}\n\n This room has the following items: {item_names}\n'
