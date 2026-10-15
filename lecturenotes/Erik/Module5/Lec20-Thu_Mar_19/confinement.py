# confinement.py

import pygame
import random
import math


# Use named constants to avoid writing "magic numbers" all throughout the program
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CLOCK_TICK = 30
TITLE = "Confined Bouncing Shapes"
CIRCLE_FENCE_CENTER = (300, 300)
CIRCLE_FENCE_RADIUS = 250
BOX_FENCE_POS = (650, 50, 500, 500)
FENCE_THICKNESS = 30


def check_circle_collision(orb_pos, orb_radius):
    """
    Has the orb collided with its circular fence?
    """
    # TODO: implement this function
    #
    # Take into account the thickness of the wall so the orb appears
    # to bounce as soon as it touches the inside edge of the wall.
    #
    # The return statement will answer this question:
    # "Is the distance of the orb from the center of the fence plus the orb's radius greater than or equal to the radius of the circular fence minus its thickness?"
    return False


def check_box_horizontal_collision(box_pos, box_width):
    """Has the box collided with the left or right walls?"""
    # TODO: implement this function
    #
    # Take into account the thickness of the walls so the box appears
    # to bounce as soon as it touches the inside edge of the wall.
    #
    # The return statement should use the 'or' keyword, like this:
    #   return SOMETHING or SOMETHING
    # and answer these questions:
    # "has the left edge of the box touched or crossed the inner edge of the left wall?"
    #   OR
    # "has the right edge of the box touched or crossed the inner edge of the right wall?"
    return False


def check_box_vertical_collision(box_pos, box_height):
    """Has the box collided with the top or bottom walls?"""
    # TODO: implement this function
    #
    # Take into account the thickness of the walls so the box appears
    # to bounce as soon as it touches the inside edge of the wall.
    #
    # The return statement should use the 'or' keyword, like this:
    #   return SOMETHING or SOMETHING
    # and answer these questions:
    # "has the top edge of the box touched or crossed the inner edge of the top wall"?
    #   OR
    # "has the bottom edge of the box touched or crossed the inner edge of the bottom wall"?
    return False


def draw_circle_fence(surface, pos, radius):
    pygame.draw.circle(surface, "red", pos, radius, FENCE_THICKNESS)


def draw_box_fence(surface, box):
    pygame.draw.rect(surface, "blue", box, FENCE_THICKNESS)


def update_pos(pos, vect):
    return [pos[0] + vect[0], pos[1] + vect[1]]


def bounce_orb(pos, radius, mvmt):
    """Calculate and return a new movement vector after bouncing off the circular fence"""
    # Calculate normal vector from center to orb
    dx = pos[0] - CIRCLE_FENCE_CENTER[0]
    dy = pos[1] - CIRCLE_FENCE_CENTER[1]
    distance = math.sqrt(dx**2 + dy**2)

    # TODO: Why is this if statement here?
    if distance > 0.0:
        # Normalize velocity
        normal_x = dx / distance
        normal_y = dy / distance

        # Reflect velocity vector
        dot_product = mvmt[0] * normal_x + mvmt[1] * normal_y

        # Create a new movement vector by copying the old one
        new_mvmt = list(mvmt)

        # Apply the bounce direction
        new_mvmt[0] -= 2 * dot_product * normal_x
        new_mvmt[1] -= 2 * dot_product * normal_y

        # STRETCH CHALLENGE: Play the boing sound when a bounce occurs
        # STRETCH CHALLENGE: Add a little randomness to new_mvmt

        return new_mvmt


def bounce_box_horizontally(mvmt):
    """Calculate and return a new movement vector after bouncing off the box fence's horizontal walls"""
    # Create a new movement vector by copying the old one
    new_mvmt = list(mvmt)

    # invert the X direction
    new_mvmt[0] = -new_mvmt[0]

    # STRETCH CHALLENGE: Play the boing sound when a bounce occurs
    # STRETCH CHALLENGE: Add randomness to vertical component when hitting horizontal walls

    return new_mvmt


def bounce_box_vertically(mvmt):
    """Calculate and return a new movement vector after bouncing off the box fence's horizontal walls"""
    # Create a new movement vector by copying the old one
    new_mvmt = list(mvmt)

    # invert the Y direction
    new_mvmt[1] = -new_mvmt[1]

    # STRETCH CHALLENGE: Play the boing sound when a bounce occurs
    # STRETCH CHALLENGE: Add randomness to horizontal component when hitting vertical walls

    return new_mvmt


def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()


    ##########
    # Set up game media images, sounds
    ##########
    orb = pygame.image.load("orb.png")
    box = pygame.image.load("box.png")


    ##########
    # Set up game data
    ##########
    # TODO: Answer these questions
    #   - What does min() do?
    #   - If you knew the dimensions of orb.png, would this code be necessary?
    orb_radius = min(orb.get_width(), orb.get_height()) // 2
    box_width = box.get_width()
    box_height = box.get_height()

    # STRETCH CHALLENGE: Introduce an element of randomness to the starting attributes of the bouncing shapes

    # Initial Orb Movement Vector
    orb_mvmt = [3, 7]
    # Orb Initial Position - start in the center of the fence
    orb_pos = [CIRCLE_FENCE_CENTER[0], CIRCLE_FENCE_CENTER[1]]

    # Initial Box Movement Vector
    box_mvmt = [6, 4]
    # Box Initial Position - start in the center of the fence
    box_pos = [BOX_FENCE_POS[0] + BOX_FENCE_POS[2] // 2, BOX_FENCE_POS[1] + BOX_FENCE_POS[3] // 2]


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
                    game_over = False

        ##########
        # Update state of components/data
        ##########
        #### Always Update ####

        # Update Orb position
        orb_pos = update_pos(orb_pos, orb_mvmt)

        # Check collision with circle fence and bounce off the wall
        if check_circle_collision(orb_pos, orb_radius):
            orb_mvmt = bounce_orb(orb_pos, orb_radius, orb_mvmt)

        # Update box position
        box_pos = update_pos(box_pos, box_mvmt)

        # Check collisions with box fences and bounce off the walls
        if check_box_horizontal_collision(box_pos, box_width):
            box_mvmt = bounce_box_horizontally(box_mvmt)

        if check_box_vertical_collision(box_pos, box_height):
            box_mvmt = bounce_box_vertically(box_mvmt)

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
        screen.fill("white")

        # draw the circle fence & orb
        draw_circle_fence(screen, CIRCLE_FENCE_CENTER, CIRCLE_FENCE_RADIUS)
        screen.blit(orb, (orb_pos[0] - orb.get_width() // 2, orb_pos[1] - orb.get_height() // 2))

        # draw the box fence & box
        draw_box_fence(screen, BOX_FENCE_POS)
        screen.blit(box, (box_pos[0] - box.get_width() // 2, box_pos[1] - box.get_height() // 2))

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
        clock.tick(CLOCK_TICK)


main()
