# clicky-grid.py

import pygame

import constants
from grid import Grid, index_to_rc, pixel_from_cell


def cell_from_pixel(px, py, cell_size, cols, rows, margin):
    """Convert pixel coordinates to grid cell (row, col). Returns (-1, -1) if invalid."""
    if px < 0 or py < 0:
        return -1, -1
    block = cell_size + margin
    c = px // block
    r = py // block
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return -1, -1
    # reject clicks on the margin strip
    if (px % block) >= cell_size or (py % block) >= cell_size:
        return -1, -1
    return int(r), int(c)


def draw_keyboard_mode_message(screen, font):
    """Display a message on the screen indicating keyboard mode is active."""
    line1 = "Awaiting keyboard input"
    line2 = "in terminal..."
    text1 = font.render(line1, True, constants.HIGHLIGHT_COLOR)
    text2 = font.render(line2, True, constants.HIGHLIGHT_COLOR)
    rect1 = text1.get_rect()
    rect2 = text2.get_rect()
    center_x = constants.SCREEN_WIDTH // 2
    center_y = constants.SCREEN_HEIGHT // 2
    rect1.center = (center_x, center_y - rect1.height // 2 - 5)
    rect2.center = (center_x, center_y + rect2.height // 2 + 5)
    screen.blit(text1, rect1)
    screen.blit(text2, rect2)


def print_mouse_mode_instructions():
    """Print instructions for mouse mode to the terminal."""
    print("=== Mouse Mode ===")
    print("Window controls:")
    print("  ESC or Q  → quit")
    print("Interaction:")
    print("  - Click a cell to toggle it on/off")
    print("  - Prints mouse pixel coords and grid cell (r,c)")
    print("  - Screen updates immediately")
    print("  - Press ENTER to switch to keyboard mode")
    print("--------------------------------")


def print_keyboard_mode_instructions(total_cells):
    """Print instructions for keyboard mode to the terminal."""
    print("=== Keyboard Mode ===")
    print("  - Type a cell NUMBER (0..{}) and press ENTER".format(total_cells - 1))
    print("  - Toggles that cell and prints its upper-left pixel coords")
    print("  - Invalid or out-of-range numbers are ignored")
    print("  - Press ENTER with no input to return to mouse mode")
    print("--------------------------------")


def prompt_keyboard_and_toggle(grid, screen, font):
    """Loop to get keyboard input and toggle cells. Returns when user enters blank line."""
    while True:
        raw = input("Enter a cell number (0..{}), or blank to return to mouse mode: ".format(grid.total - 1))
        if raw.strip() == "":
            print("[keyboard] returning to mouse mode")
            print_mouse_mode_instructions()
            return
        stripped = raw.strip()
        if not stripped.isdigit():
            print("[keyboard] invalid integer:", raw)
            continue
        n = int(stripped)
        if grid.toggle_index(n):
            r, c = index_to_rc(n, grid.cols)
            px, py = pixel_from_cell(r, c, constants.CELL_SIZE, constants.MARGIN)
            print(f"[keyboard] toggled cell {n} at (r={r}, c={c}); upper-left pixel=({px},{py})")
            grid.draw(screen, font)
            draw_keyboard_mode_message(screen, font)
            pygame.display.flip()
        else:
            print(f"[keyboard] out of range: {raw}")


def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption(constants.TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########
    font = pygame.font.SysFont("consolas", 32)

    ##########
    # Set up game data
    ##########
    grid = Grid(constants.GRID_ROWS, constants.GRID_COLS)
    mouse_mode = True
    print_mouse_mode_instructions()

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
                    grid = Grid(constants.GRID_ROWS, constants.GRID_COLS)
                    game_over = False
                if event.key == pygame.K_RETURN and not game_over and mouse_mode:
                    mouse_mode = False
                    print_keyboard_mode_instructions(grid.total)
                    grid.draw(screen, font)
                    draw_keyboard_mode_message(screen, font)
                    pygame.display.flip()
                    prompt_keyboard_and_toggle(grid, screen, font)
                    mouse_mode = True

            # Mouse click toggles cell in mouse mode
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and mouse_mode:
                mx, my = event.pos
                r, c = cell_from_pixel(mx, my, constants.CELL_SIZE, constants.GRID_COLS, constants.GRID_ROWS, constants.MARGIN)
                print(f"[click] mouse=({mx},{my}) -> cell=({r},{c})")
                if r != -1 and c != -1:
                    grid.toggle_rc(r, c)
                    px, py = pixel_from_cell(r, c, constants.CELL_SIZE, constants.MARGIN)
                    print(f"[click] toggled cell at (r={r}, c={c}); upper-left pixel=({px},{py})")

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
        grid.draw(screen, font)

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
        clock.tick(constants.CLOCK_TICK)

if __name__ == "__main__":
    main()
