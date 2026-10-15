# hotpoint.py

import math
import pygame

from cursor import Cursor


TITLE = "Cursor Hotpoint Calibrator"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CLOCK_TICK = 30                # Framerate of the game
CLICK_FRAMES = CLOCK_TICK * 2  # Number of frames a click remains on screen
CURSOR_IMAGE = "cursor3.png"   # TODO: try each of "cursor0.png"
                               #                   "cursor1.png"
                               #                   "cursor2.png"
                               #                   "cursor3.png"
                               #                   "cursor4.png"
                               #                   "cursor5.png"
                               #                   "cursor6.png"


def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########
    # TODO: create an instance of the Cursor class
    # TODO: hide your OS cursor

    ##########
    # Set up game data
    ##########
    center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    game_over = False
    clicks = []  # list of on-screen click images

    ##########
    # Game Loop
    ##########
    running = True
    while running:

        # Reset the boolean that tracks whether the mouse was clicked on this frame
        mouse_clicked = False
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
                    # Not used in this lab, kept to preserve template behavior
                    game_over = False

            # TODO: Presently a click is registered for ANY mouse button
            #       Change this so that only left mouse button clicks are registered
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True
                # add a new Click object to the list of on-screen clicks
                clicks.append(Click(event.pos))


        ##########
        # Update state of components/data
        ##########
        #### Always Update ####
        mouse_pos = pygame.mouse.get_pos()
        cursor.update_pos(mouse_pos)

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

        draw_crosshairs(screen)

        # Draw all clicks with fade effect, removing those that age out
        new_clicks = []
        for click in clicks:
            click.draw(screen)  # this method also decrements the Time To Live counter
            if click.ttl != 0:
                new_clicks.append(click)
        clicks = new_clicks

        # Draw the custom cursor last so it sits above the other elements
        # TODO: what happens if you move this line of code above draw_crosshairs()?
        cursor.draw(screen)

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


def draw_crosshairs(surface, color="black", size=3):
    """Draw calibration target at exact center of screen"""
    pygame.draw.line(surface, color, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
    pygame.draw.line(surface, color, (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2))


class Click:
    """X marks the spot where the mouse button was clicked"""
    COLORS = []
    for i in range(CLICK_FRAMES, 0, -1):
        fade = i / CLICK_FRAMES
        COLORS.append((255, int(255 * fade), int(255 * fade)))

    def __init__(self, center, ttl=CLICK_FRAMES, size=15, thickness=10):
        self.center = center
        self.ttl = ttl  # ttl = Time To Live
        self.size = size
        self.thickness = thickness

    def draw(self, surface):
        """
        Put an X on the screen centered on this object's center attribute,
        and decrement the TTL counter by 1
        """
        if self.ttl > 0:
            self.ttl -= 1
            cx, cy = self.center
            pygame.draw.line(surface, Click.COLORS[self.ttl], (cx - self.size, cy - self.size), (cx + self.size, cy + self.size), self.thickness)
            pygame.draw.line(surface, Click.COLORS[self.ttl], (cx - self.size, cy + self.size), (cx + self.size, cy - self.size), self.thickness)


main()
