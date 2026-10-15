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
