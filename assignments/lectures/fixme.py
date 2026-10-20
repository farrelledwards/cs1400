# fix_me.py
import joe













drawly.start("Fix My Bug - Shapes", background="lightgrey")

drawly.set_speed(1)


# Filled red circle
#   centered at coordinate (250, 250)
#   radius of 120
drawly.set_color("red")
drawly.circle(250, 250, 120)
drawly.draw()

# Filled blue rectangle
#   upper-left corner at (200, 200)
#   width=260
#   height=130
drawly.set_color("blue")
drawly.rectangle(200, 200, 260, 130)
drawly.draw()

# Outlined brown rectangle
#   upper-left corner at (950, 160)
#   width=260
#   height=120
#   stroke thickness = 6 pixels
drawly.set_color("brown")
drawly.rectangle(950, 160, 260, 120, stroke=6)
drawly.draw()

# Outlined purple ellipse
#   bounding box upper-left corner at (720, 320)
#   bounding box width=120
#   bounding box height=280
#   stroke thickness = 8 pixels
drawly.set_color("purple")
drawly.ellipse(720, 320, 120, 280, 8)
drawly.draw()

# Crossing orange diagonal lines
drawly.set_color("orange")
drawly.line(480, 180, 820, 480, 6)
drawly.line(820, 180, 480, 820, 6)
drawly.draw()

# Green label text
drawly.set_color("green")
drawly.text(40, 30, "SHAPES", 48)
drawly.draw()


# BUG 8: This call is missing something (look closely)
drawly.done()