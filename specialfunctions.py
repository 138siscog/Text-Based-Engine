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

def player_movement(action):
        if action != action_list:
            print("Action not recognized")
        elif action == "west":
            player_posx -= 1
        elif action == "east":
            player_posx += 1
        elif action == "north":
            player_pos -= 1
        elif action == "south":
            player_pos += 1