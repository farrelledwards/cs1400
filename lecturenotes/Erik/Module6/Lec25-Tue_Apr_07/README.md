CS1400 - Tuesday, April 07 - Lecture 25 - Module 6

# Topics:
* [🟥Assn 6 - Crashtropolis](#assn-6---crashtropolis)
* [Code Lab Challenge 0 - The Perfectly Safe Radio Collar Hunt](#code-lab-challenge-0---the-perfectly-safe-radio-collar-hunt)
* [Code Lab Challenge 1 - Sprite Transformer](#code-lab-challenge-1---sprite-transformer)


------------------------------------------------------------
# Announcements

## *TONIGHT* FSLC - Your Custom Linux Desktop

*   **When**    6:30 PM Tuesday, April 7th
*   **Where**   WIDT 007
*   **Website** https://linux.usu.edu
*   **Discord** https://discord.gg/PvgG6N2hsU

"You can customize Linux", they say. "You can do whatever you want with Linux", they say. Tonight we'll show you how! We'll start with the classic Gnome Desktop using GUI's. Then we'll take a turn for the dark side and switch it out for Niri, a scrolling (tiling) window manager and showcase your first steps in configuration with dotfiles.


## [Take the IDEA Survey](https://usu.campuslabs.com/eval-home/)

*   It's worth 185 points of extra credit
*   The survey closes 04/21/2026 at 11:59 PM


# Action Items

## Upcoming Schedule

-   Thu, Apr 09 **Canceled** See you at BSidesSLC!
    -   Erik's office hours are also cancelled this week
-   Sun, Apr 12 *Assn 6: Crashtropolis due*
-   Tue, Apr 14 Code lab for Assn 7
-   Thu, Apr 16 Final Code Lab
-   Sun, Apr 19 *Assn 7: Deckinator due*
-   Tue, Apr 21 Review for final exam
-   Wed, Apr 22 *Finals week begins*
-   Tue, Apr 28 *End of finals week*


# [🟥Assn 6 - Crashtropolis](https://usu.instructure.com/courses/794745/assignments/5122792)


| Task/Day           | **Tuesday**        | **Wednesday** | **Thursday**       | **Friday** | **Saturday** | **Sunday**                           | **Monday**                         | **Tuesday**
| ------------------ | -------------------| ------------- | ------------------ | ---------- | ------------ | ------------------------------------ | ---------------------------------- | -----------
| **Classroom Time** | Classroom Lab Time |               | Code Lab Cancelled | BSidesSLC  |              |                                      |                                    | 7.1: Search Algorithms
| **Items Due**      |                    |               | for BSidesSLC      |            |              | Assignment 6<br/>Reflection Survey 6 | Code Reviews for <br/>Assn 6 begin |



# Code Lab Challenge 0 - The Perfectly Safe Radio Collar Hunt

Do you remember the day when the bomb squad was called up to campus?  Good times...

On a completely different topic, the Department of Wildland Resources has reached out to the School of Computing for help developing
a completely safe and non-threatening wildlife tracking collar locating simulator that their undergraduates can use to learn how to 
track these collars down without causing concern with some of our... excitable colleagues.

I've gotten a good start on one version of this program.  Can you help me finish it?  One part of this program asks us to compute the Manhattan Distance between two cells in a 2D grid.
The formula for that is: $`\lvert x_1 - x_2 \rvert + \lvert y_1 - y_2 \rvert`$


<details>
<summary><h3>radio-collar-hunt.py</h3></summary>

```python
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
```

</details>

[Download radio-collar-hunt.py](./radio-collar-hunt.py)

![](./radio-collar.png)

[Download radio-collar.png](./radio-collar.png)


### Phase 0 - Identify The Missing Features

Answer each of these questions in today's Wooclap:

*   Which TODO items do you think will be the easiest to address?
*   Which TODO items depend on other TODO items being completed first? (For example, can you test `build_distance_grid` without first implementing `manhattan_distance`?)
*   What would happen if you ran the program right now with all the TODOs still in place? What errors or unexpected behaviors would you see?
*   For the `place_prize` function what should the range of valid row and column values be?
*   What data structure should `revealed` be to represent a 2D grid? 
*   Where in the code should `click_count` be incremented?
    *   What should happen to `click_count` when the game resets (i.e. when Space is pressed)?
    *   Where in the code should you set it back to `0`?


### Phase 1 - Fix It

Enact your proposed changes in the program.


### Phase 2 - Test It

Run the program several times to make sure that

*   Each cell is populated with its correct Manhattan Distance
*   Hot & cold colors are correctly applied
*   The game ends when the collar is found
*   The game is correctly reset when Space is pressed
*   The game is exited when Escape or `q` is pressed
*   The click count is incremented and reset correctly


### Phase 3 - Reflect On It

Answer these debrief questions in comments in today's Wooclap:

*   How did you implement `build_distance_grid()`?
*   How did you populate the `revealed` list?
*   `revealed` is initialized in two different places (at game start and when resetting)
    *   What does this duplication suggest about the code structure?
    *   How might you avoid this duplication?
*   What was the most challenging TODO item for you to complete, and why? 
    *   What was your strategy to work through it?
*   How did you test your implementation?
*   Looking at the `manhattan_distance` function: why do you think the comment specifies it should be "1 line long"?
    *   What does this constraint teach us about writing concise, readable code?
*   If you were to explain Manhattan Distance to someone who has never heard of it, how would you describe it using everyday language?



### Phase 4 - Stretch Challenges

* There is code to display the message `"Game Over."`  Is it possible for this message to ever be displayed?
* The program maintains two variables `found_prize` and `game_over`
    *   Are both of these really necessary?
    *   See if you can rewrite the program to only need one of these
* There is one color for hot and one color for cold, but there are many degrees between the coldest possible square and the prize
    *   Work out what the maximum Manhattan Distance could possibly be on a 10x10 grid
    *   Add more in-between colors for each distance 
* Some code is copy & pasted into the program twice
    *   Identify duplicated code and create a `Game` class that embodies the game grid's logic and data
    *   You may need to migrate other functions and data into this new class to get everything to work 


# Code Lab Challenge 1 - Sprite Transformer

In this code challenge you will practice using Pygame's surface transformation functions to create altered copies of sprites.

<details>
<summary><h3>sprite-transformer.py</h3></summary>

```python
import pygame
import sys


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CLOCK_TICK = 60
TITLE = "Sprite Editor"

STAGE_BG = "#000000"
UI_BG = "#111111"
TEXT_COLOR = "#DDDDDD"

PALETTE_HEIGHT = 120
PALETTE_MARGIN = 10

# Number of sprites in the palette (1–5)
NUM_SPRITES = 5

# Rotation and scale controls
ROTATION_STEP_DEGREES = 15
SCALE_STEP = 0.15  # 15%
MIN_SCALE = 0.2
MAX_SCALE = 3.0


#########################
# Transforms to implement
#########################
def apply_rotation(sprite, degrees):
    """Call the pygame transform function to rotate the sprite by the desired amount, returning a copy of the sprite"""
    # TODO
    return sprite


def apply_scale(sprite, scale_factor):
    """Call the pygame transform function to scale the sprite by the desired amount, returning a copy of the sprite"""
    # TODO
    return sprite


def apply_grayscale(sprite):
    """Call the pygame transform function that removes color from the sprite, returning a copy of the sprite"""
    # TODO
    return sprite


def apply_horizontal_flip(sprite):
    """Call the pygame transform function flips the sprite horizontally, returning a copy of the sprite"""
    # TODO
    return sprite


def apply_vertical_flip(sprite):
    """Call the pygame transform function flips the sprite vertically, returning a copy of the sprite"""
    # TODO
    return sprite


def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########
    font = pygame.font.SysFont("courier", 24)
    original_sprites = []
    original_sprites.append(pygame.image.load("cherry.png").convert_alpha())
    original_sprites.append(pygame.image.load("flower.png").convert_alpha())
    original_sprites.append(pygame.image.load("ghost.png").convert_alpha())
    original_sprites.append(pygame.image.load("ship.png").convert_alpha())
    original_sprites.append(pygame.image.load("star-gem.png").convert_alpha())

    ##########
    # Set up game data
    ##########
    selected_index = 0
    current_sprite = original_sprites[selected_index]

    undo_stack = []
    redo_stack = []

    ##########
    # Game Loop
    ##########
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

                # Sprite selection (1–5)
                if pygame.K_1 <= event.key <= pygame.K_5:
                    selected_index = event.key - pygame.K_1
                    current_sprite = original_sprites[selected_index]
                    # STRETCH: clear out the undo/redo stacks when a new sprite is selected

                # Undo / Redo
                if event.key == pygame.K_u:
                    # STRETCH: Move the top image of the undo stack onto the top of the redo stack
                    pass

                if event.key == pygame.K_r:
                    # STRETCH: Move the top image of the redo stack back onto the top of the undo stack
                    pass

                # Rotation
                if event.key == pygame.K_LEFT:
                    # TODO: Rotate the sprite clockwise
                    # STRETCH: append the current image onto the top of the undo stack
                    current_sprite = apply_rotation(current_sprite, -ROTATION_STEP_DEGREES)

                if event.key == pygame.K_RIGHT:
                    # TODO: Rotate the sprite counter-clockwise
                    # STRETCH: append the current image onto the top of the undo stack
                    current_sprite = apply_rotation(current_sprite, ROTATION_STEP_DEGREES)

                # Flip
                if event.key == pygame.K_v:
                    # TODO: flip the sprite vertically
                    # STRETCH: append the current image onto the top of the undo stack
                    current_sprite = apply_vertical_flip(current_sprite)

                if event.key == pygame.K_h:
                    # TODO: flip the sprite horizontally
                    # STRETCH: append the current image onto the top of the undo stack
                    current_sprite = apply_horizontal_flip(current_sprite)

                # Scaling
                if event.key == pygame.K_UP:
                    # TODO: Enlarge the sprite
                    # STRETCH: append the current image onto the top of the undo stack
                    current_sprite = apply_scale(current_sprite, 1 + SCALE_STEP)

                if event.key == pygame.K_DOWN:
                    # TODO: Shrink the sprite
                    # STRETCH: append the current image onto the top of the undo stack
                    current_sprite = apply_scale(current_sprite, 1 - SCALE_STEP)

                # Grayscale (remove color)
                if event.key == pygame.K_g:
                    # TODO: render the sprite in grayscale
                    # STRETCH: append the current image onto the top of the undo stack
                    current_sprite = apply_grayscale(current_sprite)

        ##########
        # Update Display
        ##########
        #### Always Display ####
        screen.fill(pygame.Color("#000000"))

        draw_stage(screen, current_sprite)
        draw_palette(screen, font, original_sprites, selected_index)

        #### Draw changes the screen ####
        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)


###########################
# Leave this code unchanged
###########################
def draw_palette(screen, font, sprites, selected_index):
    pygame.draw.rect(
        screen,
        pygame.Color(UI_BG),
        pygame.Rect(0, SCREEN_HEIGHT - PALETTE_HEIGHT, SCREEN_WIDTH, PALETTE_HEIGHT),
    )

    available_width = SCREEN_WIDTH - 2 * PALETTE_MARGIN
    slot_width = available_width // NUM_SPRITES
    center_y = SCREEN_HEIGHT - PALETTE_HEIGHT // 2

    for i in range(NUM_SPRITES):
        x_center = PALETTE_MARGIN + slot_width * i + slot_width // 2

        thumb_height = PALETTE_HEIGHT - 40
        thumb = pygame.transform.smoothscale(sprites[i], (thumb_height, thumb_height))
        rect = thumb.get_rect(center=(x_center, center_y))
        screen.blit(thumb, rect)

        if i == selected_index:
            pygame.draw.rect(screen, pygame.Color("#FFFFFF"), rect.inflate(8, 8), 2)

        label = font.render(str(i + 1), True, pygame.Color(TEXT_COLOR))
        label_rect = label.get_rect(center=(x_center, SCREEN_HEIGHT - 20))
        screen.blit(label, label_rect)


def draw_stage(screen, current_sprite):
    stage_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT - PALETTE_HEIGHT)
    pygame.draw.rect(screen, pygame.Color(STAGE_BG), stage_rect)

    if current_sprite is not None:
        center_x = SCREEN_WIDTH // 2
        center_y = (SCREEN_HEIGHT - PALETTE_HEIGHT) // 2
        rect = current_sprite.get_rect(center=(center_x, center_y))
        screen.blit(current_sprite, rect)

main()
```

</details>

[Download sprite-transformer.py](./sprite-transformer.py)

| Cherry | Flower | Ghost | Space Ship | Star Gem | 
|--------|--------|-------|------------|----------| 
|[Download](./cherry.png) <br> ![](./cherry.png)| [Download](./flower.png) <br> ![](./flower.png)| [Download](./ghost.png) <br> ![](./ghost.png) | [Download](./ship.png) <br> ![](./ship.png) | [Download](./star-gem.png) <br> ![](./star-gem.png) |


### Phase 0 - Identify The Missing Features

Locate each of the TODO comments in the code.

*   Which TODO items do you think will be the easiest to address?
*   Which TODO items depend on other TODO items being completed first?

### Phase 1 - Fix It

Enact your proposed changes in the program.


### Phase 2 - Test It

Pay attention to the appearance of sprites as you test the program.


### Phase 3 - Reflect On It

Answer these debrief questions in comments in today's Wooclap:

*   What kinds of visual changes do rotation and scaling produce on your sprite? Describe at least two things you noticed.
*   How does repeatedly rotating the sprite affect its appearance? Does it stay perfectly crisp? Why or why not?
*   When you scale your sprite up and then back down, does it look identical to the original? What does this tell you about image transformations?
*   Were you able to make your program slow down and crash? What do you think is happening?
*   Describe a scenario where the undo stack could get out of sync with the user’s actions. How would you prevent that?


### Phase 4 - Stretch Challenges

There are comments in the code that suggest how to implement an **undo** feature by using a Python list to keep copies of previous sprites.

*   When a list is used in this fashion we call it a **stack**
    *   **Undo** is triggered by pressing `U`
    *   Add an item to the `undo_stack` with the `.append()` method (in stack jargon we say *push the item onto the stack*)
    *   Remove an item from the `undo_stack` with the `.pop()` method (*pop* is stack jargon for *remove the top item from the stack*)
    *   Replace the `undo_stack` with an empty array when a new sprite is selected
*   Implement a **redo** feature by pushing sprites that are popped from the `undo_stack` onto a new `redo_stack`
    *   **Redo** is triggered by pressing `R`


