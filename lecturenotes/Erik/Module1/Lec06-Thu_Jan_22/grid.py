import drawly


drawly.start("Drawly Arc Demo")
drawly.set_speed(10)

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

## Draw some arcs here

drawly.done()
