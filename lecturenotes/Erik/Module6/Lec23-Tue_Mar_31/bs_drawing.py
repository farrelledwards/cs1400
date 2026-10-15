# bs_drawing.py

##
## Don't change anything below this comment
##

import pygame

import bs_config
import bs_board


def pixel_from_cell(row, col, offset_x, offset_y):
    """Convert grid cell (row, col) to pixel coordinates."""
    px = offset_x + bs_config.LABEL_WIDTH + col * (bs_config.CELL_SIZE + bs_config.CELL_MARGIN)
    py = offset_y + bs_config.LABEL_HEIGHT + row * (bs_config.CELL_SIZE + bs_config.CELL_MARGIN)
    return px, py


def cell_from_pixel(px, py, offset_x, offset_y):
    """Convert pixel coordinates to grid cell (row, col). Returns (-1, -1) if invalid."""
    # Adjust for label area
    px -= offset_x + bs_config.LABEL_WIDTH
    py -= offset_y + bs_config.LABEL_HEIGHT

    if px < 0 or py < 0:
        return -1, -1

    block = bs_config.CELL_SIZE + bs_config.CELL_MARGIN
    col = px // block
    row = py // block

    # Check if click is within cell bounds (not in margin)
    if (px % block) >= bs_config.CELL_SIZE or (py % block) >= bs_config.CELL_SIZE:
        return -1, -1

    if row < 0 or row >= bs_config.BOARD_SIZE or col < 0 or col >= bs_config.BOARD_SIZE:
        return -1, -1

    return row, col


def draw_cell(screen, x, y, cell_value, show_ships):
    """Draw a single cell based on its value in the 2D list."""
    rect = pygame.Rect(x, y, bs_config.CELL_SIZE, bs_config.CELL_SIZE)

    # Determine color based on cell value
    if cell_value == bs_config.HIT:
        color = bs_config.COLOR_HIT
    elif cell_value == bs_config.MISS:
        color = bs_config.COLOR_MISS
    elif cell_value == bs_config.SHIP and show_ships:
        color = bs_config.COLOR_SHIP
    else:
        color = bs_config.COLOR_EMPTY

    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, bs_config.COLOR_GRID_LINE, rect, 1)


def draw_board(screen, board_state, offset_x, offset_y, show_ships, font):
    """Draw a game board by iterating through the 2D list."""
    # Draw row labels (A-J)
    for row in range(bs_config.BOARD_SIZE):
        label = chr(ord('A') + row)
        text = font.render(label, True, bs_config.COLOR_LABEL)
        text_rect = text.get_rect()
        text_rect.center = (offset_x + bs_config.LABEL_WIDTH // 2,
                           offset_y + bs_config.LABEL_HEIGHT + row * (bs_config.CELL_SIZE + bs_config.CELL_MARGIN) + bs_config.CELL_SIZE // 2)
        screen.blit(text, text_rect)

    # Draw column labels (1-10)
    for col in range(bs_config.BOARD_SIZE):
        label = str(col + 1)
        text = font.render(label, True, bs_config.COLOR_LABEL)
        text_rect = text.get_rect()
        text_rect.center = (offset_x + bs_config.LABEL_WIDTH + col * (bs_config.CELL_SIZE + bs_config.CELL_MARGIN) + bs_config.CELL_SIZE // 2,
                           offset_y + bs_config.LABEL_HEIGHT // 2)
        screen.blit(text, text_rect)

    # Draw cells by iterating through the 2D list
    for row in range(bs_config.BOARD_SIZE):
        for col in range(bs_config.BOARD_SIZE):
            px, py = pixel_from_cell(row, col, offset_x, offset_y)
            cell_value = bs_board.get_cell(board_state, row, col)
            draw_cell(screen, px, py, cell_value, show_ships)


def draw_status_text(screen, font, text, y_pos):
    """Draw status text on the screen."""
    text_surface = font.render(text, True, bs_config.COLOR_TEXT)
    text_rect = text_surface.get_rect()
    text_rect.center = (bs_config.SCREEN_WIDTH // 2, y_pos)
    screen.blit(text_surface, text_rect)
