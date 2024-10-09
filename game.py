import pygame as pg
import time as t
import random as rand
pg.font.init()

# all of the imports and such

# now, making a window
width, height = 600, 600
window = pg.display.set_mode((width, height))
pg.display.set_caption("Game Tester")

# making constant variables for velocities
playerVel = 5
moo_vel = 3
shot_vel = 3

# dimensions for the cows and shots
cow_height = 80
cow_width = 80
shot_h = 15
shot_w = 10
meat_h = 25
meat_w = 25

# loading the images with transparency support
cow = pg.image.load("goodyCow.png").convert_alpha()  # Use .convert_alpha() for transparency
cow = pg.transform.scale(cow, (cow_width, cow_height))

meat = pg.image.load("transMeat.png").convert_alpha()  # Use .convert_alpha() for transparency
meat = pg.transform.scale(meat, (meat_h, meat_w))


BG = pg.image.load("goodGrass.jpg")
BG = pg.transform.scale(BG, (width, height))

tract = pg.image.load("goodTract.jpg")
tract.set_colorkey((255, 255, 255))
tract_width = 60
tract_height = 60
tract = pg.transform.scale(tract, (tract_width, tract_height))

# initializing the font
font = pg.font.SysFont("comic-sans", 30)

# making a boolean to keep track of when the tractor gets hit
global hit
hit = False

# draw function remains unchanged
def draw(player, elapsed_time, cowz, shots, meatz, score):
    window.blit(BG, (0, 0))
    t_text = font.render(f"Time: {round(elapsed_time)}s", 1, "white")
    window.blit(t_text, (10, 10))
    window.blit(tract, (player.x, player.y))
    score_t = font.render(f"Score: {score}", 1, "white")
    window.blit(score_t, (10, 40))

    # drawing cows and shots
    for moo in cowz:
        window.blit(cow, (moo.x, moo.y))
    for shot in shots:
        pg.draw.rect(window, "black", shot)
    for meaty in meatz:
        window.blit(meat, (meaty.x, meaty.y))

    pg.display.update()

def cowChecker(cowz, player, shots, meatz):
    global hit
    cows_to_remove = []
    shots_to_remove = []

    for moo in cowz:
        moo.y += moo_vel  # Move the cow down the screen

        if moo.y > height:  # Remove cows that go off the screen
            cows_to_remove.append(moo)
        elif moo.colliderect(player):  # Player hit by cow
            cows_to_remove.append(moo)
            hit = True

        # Move the cow closer to the player's x position
        if player.x < moo.x:
            moo.x -= moo_vel
        elif player.x > moo.x:
            moo.x += moo_vel

        # Check if a shot hit a cow
        for shot in shots:
            if shot.colliderect(moo):
                cows_to_remove.append(moo)
                shots_to_remove.append(shot)

    # Remove cows and shots after iteration to avoid modifying lists during iteration
    for moo in cows_to_remove:
        if moo in cowz:
            meatDrop(moo, meatz)
            cowz.remove(moo)

    for shot in shots_to_remove:
        if shot in shots:
            shots.remove(shot)


def meatDrop(moo, meatz) :
    meaty = pg.Rect(moo.x, moo.y, meat_w, meat_h)
    meatz.append(meaty)


# UPDATED spawnShot to correctly place bullets
def spawnShot(player, shots):
    shot_x = player.x + player.width // 2 - shot_w // 2
    shot_y = player.y  # Correct bullet position to player's y
    shot = pg.Rect(shot_x, shot_y, shot_w, shot_h)
    shots.append(shot)

def shotChecker(shots):
    for shot in shots[:]:  # Copy the list to avoid modification issues
        shot.y -= shot_vel  # Move the shot upwards
        if shot.y < 0:  # Remove the shot if it goes off the top of the screen
            shots.remove(shot)

def meatChecker(player, meatz, score):
    for meaty in meatz[:]:  # Copy the list to avoid modification issues
        if player.colliderect(meaty):  # Player touches the meat
            meatz.remove(meaty)  # Remove the meat
            score += 100
    return score



# main loop
def main():
    player = pg.Rect(300, height - tract_height, tract_width, tract_height)
    start_time = t.time()
    elapsed_time = 0
    clock = pg.time.Clock()
    
    cow_add_inc = 2000
    cow_count = 0
    cowz = []
    shots = []
    meatz = []
    score = 0
    run = True

    while run:
        cow_count += clock.tick(60)
        if cow_count > cow_add_inc:
            for _ in range(3):
                cow_x = rand.randint(-width, width)
                moo = pg.Rect(cow_x, -cow_height, cow_width, cow_height)
                cowz.append(moo)
            cow_add_inc = max(200, cow_add_inc - 50)
            cow_count = 0

        elapsed_time = t.time() - start_time
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break

        # check cows and shots
        cowChecker(cowz, player, shots, meatz)

        # checking if the player got some meat
        score = meatChecker(player, meatz, score)

        if hit:
            lost_text = font.render("You got Mooed", 1, "white")
            window.blit(lost_text, (width/2 - lost_text.get_width()/2, height/2 - lost_text.get_height()/2))
            pg.display.update()
            pg.time.delay(2000)
            break

        draw(player, elapsed_time, cowz, shots, meatz, score)

        # player movement
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and player.x - playerVel >= 0:
            player.x -= playerVel
        if keys[pg.K_RIGHT] and player.x + playerVel + player.width <= width:
            player.x += playerVel
        if keys[pg.K_DOWN] and player.y + playerVel + player.height <= height:
            player.y += playerVel
        if keys[pg.K_UP] and player.y - playerVel >= 0:
            player.y -= playerVel
        if keys[pg.K_a]:
            spawnShot(player, shots)

        shotChecker(shots)

    pg.quit()

# main function call
if __name__ == "__main__":
    main()
