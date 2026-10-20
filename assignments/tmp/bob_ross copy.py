import drawly


drawly.set_speed(10)

drawly.start(title="Happy Little trees, by Bob Ross")

drawly.set_color("aqua")
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


# draw the sun
drawly.set_color("yellow1")
drawly.circle(750, 150, 75)
drawly.draw()

# Three mountain peaks
drawly.set_color("lightslategray")
drawly.polygon_begin()
drawly.add_poly_point(100, 550)
drawly.add_poly_point(350, 117)
drawly.add_poly_point(500, 400)
drawly.add_poly_point(640, 320)
drawly.add_poly_point(775, 450)
drawly.add_poly_point(950, 210)
drawly.add_poly_point(1200, 550)
drawly.add_poly_point(100, 550)
drawly.polygon_end()
drawly.draw()

# two clouds
drawly.set_color("white")
drawly.ellipse(801, 75, 340, 78)
drawly.draw()
drawly.ellipse(222, 375, 240, 98)
drawly.draw()

# draw a lake (an ellipse) on top of the grass
drawly.set_color("blue")
drawly.ellipse(100, 550, 1100, 431)
drawly.ellipse(950, 600, 300, 131)
drawly.draw()

# draw some happy little trees and hope they land on the mountainside
drawly.set_color("forestgreen")

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

print("Behold my masterpiece: ", "Happy Little trees!")
drawly.done()