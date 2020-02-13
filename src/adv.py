from room import Room
from player import Player
from item import Item

# Declare all the items

item_dic = {
    'sword': Item('sword','Use this for battle'),
    'axe': Item('axe','Use this for battle'),
    'coin': Item('coin', 'It is shiny!'),
    'potion': Item('potion', 'Restores 10 Health')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[item_dic['sword']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[item_dic['coin']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[item_dic['axe']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[item_dic['potion'], item_dic['coin']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[item_dic['coin']]),
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

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


starting_room = room['outside']
items = []
# Create Person object
name = input("Enter your name: ")
p1 = Player(name, starting_room, items)

# Error to print when user attempts to move in non existent room
error = "~~~You cannot go that way!~~~"

game_run = True
while game_run == True:
    print(p1.room)
    print("\n\tEnter 'n', 's', 'e', or 'w' to move\n\tEnter 'get [item]' to pick up an item or 'drop [item]' to drop it.\n\t(q to quit)")
    user_input = input("~~> ")
    print("________________________________________________________________________________________")

    # Game Logic

    # End Game
    if user_input == 'q':
        print("\nClosing Game...")
        exit()

    # Get an item
    elif 'get' in user_input:
        item_input = user_input.split(' ')[1]
        if item_dic[item_input] in p1.room.items:
            p1.items.append(item_dic[item_input]) # add to inventory
            p1.room.items.remove(item_dic[item_input]) # remove item from room
            print(f"{item_input} added!")
        else:
            print(f"~~~{item_input} not available~~~")

    # Drop an item
    elif 'drop' in user_input:
        item_input = user_input.split(' ')[1]
        if item_dic[item_input] in p1.room.items:
            p1.items.remove(item_dic[item_input])
            p1.room.items.append(item_dic[item_input])
        else:
            print(f"~~~{item_input} not available~~~")

    # Move rooms 
    elif user_input == 'n':
        if p1.room.n_to != None:
            p1.room = p1.room.n_to
        else:
            print(error)
    elif user_input == 's':
        if p1.room.s_to != None:
            p1.room = p1.room.s_to
        else:
            print(error)

    elif user_input == 'e':
        if p1.room.e_to != None:
            p1.room = p1.room.e_to
        else:
            print(error)

    elif user_input == 'w':
        if p1.room.w_to != None:
            p1.room = p1.room.w_to
        else:
            print(error)

    # Invalid input
    else:
        print("~~~input not valid~~~")