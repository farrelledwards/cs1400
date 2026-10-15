import drawly


drawly.set_speed(10)

adjective1 = input("Give me an adjective describing an emotion: ")
adjective2 = input("Give me an adjective that describes size: ")
drawly.start(title=adjective1 + " " + adjective2 + " trees, by Bob Ross", terminal=True, terminal_lines=4)

# ask the user for a color to use for the sky
# Show the URL to the color swatches in the prompt https://www.pygame.org/docs/ref/color_list.html
drawly.terminal_output("This is the list of colors you can choose from:")
drawly.terminal_output("See https://www.pygame.org/docs/ref/color_list.html")
sky = drawly.terminal_input("What color should I paint the sky? ")
drawly.set_color(sky)
drawly.rectangle(0, 0, 1280, 720)

# draw green grass in the foreground
drawly.set_color("darkgreen")
drawly.rectangle(0, 500, 1280, 720)
drawly.draw()

# draw a grid in the background at 100px intervals

# verticals
drawly.set_color("magenta")
drawly.line(100, 0, 100, 720)
drawly.line(200, 0, 200, 720)
drawly.line(300, 0, 300, 720)
drawly.line(400, 0, 400, 720)
drawly.line(500, 0, 500, 720)
drawly.line(600, 0, 600, 720)
drawly.line(700, 0,  700, 720)
drawly.line(800, 0,  800, 720)
drawly.line(900, 0,  900, 720)
drawly.line(1000, 0, 1000, 720)
drawly.line(1100, 0, 1100, 720)
drawly.line(1200, 0, 1200, 720)
drawly.set_color("darkblue")
drawly.text(100, 0, "100")
drawly.text(300, 0, "300")
drawly.text(500, 0, "500")
drawly.text(700, 0, "700")
drawly.text(900, 0, "900")
drawly.text(1100, 0, "1100")


# horizontals
drawly.set_color("magenta")
drawly.line(0, 100, 1280, 100)
drawly.line(0, 200, 1280, 200)
drawly.line(0, 300, 1280, 300)
drawly.line(0, 400, 1280, 400)
drawly.line(0, 500, 1280, 500)
drawly.line(0, 600, 1280, 600)
drawly.line(0, 700, 1280, 700)
drawly.set_color("darkblue")
drawly.text(0, 100, "100")
drawly.text(0, 300, "300")
drawly.text(0, 500, "500")
drawly.text(0, 700, "700")

drawly.draw()


# ask the user for x coordinate for the sun
sun_x = int(drawly.terminal_input("Enter an X coordinate for the sun: "))
drawly.set_color("yellow1")
drawly.circle(sun_x, 150, 75)
drawly.draw()

# ask the user for three y coordinate for the peaks of the mountains
peak1 = int(drawly.terminal_input("Enter a Y coordinate for the 1st mountain peak [0,550]: "))
peak2 = int(drawly.terminal_input("Enter a Y coordinate for the 2nd mountain peak [0,550]: "))
peak3 = int(drawly.terminal_input("Enter a Y coordinate for the 3rd mountain peak [0,550]: "))
drawly.set_color("lightslategray")
drawly.polygon_begin()
drawly.add_poly_point(100, 550)
drawly.add_poly_point(350, peak1)
drawly.add_poly_point(500, 400)
drawly.add_poly_point(640, peak2)
drawly.add_poly_point(775, 450)
drawly.add_poly_point(950, peak3)
drawly.add_poly_point(1200, 550)
drawly.add_poly_point(100, 550)
drawly.polygon_end()
drawly.draw()

# clouds
cloud1 = int(drawly.terminal_input("Enter an X coordinate for the high cloud: "))
drawly.set_color("white")
drawly.ellipse(cloud1, 75, 340, 78)
drawly.draw()
cloud2 = int(drawly.terminal_input("Enter an X coordinate for the low cloud: "))
drawly.ellipse(cloud2, 375, 240, 98)
drawly.draw()

# draw a lake (an ellipse) on top of the grass
# ask the user for a shade of blue for the lake
lakeblue = drawly.terminal_input("What color should I paint the lake? ")
drawly.set_color(lakeblue)
drawly.ellipse(100, 550, 1100, 431)
drawly.ellipse(950, 600, 300, 131)
drawly.draw()

# draw some happy little trees and hope they land on the mountainside
treegreen = drawly.terminal_input("What color should I paint the trees? ")
drawly.set_color(treegreen)

# Tree #1
drawly.polygon_begin()
drawly.add_poly_point(50, 600)
drawly.add_poly_point(75, 500)
drawly.add_poly_point(100, 600)
drawly.polygon_end()
drawly.draw()

# Tree #2
drawly.polygon_begin()
drawly.add_poly_point(150, 610)
drawly.add_poly_point(175, 510)
drawly.add_poly_point(200, 610)
drawly.polygon_end()
drawly.draw()

# Tree #3
drawly.polygon_begin()
drawly.add_poly_point(125, 650)
drawly.add_poly_point(150, 550)
drawly.add_poly_point(175, 650)
drawly.polygon_end()
drawly.draw()

# Tree #4
drawly.polygon_begin()
drawly.add_poly_point(250, 594)
drawly.add_poly_point(275, 494)
drawly.add_poly_point(300, 594)
drawly.polygon_end()
drawly.draw()

# Tree #5
drawly.polygon_begin()
drawly.add_poly_point(925, 566)
drawly.add_poly_point(950, 466)
drawly.add_poly_point(975, 566)
drawly.polygon_end()
drawly.draw()

# Tree #6
drawly.polygon_begin()
drawly.add_poly_point(1025, 588)
drawly.add_poly_point(1050, 488)
drawly.add_poly_point(1075, 588)
drawly.polygon_end()
drawly.draw()

# Sign your work!
drawly.set_color("black")
drawly.text(950, 685, "signed: Bob Rossinator")
drawly.draw()

drawly.terminal_output("Behold my masterpiece: ", adjective1, adjective2, "trees!")
drawly.done()
