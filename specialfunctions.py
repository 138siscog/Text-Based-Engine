import os
from actions import action_list
from actions import inventory_list


# quick clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#drawing the grid
def draw_map(grid):
    for row in grid:
        print(" ".join(row))

# movement
def player_movement(action,x,y,grid):
    if action not in action_list:
        print("not Found")
        return x, y
    # what each action does
    new_x, new_y = x, y
    if action == "west":
        new_x -= 1
    elif action == "east":
        new_x += 1
    elif action == "north":
        new_y -= 1
    elif action == "south":
        new_y += 1
    elif action == "list":
        print(action_list)
    elif action == "inventory":
        print(inventory_list)
    
    # Check bounds + walls
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0
    if 0 <= new_x < width and 0 <= new_y < height and grid[new_y][new_x] != "x":
        grid[y][x] = "o"
        
        grid[new_y][new_x] = "@"
        return new_x, new_y
    else:
        print("You cannot go that way")
        return x, y
    
