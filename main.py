from specialfunctions import clear_screen
from specialfunctions import draw_map
from specialfunctions import player_movement
from rooms import grid
import sys

# placeholder would like to a splash screen 
print("Welcome to 'This Game'")

input("Press Enter")

clear_screen()

print("What is your name young Hero?")
char_name = input("Enter your Name: ")
print("\n")
input(f"Welcome {char_name}, press enter to begin your journey!...")

# Player Starting Point
x = 2
y = 4
player_posx = [x]
player_posy = [y]

# character representation
grid[y][x] = "@"

# wall locations
grid[2][0] = "x"
grid[2][1] = "x"
grid[2][3] = "x"
grid[2][4] = "x"
grid[1][1] = "x"
grid[1][3] = "x"
grid[2][3] = "x"
grid[3][1] = "x"
grid[3][3] = "x"

# Initial map print
draw_map(grid)

running = True
while True:
    action = input("What would you like to do?\n").lower().strip()
    clear_screen()
    # this handles the player movement / actions such as north, west, south, east, inventory ect.
    x,y = player_movement(action,x,y,grid)
    # re draws updated map with no character coordinates
    draw_map(grid)


