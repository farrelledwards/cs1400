# battleship.py

##
## Don't change anything below this comment
##

import pygame

import bs_ai
import bs_board
import bs_config
import bs_drawing


def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((bs_config.SCREEN_WIDTH, bs_config.SCREEN_HEIGHT))
    pygame.display.set_caption(bs_config.TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########
    font = pygame.font.SysFont("courier", 24)
    title_font = pygame.font.SysFont("courier", 32)

    ##########
    # Set up game data
    ##########
    # Create 2D lists for game boards
    player_board = bs_board.create_board()
    opponent_board = bs_board.create_board()

    # Place ships randomly on both boards
    bs_board.place_ships_randomly(player_board)
    bs_board.place_ships_randomly(opponent_board)

    # Game state
    player_turn = True
    last_message = "Click on the opponent's board to make a guess!"

    # AI state - list of available positions to guess
    ai_available_positions = bs_ai.initialize_available_positions()

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
                    # Reset game by creating new 2D lists and placing ships
                    player_board = bs_board.create_board()
                    opponent_board = bs_board.create_board()
                    bs_board.place_ships_randomly(player_board)
                    bs_board.place_ships_randomly(opponent_board)
                    player_turn = True
                    last_message = "Click on the opponent's board to make a guess!"
                    ai_available_positions = bs_ai.initialize_available_positions()
                    game_over = False

            # Handle mouse clicks for making guesses
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player_turn:
                mx, my = event.pos
                # Check if click is on opponent board
                row, col = bs_drawing.cell_from_pixel(mx, my, bs_config.OPPONENT_BOARD_X, bs_config.OPPONENT_BOARD_Y)
                if row != -1 and col != -1:
                    result = bs_board.make_guess(opponent_board, row, col)
                    if result == 'hit':
                        last_message = f"Hit at {chr(ord('A') + row)}{col + 1}!"
                        # Check if all ships are sunk
                        if bs_board.all_ships_sunk(opponent_board):
                            game_over = True
                            last_message = "You Win! All enemy ships destroyed!"
                        else:
                            # Switch to AI turn
                            player_turn = False
                    elif result == 'miss':
                        last_message = f"Miss at {chr(ord('A') + row)}{col + 1}!"
                        # Switch to AI turn
                        player_turn = False
                    elif result == 'invalid':
                        last_message = "You already guessed that location!"

        ##########
        # Update state of components/data
        ##########
        #### Always Update ####

        #### Update if Game is Not Over ####
        if not game_over:
            # AI takes a turn
            if not player_turn:
                row, col = bs_ai.ai_make_guess(ai_available_positions)
                if row is not None and col is not None:
                    result = bs_board.make_guess(player_board, row, col)
                    if result == 'hit':
                        last_message = f"AI hit at {chr(ord('A') + row)}{col + 1}!"
                        # Check if all player ships are sunk
                        if bs_board.all_ships_sunk(player_board):
                            game_over = True
                            last_message = "AI Wins! All your ships destroyed! Press SPACE to play again."
                        # AI keeps turn on hit (optional - can switch if you want)
                        player_turn = True
                    elif result == 'miss':
                        last_message = f"AI missed at {chr(ord('A') + row)}{col + 1}!"
                        player_turn = True
        #### Update if Game is Over ####
        else:
            pass

        ##########
        # Update Display
        ##########
        #### Always Display ####
        screen.fill(bs_config.COLOR_BG)

        # Draw board labels
        player_label = title_font.render("Your Board", True, bs_config.COLOR_TEXT)
        opponent_label = title_font.render("Opponent Board", True, bs_config.COLOR_TEXT)
        screen.blit(player_label, (bs_config.PLAYER_BOARD_X, bs_config.PLAYER_BOARD_Y - 40))
        screen.blit(opponent_label, (bs_config.OPPONENT_BOARD_X, bs_config.OPPONENT_BOARD_Y - 40))

        #### Display while Game is being played ####
        if not game_over:
            # Draw both boards by iterating through their 2D lists
            # Player board shows ships
            bs_drawing.draw_board(screen, player_board, bs_config.PLAYER_BOARD_X, bs_config.PLAYER_BOARD_Y, True, font)
            # Opponent board doesn't show ships (only hits/misses)
            bs_drawing.draw_board(screen, opponent_board, bs_config.OPPONENT_BOARD_X, bs_config.OPPONENT_BOARD_Y, False, font)

            # Draw status message
            bs_drawing.draw_status_text(screen, font, last_message, 600)

            # Draw instructions based on whose turn it is
            if player_turn:
                instructions = "Your turn - Click on the opponent's board to make a guess"
            else:
                instructions = "AI's turn - waiting..."
            bs_drawing.draw_status_text(screen, font, instructions, 650)
        #### Display while Game is Over ####
        else:
            # Draw both boards
            bs_drawing.draw_board(screen, player_board, bs_config.PLAYER_BOARD_X, bs_config.PLAYER_BOARD_Y, True, font)
            bs_drawing.draw_board(screen, opponent_board, bs_config.OPPONENT_BOARD_X, bs_config.OPPONENT_BOARD_Y, True, font)

            # Draw game over message
            bs_drawing.draw_status_text(screen, title_font, last_message, 600)
            bs_drawing.draw_status_text(screen, font, "Press SPACE to play again", 650)

        #### Draw changes the screen ####
        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(bs_config.CLOCK_TICK)


main()
