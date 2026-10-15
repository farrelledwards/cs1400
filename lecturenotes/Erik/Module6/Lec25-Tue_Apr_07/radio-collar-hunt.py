import pygame
import random


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CLOCK_TICK = 10
TITLE = "Perfectly Safe Radio Collar Hunt"

# Grid configuration
GRID_ROWS = 10
GRID_COLS = 10
CELL_SIZE = 50
MARGIN = 2
GRID_PIXEL_W = GRID_COLS * CELL_SIZE + (GRID_COLS - 1) * MARGIN
GRID_PIXEL_H = GRID_ROWS * CELL_SIZE + (GRID_ROWS - 1) * MARGIN
GRID_LEFT = (SCREEN_WIDTH - GRID_PIXEL_W) // 2
GRID_TOP = (SCREEN_HEIGHT - GRID_PIXEL_H) // 2

# Colors
BG_COLOR     = "#14161E"
GRID_LINE    = "#505A6E"
HIDDEN_COLOR = "#28324B"
PRIZE_COLOR  = "#FFD764"
TEXT_COLOR   = "#E6EBF5"
COLD_COLOR   = "#5A82DC"
HOT_COLOR    = "#DC5050"


def place_prize(rows, cols):
    """
    Return a pair of randomly choosen [row, column] coordinates that lie within the game grid
    """
    # TODO
    return [0, 0]


def manhattan_distance(r1, c1, r2, c2):
    """
    Given two (row,col) coordinate pairs, return their manhattan distance

    This function should be 1 line long
    """
    # TODO
    return 0


def build_distance_grid(rows, cols, prize_r, prize_c):
    """
    Given a grid size and a location for the prize, return a 2D list of integers that indicate the manhattan distance of each cell from the prize cell.

    The prize's manhattan distance will be zero.
    """
    # TODO
    return [ [], [], [], ]


def cell_from_pixel(px, py):
    local_x = px - GRID_LEFT
    local_y = py - GRID_TOP

    if local_x < 0 or local_y < 0:
        return -1, -1
    if local_x >= GRID_PIXEL_W or local_y >= GRID_PIXEL_H:
        return -1, -1

    block = CELL_SIZE + MARGIN
    c = local_x // block
    r = local_y // block

    if r < 0 or r >= GRID_ROWS or c < 0 or c >= GRID_COLS:
        return -1, -1

    if (local_x % block) >= CELL_SIZE or (local_y % block) >= CELL_SIZE:
        return -1, -1

    return int(r), int(c)


def pixel_from_cell(r, c):
    x = GRID_LEFT + c * (CELL_SIZE + MARGIN)
    y = GRID_TOP + r * (CELL_SIZE + MARGIN)
    return x, y


def heat_color(distance):
    if distance == 0:
        return pygame.Color(PRIZE_COLOR)
    if distance <= 3:
        return pygame.Color(HOT_COLOR)
    return pygame.Color(COLD_COLOR)


def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########
    font_cell  = pygame.font.SysFont("courier", 28)
    font_small = pygame.font.SysFont("courier", 24)
    font_title = pygame.font.SysFont("courier", 36)
    prize_sprite = pygame.image.load("radio-collar.png")

    # Prize setup
    prize_r, prize_c = place_prize(GRID_ROWS, GRID_COLS)
    distance_grid = build_distance_grid(GRID_ROWS, GRID_COLS, prize_r, prize_c)

    ##########
    # Set up game data
    ##########
    revealed = []
    # TODO: make 'revealed' into a 2D grid of size GRID_ROWS x GRID_COLS initialized with False values

    click_count = 0
    # TODO: fix the click counter so that it increments with each click, and is reset to 0 when the game restarts
    found_prize = False

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
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    running = False

                if event.key == pygame.K_SPACE:
                    # Reset everything
                    prize_r, prize_c = place_prize(GRID_ROWS, GRID_COLS)
                    distance_grid = build_distance_grid(GRID_ROWS, GRID_COLS, prize_r, prize_c)

                    revealed = []
                    # TODO: make 'revealed' into a 2D grid of size GRID_ROWS x GRID_COLS initialized with False values

                    found_prize = False
                    game_over = False

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mx, my = event.pos
                r, c = cell_from_pixel(mx, my)
                if r != -1 and not revealed[r][c]:
                    revealed[r][c] = True
                    if r == prize_r and c == prize_c:
                        found_prize = True
                        game_over = True

        screen.fill(pygame.Color(BG_COLOR))

        # Title
        ttxt = font_title.render("Perfectly Safe Radio Collar Hunt", True, pygame.Color(TEXT_COLOR))
        screen.blit(ttxt, ttxt.get_rect(center=(SCREEN_WIDTH // 2, 40)))

        # Clicks
        ctxt = font_small.render("Clicks: " + str(click_count),
                                 True, pygame.Color(TEXT_COLOR))
        screen.blit(ctxt, (20, SCREEN_HEIGHT - 40))

        # Instructions
        itxt = font_small.render("Click tiles to reveal. SPACE to reset, ESC to quit.",
                                 True, pygame.Color(TEXT_COLOR))
        screen.blit(itxt, itxt.get_rect(center=(SCREEN_WIDTH // 2,
                                                SCREEN_HEIGHT - 40)))

        # Draw grid
        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                x, y = pixel_from_cell(r, c)
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

                if revealed[r][c]:
                    d = distance_grid[r][c]
                    color = heat_color(d)
                    pygame.draw.rect(screen, color, rect)
                    pygame.draw.rect(screen, pygame.Color(GRID_LINE), rect, 1)

                    if r == prize_r and c == prize_c:
                        screen.blit(prize_sprite, prize_sprite.get_rect(center=rect.center))
                    else:
                        label = font_cell.render(str(d), True, pygame.Color(BG_COLOR))
                        screen.blit(label, label.get_rect(center=rect.center))
                else:
                    pygame.draw.rect(screen, pygame.Color(HIDDEN_COLOR), rect)
                    pygame.draw.rect(screen, pygame.Color(GRID_LINE), rect, 1)

        if game_over:
            if found_prize:
                msg = "You found the collar in " + str(click_count) + " clicks!"
            else:
                msg = "Game Over."

            otext = font_title.render(msg, True, pygame.Color(TEXT_COLOR))
            screen.blit(otext, otext.get_rect(center=(SCREEN_WIDTH // 2, GRID_TOP - 40)))

            prompt = font_small.render("Press SPACE to play again.", True,
                                       pygame.Color(TEXT_COLOR))
            screen.blit(prompt, prompt.get_rect(center=(SCREEN_WIDTH // 2,
                                                        GRID_TOP - 5)))

        #### Draw changes the screen ####
        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)


if __name__ == "__main__":
    main()
