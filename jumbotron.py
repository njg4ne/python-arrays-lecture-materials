# Jumbotron Simulator

# Prompt: The art students at a local high school want to make animations
# on the football field's jumbotron. It is a 9x16 pixel screen. Simulate
# animation functions that draw and remove a variable width border and
# move a dot randomly around the screen.

# https://tinyurl.com/yndtbszu
# Get a random number within a range
from random import randint as random_integer

# --------------------------------------------------------------------------------
# -----------------------IMPLEMENTATION-GOES-BELOW--------------------------------
# Emojis for on and off pixels
ON = "⬜"
OFF = "⬛"
# fmt: off
pixel_grid = [
    [OFF, OFF, OFF], 
    [OFF, OFF, OFF], 
    [OFF, OFF, OFF]
]
# fmt: on

# H x W screen
HEIGHT = 5
WIDTH = 5
# pixel_grid = [[OFF for _ in range(WIDTH)] for __ in range(HEIGHT)]


# Edit this function to change what happens every frame
def edit_pixel_grid():
    global pixel_grid


# Pseudocode of how edit_pixel_grid is called:
"""
loop forever
    call edit_pixel_grid
    print pixel_grid to terminal
    pause for half second
    clear the terminal
"""


# -----------------------IMPLEMENTATION-GOES-ABOVE--------------------------------
# --------------------------------------------------------------------------------
# Function to clear the terminal
import os, time

clear_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
# Function to print the current pixel grid
print_string_grid = lambda: [print("".join(row)) for row in pixel_grid]
# Main loop to update and display the jumbotron
while True:
    edit_pixel_grid()
    print_string_grid()
    time.sleep(1 / 2)  # pause for half second
    clear_terminal()
