# arkanoid.py
import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 820
CLOCK_TICK = 30
TITLE = "Arkanoid"
PADDLE_SPEED = 10
BALL_SPEED_X = 6
BALL_SPEED_Y = 5
BLOCK_ROWS = 4
BLOCK_COLS = 6
BLOCK_SPACING = 10


class Ball:
    pass


class Paddle:
    pass


class Block:
    pass


def make_ball(filename, screen_width, screen_height):
    """Create and return a ball object"""
    ball = Ball()
    ball.image = pygame.image.load(filename)
    ball.width = ball.image.get_width()
    ball.height = ball.image.get_height()
    ball.x = screen_width // 2
    ball.y = screen_height // 2
    ball.vx = BALL_SPEED_X
    ball.vy = BALL_SPEED_Y
    return ball


def make_paddle(filename, screen_width, screen_height):
    """Create and return a paddle object"""
    paddle = Paddle()
    paddle.image = pygame.image.load(filename)
    paddle.width = paddle.image.get_width()
    paddle.height = paddle.image.get_height()
    paddle.x = screen_width // 2 - paddle.width // 2
    paddle.y = screen_height - 50
    return paddle


def make_blocks(filename, screen_width):
    """Create and return a list of block objects"""
    blocks = []
    block_image = pygame.image.load(filename)
    block_width = block_image.get_width()
    block_height = block_image.get_height()
    start_x = (screen_width - (BLOCK_COLS * block_width + (BLOCK_COLS - 1) * BLOCK_SPACING)) // 2
    start_y = 40

    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLS):
            block = Block()
            block.img = block_image
            block.width = block_width
            block.height = block_height
            block.x = start_x + col * (block.width + BLOCK_SPACING)
            block.y = start_y + row * (block.height + BLOCK_SPACING)
            block.active = True
            blocks.append(block)

    return blocks


def get_ball_rect(ball):
    """Return the left, right, top, bottom edges of the ball"""
    left = ball.x - ball.width // 2
    right = ball.x + ball.width // 2
    top = ball.y - ball.height // 2
    bottom = ball.y + ball.height // 2
    return (left, right, top, bottom)


def get_paddle_rect(paddle):
    """Return the left, right, top, bottom edges of the paddle"""
    left = paddle.x
    right = paddle.x + paddle.width
    top = paddle.y
    bottom = paddle.y + paddle.height
    return (left, right, top, bottom)


def get_block_rect(block):
    """Return the left, right, top, bottom edges of a block"""
    left = block.x
    right = block.x + block.width
    top = block.y
    bottom = block.y + block.height
    return (left, right, top, bottom)


def rects_overlap(rect1, rect2):
    """
    Check if two rectangles overlap.
    Each rect is a tuple of (left, right, top, bottom)
    """
    # TODO: Implement this function
    # Two rectangles overlap if:
    # - rect1's right edge is past rect2's left edge, AND
    # - rect1's left edge is before rect2's right edge, AND
    # - rect1's bottom edge is past rect2's top edge, AND
    # - rect1's top edge is before rect2's bottom edge
    #
    # In other words, they do NOT overlap if:
    # - rect1 is completely to the left of rect2, OR
    # - rect1 is completely to the right of rect2, OR
    # - rect1 is completely above rect2, OR
    # - rect1 is completely below rect2
    return False


def update_ball(ball, paddle, blocks, screen_width, screen_height):
    """Update ball position and handle collisions"""
    # Move the ball
    ball.x += ball.vx
    ball.y += ball.vy

    # Bounce off top and bottom walls
    if ball.y - ball.height // 2 <= 0:
        ball.vy = -ball.vy
        ball.y = ball.height // 2

    if ball.y + ball.height // 2 >= screen_height:
        return False  # Game over (ball fell below paddle)

    # Bounce off left and right walls
    if ball.x - ball.width // 2 <= 0:
        ball.vx = -ball.vx
        ball.x = ball.width // 2

    if ball.x + ball.width // 2 >= screen_width:
        ball.vx = -ball.vx
        ball.x = screen_width - ball.width // 2

    # TODO: Implement collision detection with the paddle
    # Steps:
    # 1. Get the ball and paddle rectangles using get_ball_rect() and get_paddle_rect()
    # 2. Check if they overlap using rects_overlap()
    # 3. If they do:
    #    a. Reverse the ball's vertical velocity (ball.vy = -ball.vy)
    #    b. Move the ball to be above the paddle (ball.y = paddle.y - ball.height // 2)

    # TODO: Implement collision detection with blocks
    # For each active block in the blocks list:
    # 1. Get the block's rectangle using get_block_rect()
    # 2. Check if it overlaps with the ball using rects_overlap()
    # 3. If it does:
    #    a. Set block.active = False to destroy the block
    #    b. Determine collision direction by comparing distances:
    #       - dx = abs(ball.x - (block.x + block.width // 2))
    #       - dy = abs(ball.y - (block.y + block.height // 2))
    #       - If dx > dy: ball hit from side → reverse ball.vx
    #       - Otherwise: ball hit from top/bottom → reverse ball.vy
    #    c. Break out of the loop (only process one collision per frame)

    return True  # Game continues


