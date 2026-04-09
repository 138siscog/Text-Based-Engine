## This is a basic dungeon crawling engine, it works on a grid system very much like zork

## Currently you are able to move between all rooms in the 5x5 grid created, 

## actions.py has all the control actions like north, south, ect. you can add mode actions as needed but they will need to be defined 

## The main.py file has the main loop in the game, it stores chracter name, prints the grid system and updates as you move

## rooms.py currently holds the grid system, eventually i will start adding room descriptions using a coordinate system (x,y) essentiall if location == (x,y) print(room description)

## special functins currently holds the functions i create so i can have them all in one place and call back as needed

######

## Fixes, i need to ensure that i set a wall boundary so player cannot go outside of the grid for now, i also want to make pathed rooms, if there is a room i dont want players to axis ill make the update so that the player does not move and you get the message "you cannot go that way" 

## Later Features ##

# keys to open rooms (single use keys)
# enemays with combat system much like a turnbase game
# player health
# enemy health 
# weapon / shield stats update (probablity of landing a hit increases / decreases)
# boss fights

####################################################################################################

Update 2. 04/07/2026

## boundary of player now works, if you try to go outside of boundary you will get a (you can't go that way) message instead of the code 

## you are now able to set wall coordinates using "x" to mark the walls you will not be able to move through them, currently the walls are hard coded into the main.py 

####################################################################################################

Update 3. 04/09/2026

## light day today, added some comments explaining the code, looking into adding character stats that will increase with items you pick up still researching how to do this effectively 
