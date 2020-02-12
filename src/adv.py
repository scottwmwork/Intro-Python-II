from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Create Person object
name = input("Enter your name: ")
p1 = Player(name, starting_room)

# Inputs the user can use
valid = ['n', 's', 'e', 'w', 'q']

# Error to print when user attempts to move in non existent room
error = "Room does not exist, please try another direction"

# print starting_room
print(p1.room.description)

game_run = True
while game_run == True:

    print("Enter n, s, e, or w (q to quit)")
    user_input = input("~~>")
    print("---------------------------------------")
    if user_input in valid:

        # Game Logic
        if user_input == 'n':
            
            try:
                p1.room = p1.room.n_to
                print(p1.room)
            except:
                print(error)
            
        elif user_input == 's':

            try:
                p1.room = p1.room.s_to
                print(p1.room)
            except:
                print(error)

        elif user_input == 'e':

            try:
                p1.room = p1.room.e_to
                print(p1.room)
            except:
                print(error)

        elif user_input == 'w':
            try:
                p1.room = p1.room.w_to
                print(p1.room)
            except:
                print(error)

        # End Game
        if user_input == 'q':
            print("\nClosing Game...")
            exit()