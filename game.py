import pygame as pg
import time as t
import random as ran

# all of the imports and such

# now, making a window
width, height = 600, 600
# setting it so that the window will be displayed
window = pg.display.set_mode((width, height))
# setting the name of the window
pg.display.set_caption("Game Tester")


# now we get to add a background image.
BG = pg.image.load("background.jpg")
# since my image was taken from my phone
# i needed to not only change the size
# but also rotate it
# fortunately, it was easy enough to do, 
# since pygame has those methods available
BG = pg.transform.scale(BG, (600, 600))

# you can also call the scale method as this:
# BG = pg.transform.scale(pg.image.load("background.jpg"), 
#   (width, height))
BG = pg.transform.rotate(BG, -90)

def draw() :
    # setting the image, and then 
    # the two different numbers set the
    # sizing of the image. The 0, 0
    # means that it will fill the full
    # size of the window.
    window.blit(BG, (0, 0))
    pg.display.update()
    # Now we update the window.



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

        # now we display the background
        draw()
        
    # once we've broken out of the loop, 
    # the game is over.
    pg.quit()

# so now that we have made the main function
# we need to make it available to be called.
if __name__ == "__main__":
    main()