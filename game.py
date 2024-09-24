import pygame as pg
import time as t
import random as ran

# all of the imports and such

# now, making a window
width, height = 600, 400
# setting it so that the window will be displayed
window = pg.display.set_mode((width, height))
# setting the name of the window
pg.display.set_caption("Game Tester")


# to keep the game running for as long as the
# character is alive, we need a while-loop
# For the sake of testing, the while loop will work
# while there have not been any collisions, etc.
def main() : 
    # using the run variable, we can change it to 
    # false whenever the character dies
    run = True
    while run:
        # this keeps track of all events that
        # have occurred thus far??
        # NEW INFO. Keeps track of user input
        # the even equalling pg.quit is when
        # the user has entered that X button on the top
        # corner! 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
        
    # once we've broken out of the loop, 
    # the game is over.
    pg.quit()

# so now that we have made the main function
# we need to make it available to be called.
if __name__ == "__main__":
    main()