# grid.py

import pygame

import constants


# ===============================
# Helpers students focus on
# ===============================
def rc_to_index(r, c, cols):
    """Convert row and column to a 1D index."""
    # TODO: Implement this function
    return 0


def index_to_rc(index, cols):
    """Convert a 1D index to row and column."""
    # TODO: Implement this function
    return [0, 0]


def pixel_from_cell(r, c, cell_size, margin):
    """Convert grid cell (row, col) to pixel coordinates (x, y) of upper-left corner."""
    # TODO: Implement this function
    return [0, 0]


# ===============================
# 1D Grid model
# ===============================
class Grid:
    def __init__(self, rows, cols):
        self.rows = int(rows)
        self.cols = int(cols)
        self.total = self.rows * self.cols
        self.cells = []
        for i in range(self.total):
            self.cells.append(0)  # 0=off, 1=on

    def in_bounds(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def get(self, r, c):
        if not self.in_bounds(r, c):
            return 0
        return self.cells[rc_to_index(r, c, self.cols)]

    def toggle_rc(self, r, c):
        if not self.in_bounds(r, c):
            return False
        idx = rc_to_index(r, c, self.cols)
        self.cells[idx] = 0 if self.cells[idx] == 1 else 1
        return True

    def toggle_index(self, index):
        if index < 0 or index >= self.total:
            return False
        r, c = index_to_rc(index, self.cols)
        return self.toggle_rc(r, c)

    def draw(self, screen, font):
        screen.fill(constants.BG)
        for r in range(self.rows):
            for c in range(self.cols):
                px, py = pixel_from_cell(r, c, constants.CELL_SIZE, constants.MARGIN)
                rect = pygame.Rect(px, py, constants.CELL_SIZE, constants.CELL_SIZE)
                color = constants.ON_CELL if self.get(r, c) == 1 else constants.OFF_CELL
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, constants.GRID_LINE, rect, 1)

                idx = rc_to_index(r, c, self.cols)
                label = font.render(str(idx), True, constants.TEXT_COLOR)
                label_rect = label.get_rect()
                label_rect.center = (px + constants.CELL_SIZE // 2, py + constants.CELL_SIZE // 2)
                screen.blit(label, label_rect)
