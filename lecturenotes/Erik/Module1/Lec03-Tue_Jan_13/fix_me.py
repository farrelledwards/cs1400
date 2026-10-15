# fix_me.py
import drawly


# BUG 0: There's a simple syntax problem on this line
drawly.start("Fix My Bug - Shapes", background="lightgrey"


# BUG 1: This function needs a number - I recommend 10
drawly.set_speed()


# TODO: (Optional) paste your grid code here


# Filled red circle
#   centered at coordinate (250, 250)
#   radius of 120
# BUG 2: Something is wrong with the parameters here (hint: order matters)
drawly.set_color("red")
drawly.circle(250, 120, 250)
drawly.draw()

# Filled blue rectangle
#   upper-left corner at (200, 200)
#   width=260
#   height=130
# BUG 3: A required parameter is missing
drawly.set_color("blue")
drawly.rectangle(200, 260, 130)
drawly.draw()

# Outlined brown rectangle
#   upper-left corner at (950, 160)
#   width=260
#   height=120
#   stroke thickness = 6 pixels
# BUG 4: One parameter name is wrong (typo-level wrong)
drawly.set_color("brown")
drawly.rectangle(950, 160, 260, 120, stoke=6)
drawly.draw()

# Outlined purple ellipse 
#   bounding box upper-left corner at (720, 320)
#   bounding box width=120
#   bounding box height=280
#   stroke thickness = 8 pixels
# BUG 5: One parameter does not belong in this call
drawly.ellipse("purple", 720, 320, 120, 280, 8)
drawly.draw()

# Crossing orange diagonal lines
# BUG 6: One of these lines is missing a parameter
drawly.set_color("orange")
drawly.line(480, 180, 820, 480, 6)
drawly.line(820, 180, 480, 6)
drawly.draw()

# Green label text
# BUG 7: This call has a simple problem (look closely)
drawly.set_color("green")
drawly.text(40, 30, Shapes!, 48)
drawly.draw()


# BUG 8: This call is missing something (look closely)
drawly.done)
