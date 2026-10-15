# buggy-bouncing-balls.py
import pygame


SCREEN_WIDTH = 1280  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 720
TITLE = "Bouncy Bugs"
CLOCK_TICK = 30
BALL_SIZE = 64
BACKGROUND_COLOR = "black"


class Ball:
    def __init__(self, image_file, x, y, dx, dy):
        self.image = pygame.image.load(image_file)
        self.position = [x, y]
        self.speed = [dx, dy]

    def move(self):
        self.position[0] = self.position[0] + self.speed[0]
        self.position[1] = self.position[1] + self.speed[1]

        # TODO: is this movement logic correct?
        if self.position[0] > SCREEN_WIDTH // 2 - 80 and self.position[0] < SCREEN_WIDTH // 2 + 80:
            self.speed[0] = 0

    def bounce(self):
        # TODO: is the bounce logic correct?
        if self.position[0] < 0:
            self.speed[0] = self.speed[0] * -1
        elif self.position[0] > SCREEN_WIDTH:
            self.speed[0] = self.speed[0] * -1

        if self.position[1] < 0:
            self.speed[1] = self.speed[1] * -1
        elif self.position[1] > SCREEN_HEIGHT:
            self.speed[1] = self.speed[1] * -1

    def draw(self, screen):
        screen.blit(self.image, self.position)


def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########

    balls = []
    balls.append(Ball("EnBallBlue.png", 100, 100, 6, 4))
    balls.append(Ball("EnBallGreen.png", 500, 300, -5, 3))
    balls.append(Ball("EnBallPurp.png", 900, 200, 7, -4))

    ##########
    # Set up game data
    ##########

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
            if event.type == pygame.KEYDOWN:
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

        for ball in balls:
            ball.move()
            ball.bounce()

        #### Display while Game is being played ####
        if not game_over:
            pass
        #### Display while Game is Over ####
        else:
            pass

        #### Draw changes the screen ####
        screen.fill(BACKGROUND_COLOR)
        for ball in balls:
            ball.draw(screen)
        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)


main()
