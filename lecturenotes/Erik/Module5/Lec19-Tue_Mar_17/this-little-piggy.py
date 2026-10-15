# this-little-piggy.py
import pygame


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CLOCK_TICK = 30
TITLE = "This Little Piggy"


def main():
    # Setup the pygame window and clock
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########
    piggy = pygame.image.load("Pig.PNG")
    # TODO: load the image of the pig into a variable
    # TODO: load the boing sound at 50% volume
    # TODO: load the background music
    # TODO: begin playing the background music at 20% volume

    ##########
    # Set up game data
    ##########
    x_pos = 240
    y_pos = 260
    RADIUS = 25
    x_dir = 14
    y_dir = 8

    ##########
    # Game Loop
    ##########
    game_over = False
    running = True
    while running:
        ##########
        # Get Input/Events
        ##########
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # User clicked the window's X button
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE and game_over:
                    ### Do Stuff to Reset Game ###
                    game_over = False

        ##########
        # Update state of components/data
        ##########
        #### Always Update ####
        x_pos += x_dir
        y_pos += y_dir

        # TODO: use the piggy's width in this calculation
        if x_pos + RADIUS >= SCREEN_WIDTH or x_pos - RADIUS <= 0:
            print("The piggy bounced off a side wall")
            x_dir = -x_dir
            # TODO: play the boing sound

        # TODO: use the piggy's height in this calculation
        if y_pos + RADIUS >= SCREEN_HEIGHT or y_pos - RADIUS <= 0:
            print("The piggy bounced off the top or bottom wall")
            y_dir = -y_dir
            # TODO: play the boing sound

        #### Update if Game is Not Over ####
        if not game_over:
            pass
        #### Update if Game is Over ####
        else:
            pass

        ##########
        # Update Display
        ##########
        #### Always Display ####
        screen.fill("white")  # Filling the screen wipes out any previous screen content
        # TODO: remove the circle, and instead blit the piggy onto the screen
        #pygame.draw.circle(screen, "black", (x_pos, y_pos), RADIUS)
        screen.blit(piggy, [x_pos, y_pos])

        pygame.display.flip()

        #### Display while Game is being played ####
        if not game_over:
            pass
        #### Display while Game is Over ####
        else:
            pass

        #### Draw changes the screen ####
        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)


main()
