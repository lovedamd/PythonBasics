import pygame as pg
import time as t
import random as ran


# the time thing may have been confusing
# but we imported it for a reason
# Since some computers have a lot
# more hertz per second than others
# time is not regulated equally across
# all systems. So we use the time lib
# to regulate the timing of our game and
# keep things at a simple pace (was way too fast!!)

# all of the imports and such

# now, making a window
width, height = 600, 600
# setting it so that the window will be displayed
window = pg.display.set_mode((width, height))
# setting the name of the window
pg.display.set_caption("Game Tester")


# making an easy constant variable
# for the player object's velocity
playerVel = 5

# now we get to add a background image.
BG = pg.image.load("background.jpg")
# since my image was taken from my phone
# i needed to not only change the size
# but also rotate it
# fortunately, it was easy enough to do, 
# since pygame has those methods available
BG = pg.transform.scale(BG, (width, height))

# you can also call the scale method as this:
# BG = pg.transform.scale(pg.image.load("background.jpg"), 
#   (width, height))
BG = pg.transform.rotate(BG, -90)


# now we finally get to make our character.
# I want to make it a tractor, so I'm going
# to take some time to make a pixellated
# tractor image.
tract = pg.image.load("tractor.png")
# making the white in the tractor transparent, 
# so the background does not exist
tract.set_colorkey((255,255,255))
tract_width = 40
tract_height = 40

def draw(player) :
    # setting the image, and then 
    # the two different numbers set the
    # sizing of the image. The 0, 0
    # means that it will fill the full
    # size of the window.
    window.blit(BG, (0, 0))

    # use this to draw the player image
    # colors can be given in string, 
    # since python was updated recently
    pg.draw.rect(window, "yellow", player)


    pg.display.update()
    # Now we update the window.



# to keep the game running for as long as the
# character is alive, we need a while-loop
# For the sake of testing, the while loop will work
# while there have not been any collisions, etc.
def main() : 
    # subtracting the tractheight from height
    # gives it a position at the bottom of the 
    # screen to start with
    player = pg.Rect((300, height - tract_height, tract_width, tract_height))
    # parameters = X position, Y position, width, height


    # make a clock outside of the while loop
    # that way we can control the speed of the
    # loop and make it easier to move the 
    # character
    clock = pg.time.Clock()

    # using the run variable, we can change it to 
    # false whenever the character dies
    run = True
    while run:

        clock.tick(60)

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
        draw(player)
        
        # now to move the rectangle, we
        # just set the X coordinate of player
        # to adjust as necessary
        keys = pg.key.get_pressed()

        # if they press the left or right
        # button, we can figure that out
        # and then move the character accordingly
        if keys[pg.K_LEFT] and player.x - playerVel >= 0:
            player.x -= playerVel
        elif keys[pg.K_RIGHT] and player.x + playerVel + player.width <= width:
            player.x += playerVel
    

    # once we've broken out of the loop, 
    # the game is over.
    pg.quit()

# so now that we have made the main function
# we need to make it available to be called.
if __name__ == "__main__":
    main()