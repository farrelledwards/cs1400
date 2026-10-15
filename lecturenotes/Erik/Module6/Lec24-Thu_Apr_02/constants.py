# ---- Grid config ----
MARGIN = 4  # spacing between cells
CELL_SIZE = 64
GRID_ROWS = 6
GRID_COLS = 10
SCREEN_WIDTH = GRID_COLS * CELL_SIZE + (GRID_COLS - 1) * MARGIN
SCREEN_HEIGHT = GRID_ROWS * CELL_SIZE + (GRID_ROWS - 1) * MARGIN

CLOCK_TICK = 30
TITLE = "Pixel to Grid Translator"

# ---- Colors (hex RGB strings) ----
BG         = "#18181C"
GRID_LINE  = "#3C3C46"
OFF_CELL   = "#202840"
ON_CELL    = "#DCF0FF"
TEXT_COLOR = "#14181C"
HIGHLIGHT_COLOR = "#FF00FF"