def move_paddle(paddle, direction, screen_width):
    """Move paddle left or right, keeping it in bounds"""
    # TODO: Update the paddle's x position by direction * PADDLE_SPEED
    # Hint: paddle.x += direction * PADDLE_SPEED

    # TODO: Ensure the paddle stays within the screen bounds
    # The left edge should not go below 0
    # The right edge should not go beyond screen_width
    # Hint: Use if statements to check and correct paddle.x
    pass


def all_blocks_destroyed(blocks):
    """Check if all blocks have been destroyed"""
    # TODO: Implement this function
    # Return True if all blocks have active = False
    # Return False if any block still has active = True
    # Hint: Use a for loop and check block.active for each block
    return False


def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images
    ##########
    background_color = (30, 30, 30)
    ball = make_ball("ball.png", SCREEN_WIDTH, SCREEN_HEIGHT)
    paddle = make_paddle("paddle-large.png", SCREEN_WIDTH, SCREEN_HEIGHT)
    blocks = make_blocks("emerald_brick.png", SCREEN_WIDTH)

    ##########
    # Set up game data
    ##########
    game_over = False
    game_won = False
    running = True

    ##########
    # Game Loop
    ##########
    while running:
        ##########
        # Get Input/Events
        ##########
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE and (game_over or game_won):
                    # Reset the game
                    game_over = False
                    game_won = False
                    ball = make_ball("ball.png", SCREEN_WIDTH, SCREEN_HEIGHT)
                    paddle = make_paddle("paddle-large.png", SCREEN_WIDTH, SCREEN_HEIGHT)
                    blocks = make_blocks("emerald_brick.png", SCREEN_WIDTH)

        ##########
        # Update state of components/data
        ##########
        #### Always Update ####
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            move_paddle(paddle, -1, SCREEN_WIDTH)
        if keys[pygame.K_RIGHT]:
            move_paddle(paddle, 1, SCREEN_WIDTH)

        #### Update if Game is Not Over ####
        if not game_over and not game_won:
            game_over = not update_ball(ball, paddle, blocks, SCREEN_WIDTH, SCREEN_HEIGHT)
            if not game_over:
                game_won = all_blocks_destroyed(blocks)

        ##########
        # Update Display
        ##########
        #### Always Display ####
        screen.fill(background_color)

        # Draw blocks
        for block in blocks:
            if block.active:
                screen.blit(block.img, (block.x, block.y))

        # Draw ball
        screen.blit(ball.image, (ball.x - ball.width // 2, ball.y - ball.height // 2))

        # Draw paddle
        screen.blit(paddle.image, (paddle.x, paddle.y))

        #### Display while Game is being played ####
        if not game_over and not game_won:
            pass

        #### Display while Game is Over (Lost) ####
        if game_over:
            text_font = pygame.font.SysFont("timesnewroman", 80).render("Game Over", True, (255, 0, 0))
            screen.blit(text_font, [SCREEN_WIDTH // 2 - text_font.get_width() // 2, SCREEN_HEIGHT // 2 - 100])

            text_font_small = pygame.font.SysFont("timesnewroman", 40).render("Press SPACE to Restart", True, (200, 200, 200))
            screen.blit(text_font_small, [SCREEN_WIDTH // 2 - text_font_small.get_width() // 2, SCREEN_HEIGHT // 2 + 50])

        #### Display while Game is Won ####
        if game_won:
            text_font = pygame.font.SysFont("timesnewroman", 80).render("You Won!", True, (0, 255, 0))
            screen.blit(text_font, [SCREEN_WIDTH // 2 - text_font.get_width() // 2, SCREEN_HEIGHT // 2 - 100])

            text_font_small = pygame.font.SysFont("timesnewroman", 40).render("Press SPACE to Restart", True, (200, 200, 200))
            screen.blit(text_font_small, [SCREEN_WIDTH // 2 - text_font_small.get_width() // 2, SCREEN_HEIGHT // 2 + 50])

        #### Draw changes to the screen ####
        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)


main()
