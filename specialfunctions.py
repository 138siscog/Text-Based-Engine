import os
from actions import action_list


# quick clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#drawing the grid
def draw_map(grid):
    for row in grid:
        print(" ".join(row))

# movement
def player_movement(action,x,y,grid):
    old_x, old_y = x, y
    if action not in action_list:
        print("not Found")
    elif action == "west":
        x -= 1
    elif action == "east":
        x += 1
    elif action == "north":
        y -= 1
    elif action == "south":
        y += 1
    grid[old_y][old_x] = "."
    grid[y][x] = "@"
    return x,y