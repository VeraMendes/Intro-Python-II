from room import Room
from player import Player
from item import Item, Food
# import cmd
import textwrap
import sys
import os
# import time

# Declare all the items

item = {
    'flashlight': Item("flashlight", "This can be helpful during night time"),
    'knife': Item("knife", "This can help during hard situations"),
    'fish': Food("fish", "Eating this will give you energy", 200),
    'compass': Item("compass", "This will guide on your adventure"),
    'pet': Item("pet", "Your best friend!")
}


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     "outside", [item['pet'], item['knife']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "foyer"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "overlook"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "narrow"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "treasure")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#
def title_screen_selections():
    option = input(">>>")
    if option.lower().strip() == ("play"):
        start_game()
    elif option.lower().strip() == ("help"):
        help_menu()
    elif option.lower().strip() == ("quit"):
        sys.exit()
    while option.lower().strip() not in ["play", "help", "quit"]:
        print("Please enter a valid command.")
        option = input(">>>")
        if option.lower().strip() == ("play"):
            start_game()
        elif option.lower().strip() == ("help"):
            help_menu()
        elif option.lower().strip() == ("quit"):
            sys.exit()


def title_screen():
    os.system("clear")
    print("#################################")
    print("#Welcome to your Adventure Game!#")
    print("#################################")
    print("            - Play -             ")
    print("            - Help -             ")
    print("            - Quit -             ")
    print("#################################")
    title_screen_selections()

def help_menu():
    print("#################################")
    print("          Help Menu              ")
    print("#################################")
    print("Use n to go North, s to go South ")
    print("e to go East and w to go West    ")
    print("     write play or quit          ")
    print("   Use your commands to select   ")
    print("   Good luck and have fun!!!     ")
    title_screen_selections()


# Make a new player object that is currently in the 'outside' room.

def start_game():
    print("Enter your name")
    global name
    name = input(">>>")
    global myPlayer
    myPlayer = Player(name, room['outside'])
    start_location = room['outside']
    print (f"You are here -> {start_location}")


def move_to_room(direction):
    '''valid inputs = ['n', 's', 'e', 'w', 'q', 'get [item]', 'drop [item]' ]'''
    if direction == 'q':
        print("Goodbye!")
        sys.exit()

    try:

        if direction == 'n':
            myPlayer.current_room = room[myPlayer.current_room.key].n_to
            moving = True
        elif direction == 's':
            myPlayer.current_room = room[myPlayer.current_room.key].s_to
            moving = True
        elif direction == 'e':
            myPlayer.current_room = room[myPlayer.current_room.key].e_to
            moving = True
        elif direction == 'w':
            myPlayer.current_room = room[myPlayer.current_room.key].w_to
            moving = True

        # if players enters get [<item>], confirm item is valid
        # item is removed from room's list of items and added to player list of items
        elif direction.split(' ')[0] == 'get':
            item = direction[-1]
            if item in myPlayer.current_room.items:
                myPlayer.items.append(item)
                myPlayer.current_room.items.remove(item)
                print (f'You have picked up the {item}.')
                moving = True
            else:
                print('That is not a valid item.')

        elif direction.split(' ')[1] == 'drop':
            item = direction[-1]
            if item in myPlayer.items:
                myPlayer.items.remove(item)
                myPlayer.current_room.items.append(item)
                print(f'You have dropped the {item}.')
                moving = True
            else:
                print('That is not a valid item.')

        else:
            raise ValueError

        # if valid direction
        # print new player's current room name and description
        # new_location = myPlayer.current_room
        # print (f"\n You are here -> {new_location}")
        print (f"{myPlayer}")

    except ValueError:
        print("Not a valid direction!")

    except:
        print("No room in this direction!")
        


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

title_screen()

while(True):

    global moving
    moving = False

    print(f"Where would you like to go or what would you like to do in this room?\n")
    direction = input("move -> ").lower()
    move_to_room(direction)

    # if players enters get [<item>], confirm item is valid
    # item is removed from room's list of items and added to player list of items
    # if direction.split(' ')[0] == 'get':
    #     item = direction[4:]
    #     if item in myPlayer.current_room.items:
    #         myPlayer.items.append(item)
    #         myPlayer.current_room.items.remove(item)
    #         print (f'You have picked up the {item}.')
    #         moving = True
    #     else:
    #         print('That is not a valid item.')


    # if direction.split(' ')[1] == 'drop':
    #     item = direction[5:]
    #     if item in myPlayer.items:
    #         myPlayer.items.remove(item)
    #         myPlayer.current_room.items.append(item)
    #         print(f'You have dropped the {item}.')
    #     else:
    #         print('That is not a valid item.')
