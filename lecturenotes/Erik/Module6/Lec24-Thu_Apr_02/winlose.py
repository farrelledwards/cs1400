# winlose.py
import pygame


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CLOCK_TICK = 30
TITLE = "The WIN/LOSE Game"

# ===== States =====
# TODO: read the code and identify the states of the game
# TODO: define the constants, giving each a unique value


def center(screen, surface, y):
    """Center a surface horizontally on the screen."""
    x = (SCREEN_WIDTH - surface.get_width()) // 2
    screen.blit(surface, (x, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Fonts 
    ##########
    font_big = pygame.font.SysFont("mono", 96)
    font_med = pygame.font.SysFont("mono", 48)
    font_sm  = pygame.font.SysFont("mono", 28)

    ##########
    # Game data
    ##########
    state = TITLE_STATE
    game_over = False  # "terminal state" flag (true for WIN or GAME OVER)

    countdown_frames = 0
    countdown_total = 3 # TODO: set to 3 seconds at CLOCK_TICK fps

    ##########
    # Game Loop
    ##########
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_SPACE:
                    # TODO: start the countdown from the Title screen
                    # TODO: or, reset the game from one of the "terminal" screens
                    pass

                # PLAY-state controls: W to win, L to lose
                if state == PLAY_STATE:
                    # TODO: win the game if W is pressed
                    # TODO: lose the game if L is pressed
                    # Hint: Pygame doesn't distinguish between upper- and lower-case letters
                    # Hint: https://www.pygame.org/docs/ref/key.html
                    pass

        clock.tick(CLOCK_TICK)

        if not game_over:
            if state == COUNTDOWN_STATE:
                # TODO: while in COUNTDOWN_STATE, increment countdown_frames 
                # TODO: switch to PLAY_STATE after enough countdown_frames have ticked by
                pass
        else:
            pass

        screen.fill('#121418')

        if not game_over:
            if state == TITLE_STATE:
                t1 = font_big.render("WIN/LOSE", True, '#E6F0FF')
                t2 = font_med.render("Press SPACE to start", True, '#C8D2DC')
                center(screen, t1, y=SCREEN_HEIGHT // 2 - 80)
                center(screen, t2, y=SCREEN_HEIGHT // 2 + 10)

            elif state == COUNTDOWN_STATE:
                remaining = countdown_total - countdown_frames
                if remaining < 0:
                    remaining = 0
                n = 1 + (remaining // CLOCK_TICK)
                txt = font_big.render(str(n), True, '#FFE678')
                center(screen, txt, y=SCREEN_HEIGHT // 2 - 40)
                hint = font_sm.render("Get ready...", True, '#D2DCE6')
                center(screen, hint, y=SCREEN_HEIGHT // 2 + 60)

            elif state == PLAY_STATE:
                msg1 = font_med.render("Press W to win.", True, '#C8F0C8')
                msg2 = font_med.render("Press L to lose.", True, '#F0C8C8')
                center(screen, msg1, y=SCREEN_HEIGHT // 2 - 30)
                center(screen, msg2, y=SCREEN_HEIGHT // 2 + 30)

        else:
            if state == WIN_STATE:
                win1 = font_big.render("YOU WIN!", True, '#B4FFB4')
                win2 = font_med.render("Press SPACE to return to Title", True, '#DCE6F0')
                center(screen, win1, y=SCREEN_HEIGHT // 2 - 60)
                center(screen, win2, y=SCREEN_HEIGHT // 2 + 20)
            elif state == GAME_OVER_STATE:
                over1 = font_big.render("GAME OVER", True, '#FF7878')
                over2 = font_med.render("Press SPACE to return to Title", True, '#DCE6F0')
                center(screen, over1, y=SCREEN_HEIGHT // 2 - 60)
                center(screen, over2, y=SCREEN_HEIGHT // 2 + 20)

        pygame.display.flip()


main()
