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
x = 2
y = 4
player_posx = [x]
player_posy = [y]
grid[y][x] = "@"
draw_map(grid)

running = True
while True:
    action = input("What would you like to do?").lower().strip()
    clear_screen()
    x,y = player_movement(action,x,y,grid)
    draw_map(grid)

 


