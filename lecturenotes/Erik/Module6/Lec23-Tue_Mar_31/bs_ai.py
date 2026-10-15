# bs_ai.py

import random

import bs_config


def initialize_available_positions():
    """
    Create a shuffled list of all possible positions on the board.
    """
    positions = []
    for row in range(bs_config.BOARD_SIZE):
        for col in range(bs_config.BOARD_SIZE):
            positions.append([row, col])
    # TODO: Shuffle the list of positions so the AI's play is unpredictable
    #       Hint: read the documentation for the random module
    return positions

##
## Don't change anything below this comment
##

def ai_make_guess(available_positions):
    """
    Pick the first position from the available positions list.
    """
    if available_positions:
        return available_positions.pop(0)
    else:
        return [None, None]
