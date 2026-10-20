import drawly

drawly.start("Day 5", background="grey", terminal=True, dimensions=(720,480))

name = drawly.terminal_input("What's your name?  ")
age = int(drawly.terminal_input("How old are you?  "))
drawly.set_color("red")
drawly.line(1, 1, 100, 100, 50)
drawly.draw()
#drawly.terminal_output("Hello", name, "!  In 10 years you're going to be ", age + 10)

drawly.done()