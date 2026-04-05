from specialfunctions import clear_screen
from specialfunctions import draw_map
from specialfunctions import player_movement
from rooms import grid
import sys

print("Welcome to 'This Game'")

input("Press Enter")

clear_screen()

print("What is your name young Hero?")
char_name = input("Enter your Name: ")
print("\n")
input(f"Wlcome {char_name}, press enter to begin your journey!...")

# Player Starting Point
x = 4
y = 2
player_posx = [x]
player_posy = [y]
grid[player_posx[0]][player_posy[0]] = "@"

running = True
while True:

    draw_map(grid)
    action = input("What would you like to do?")
    player_movement(action)
    draw_map(grid)
    input("press enter")
 


