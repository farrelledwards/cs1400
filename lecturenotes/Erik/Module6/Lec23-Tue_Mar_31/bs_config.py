# bs_config.py

##
## Don't change anything below this comment
##

# Screen constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CLOCK_TICK = 30
TITLE = "Battleship"

# Board constants
BOARD_SIZE = 10
CELL_SIZE = 40
CELL_MARGIN = 2
LABEL_WIDTH = 30
LABEL_HEIGHT = 30

# Board offsets (two boards side by side)
PLAYER_BOARD_X = 100
PLAYER_BOARD_Y = 100
OPPONENT_BOARD_X = 700
OPPONENT_BOARD_Y = 100

# Cell state values (for 2D list)
EMPTY = 0
SHIP = 1
HIT = 2
MISS = 3

# Colors (hex RGB strings)
COLOR_BG = "#141E32"
COLOR_EMPTY = "#325096"
COLOR_SHIP = "#646464"
COLOR_HIT = "#C83232"
COLOR_MISS = "#C8C8C8"
COLOR_GRID_LINE = "#969696"
COLOR_TEXT = "#FFFFFF"
COLOR_LABEL = "#C8C8FF"
