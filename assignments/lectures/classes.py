import drawly

class Circle:
    pass

drawly.start("user defined types")

val = Circle()

val.radius = 100
val.x_pos = 100
val.y_pos = 100
val.color = "red"

drawly.set_color(val.color)
drawly.circle(val.x_pos, val.y_pos, val.radius)

val.color = "blue"
val.radius = 50

drawly.set_color(val.color)
drawly.circle(val.x_pos, val.y_pos, val.radius)

drawly.draw()
drawly.done()