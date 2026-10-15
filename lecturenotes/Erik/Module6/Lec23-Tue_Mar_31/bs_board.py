# bs_board.py

import random

import bs_config
import bs_types


def create_board():
    """
    Create an empty 2D list representing a square game board with sides of length with bs_config.BOARD_SIZE
    """
    # TODO: implement this function
    board = []
    return board


def get_cell(board, row, col):
    """
    Read a value from a 2D list board at the given row and column.
    Check that the values of 'row' and 'col' are valid before use.
    If either is invalid, return None.
    Otherwise, return the value of the cell at that position.
    """
    # TODO: implement this function
    return bs_config.EMPTY


def set_cell(board, row, col, value):
    """
    Write a value to a 2D list board at the given row and column.
    Check that the values of 'row' and 'col' are valid before use.
    If either is invalid, return without changing anything.
    Otherwise, update the value of the cell at that position.

    """
    # TODO: implement this function
    pass

##
## Don't change anything below this comment
##

def is_valid_placement(board, row, col, length, horizontal):
    """Check if a ship can be placed at the given position."""
    # Check bounds
    if horizontal:
        if col + length > bs_config.BOARD_SIZE:
            return False
        for c in range(col, col + length):
            if get_cell(board, row, c) != bs_config.EMPTY:
                return False
    else:
        if row + length > bs_config.BOARD_SIZE:
            return False
        for r in range(row, row + length):
            if get_cell(board, r, col) != bs_config.EMPTY:
                return False
    return True


def place_ship(board, row, col, length, horizontal):
    """Place a ship on the board by setting cells in the 2D list to SHIP."""
    if not is_valid_placement(board, row, col, length, horizontal):
        return False

    if horizontal:
        for c in range(col, col + length):
            set_cell(board, row, c, bs_config.SHIP)
    else:
        for r in range(row, row + length):
            set_cell(board, r, col, bs_config.SHIP)
    return True


def place_ships_randomly(board):
    """Place all ships randomly on the board."""
    for ship_name, ship_length in bs_types.SHIPS:
        placed = False
        attempts = 0
        while not placed and attempts < 100:
            row = random.randint(0, bs_config.BOARD_SIZE - 1)
            col = random.randint(0, bs_config.BOARD_SIZE - 1)
            horizontal = random.choice([True, False])
            if place_ship(board, row, col, ship_length, horizontal):
                placed = True
            attempts += 1


def make_guess(board, row, col):
    """Process a guess at the given position. Returns 'hit', 'miss', or 'invalid'."""
    cell_value = get_cell(board, row, col)
    if cell_value is None:
        return 'invalid'
    elif cell_value == bs_config.SHIP:
        set_cell(board, row, col, bs_config.HIT)
        return 'hit'
    elif cell_value == bs_config.EMPTY:
        set_cell(board, row, col, bs_config.MISS)
        return 'miss'
    else:
        return 'invalid'  # Already guessed


def count_ships(board):
    """Count remaining ship cells in the 2D list."""
    count = 0
    for row in range(bs_config.BOARD_SIZE):
        for col in range(bs_config.BOARD_SIZE):
            if get_cell(board, row, col) == bs_config.SHIP:
                count += 1
    return count


def all_ships_sunk(board):
    """Check if all ships are sunk by iterating through the 2D list."""
    return count_ships(board) == 0
