import drawly
import time
import random

class Game:
    pass

game = Game()
game.SPEED = 10
game.SCREEN_WIDTH = 720
game.SCREEN_HEIGHT = 720
game.SCORE_GOAL = 10
game.POINT_LIST = [5, 4, 3, 2, 1]
game.BG = "gray"
game.score = 0


class Meter:
    pass

meter = Meter()
meter.FRAMES = 5
meter.INCR = 12
meter.X = 565
meter.Y = 55
meter.W = 100
meter.H = 600
meter.BG = "white"
meter.CORRECT = "green"
meter.WRONG = "red"
meter.score = 0
meter.top = 0


class Scoreboard:
    pass

sb = Scoreboard()
sb.BG = "white"
sb.FG = "black"
sb.SIZE = 30
sb.X = 55
sb.Y = 55
sb.W = 200
sb.H = 50
sb.TEXT_X = 65
sb.TEXT_Y = 65
sb.score = 0


def update_score(diff):
    direction = 1
    color = meter.CORRECT
    if diff < 0:
        direction = -1
        color = meter.WRONG
        
    for i in range(abs(diff) * meter.FRAMES):
        delta = direction / meter.FRAMES
        game.score += delta
        draw_score()
        draw_meter(color)
        drawly.draw()
    

def draw_score():
    drawly.set_color(game.BG)
    drawly.rectangle(10, 10, 100, 125)
    drawly.set_color("black")
    drawly.text(10, 10, str(int(game.score)), 25, "arial")

def draw_meter(color):
    drawly.set_color(meter.BG)
    drawly.rectangle(meter.X, meter.Y, meter.W, meter.H)
    perc = game.score / game.SCORE_GOAL
    drawly.set_color(color)
    drawly.rectangle(meter.X, meter.Y, meter.W, meter.H * perc)


drawly.start("My window", background=game.BG, dimensions=(game.SCREEN_WIDTH, game.SCREEN_HEIGHT), terminal=True, terminal_lines=4)
drawly.set_speed(game.SPEED)
drawly.terminal_input("Press enter to begin:")


while True:
    # Problem
    val1 = random.randint(1, 4)
    val2 = random.randint(1, 4)
    operand_val = random.randint(1, 3)
    correct = 0
    if operand_val == 0:
        str_val = str(val1) + " + " + str(val2) + " = "
        correct = val1 + val2
    elif operand_val == 1:
        str_val = str(val1) + " - " + str(val2) + " = "
        correct = val1 - val2
    else:
        str_val = str(val1) + " * " + str(val2) + " = "
        correct = val1 * val2
    
    start_time = time.perf_counter()
    answer = int(drawly.terminal_input(str_val))
    elapsed_time = time.perf_counter() - start_time
    print(answer, elapsed_time)
    multiplier = 1
    if elapsed_time < 1:
        multiplier = 5
    elif elapsed_time < 2:
        multiplier = 4
    elif elapsed_time < 3:
        multiplier = 3
    elif elapsed_time < 4:
        multiplier = 2
    if answer == correct:
        update_score(multiplier)
    else:
        update_score(-multiplier)


drawly.draw()
drawly.done()
