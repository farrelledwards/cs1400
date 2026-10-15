# player-constraints.py
import pygame


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
CLOCK_TICK = 60
TITLE = "Arrow-Key Player Constraints (Buggy)"
PLAYER_SPEED = 16
PLAYER_WIDTH = 64
PLAYER_COLOR = "yellow2"


class Player:
    """Represents the player on the screen"""
    pass


def move_player(player, move):
    cx, cy = player.center_pos
    cx += move[0]
    cy += move[1]
    if cx < 0:
        cx = 0
    elif cx > SCREEN_WIDTH:
        cx = SCREEN_WIDTH
    cy = max(0, min(SCREEN_HEIGHT, cy))
    player.center_pos = [cx, cy]


def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########

    ##########
    # Set up game data
    ##########
    p = Player()
    p.center_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_WIDTH]
    p.radius = PLAYER_WIDTH
    p.color = "forestgreen"

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
        pressed = pygame.key.get_pressed()
        dx = (pressed[pygame.K_RIGHT] - pressed[pygame.K_LEFT]) * 3
        dy = (pressed[pygame.K_DOWN] - pressed[pygame.K_UP]) * 3
        move_player(p, [dx, dy])

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
        pygame.draw.circle(screen, p.color, [p.center_pos[0], p.center_pos[1]], p.radius)

        #### Display while Game is being played ####
        if not game_over:
            pass
        #### Display while Game is Over ####
        else:
            pass

        #### Draw changes to the screen ####
        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)


main()
