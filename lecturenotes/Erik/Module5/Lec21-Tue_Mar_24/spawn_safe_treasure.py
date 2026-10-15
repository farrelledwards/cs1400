# spawn_safe_treasure.py
import pygame
import random


SCREEN_WIDTH = 1280  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 720
CLOCK_TICK = 10
TITLE = "Spawn-Safe Treasure"

class Treasure:
    def __init__(self, image):
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()

        self.center = [random.randint(0, SCREEN_WIDTH),
                       random.randint(0, SCREEN_HEIGHT)]

        self.radius = max(self.width, self.height)

        self.draw_pos = self.center


def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########
    treasure_img = pygame.image.load("treasure.png")

    ##########
    # Set up game data
    ##########
    # place 40 treasures on the screen
    treasures = []
    for i in range(40):
        treasures.append(Treasure(treasure_img))

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
        screen.fill("white")
        for t in treasures:
            screen.blit(t.image, t.draw_pos)
            # draw a small dot at the center of the treasure to see the error
            pygame.draw.circle(screen, "red", t.center, 2)

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
