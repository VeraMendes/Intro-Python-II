# Write a class to hold player information, e.g. what room they are in
# currently.

class Player ():
    def __init__(self, name, current_room, items =[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def inventory(self):
        print("Your inventory has:")
        if self.items == []:
            print("No items!")
        else:   
            print(f'{self.items}')

    
    # def __str__(self):
    #     return f'\n{self.name}\n\n You are at:{self.current_room} and you have the following items {self.items}.\n\n'


    def __str__(self):
        # empty list
        if self.items == []:
            return f'\n{self.name}\n\n You are at:{self.current_room}\n and you have no items.\n'
        else:
            item_names = ''
            for item in self.items:
                item_names += item.name + ' '
            # list with items
            return f'\n{self.name}\n\n You are at:{self.current_room}\n\n You have the following items: {item_names}\n'