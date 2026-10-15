CS1400 - Thursday, March 05 - Lecture 18 - Module 4

# Topics:
* [🟥Assn 4b - Chessmate & Patterns](#assn-4b---chessmate--patterns)
* [Code Lab Challenge 0 - Traffic Light](#code-lab-challenge-0---traffic-light)
* [Code Lab Challenge 1 - Cookie Cutter Neighborhood](#code-lab-challenge-1---cookie-cutter-neighborhood)


------------------------------------------------------------
# Announcements

## Spring Break is Next Week

Enjoy your time off!


# [🟥Assn 4b - Chessmate & Patterns](https://usu.instructure.com/courses/794745/assignments/5122788)


| Task/Day           | **Thursday**       | **Friday** | **Saturday** | **Sunday**                             | **Monday**                                                       |
| ------------------ | ------------------ | ---------- | ------------ | -------------------------------------- | ---------------------------------------------------------------- |
| **Classroom Time** | Classroom Lab Time |            |              |                                        | **Spring Break - No School**                                     |
| **Items Due**      |                    |            |              | Assignment 4b<br/>Reflection Survey 4b | Code Reviews for <br/>Assn 4b will happen<br/>after Spring Break |


# Code Lab Challenge 0 - Traffic Light

In this challenge you will build an **interactive traffic light simulator** in Drawly.  
Your program will repeatedly ask the user which light should be on (`red`, `yellow`, or `green`).  
The traffic light will update on the screen based on the user’s input.

You will write logic inside a function that decides which light should appear **bright** and which lights should remain **dim**.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 4*


### Program Requirements

0.  Write a function with the signature: `draw_traffic_light(x, y, lit=False)`
    -   The parameter `lit` may be `"red"`, `"yellow"`, `"green"`, or any other value.
0.  When `lit` is `"red"`, `"yellow"`, or `"green"`, that light should appear **bright** while the other lights remain **dim**.
0.  When `lit` is any other value, **all lights should appear dim**.
0.  The program should repeatedly ask the user which light should turn on using `drawly.terminal_input()`.
0.  The program should display messages using `drawly.terminal_output()`.
0.  The program should use a **while loop** to continuously update the traffic light.



### Starter Code

Use this code as your starting point.  
Your task is to **add logic inside the function** to control which light becomes bright.

```python
import drawly


def draw_traffic_light(x, y, lit=False):
    """
    Draw a traffic light at position (x, y).

    lit may be:
        "red"
        "yellow"
        "green"
        False (all lights dim)
    """

    # --- pole ---
    drawly.set_color("gray")
    drawly.rectangle(x + 18, y + 120, 14, 120)

    # --- housing ---
    drawly.set_color("black")
    drawly.rectangle(x, y, 50, 130)

    dim_red_color = "darkred"
    dim_yellow_color = "goldenrod2"
    dim_green_color = "darkgreen"

    bright_red_color = "red"
    bright_yellow_color = "yellow"
    bright_green_color = "green"

    # -------------------------------------
    # STUDENTS: ADD YOUR LOGIC HERE
    # -------------------------------------

    # If lit == "red", make the red light bright
    # If lit == "yellow", make the yellow light bright
    # If lit == "green", make the green light bright
    # Otherwise, all lights should be left dim

    # -------------------------------------

    # draw lights
    drawly.set_color(red_color)
    drawly.circle(x + 25, y + 25, 15)

    drawly.set_color(yellow_color)
    drawly.circle(x + 25, y + 65, 15)

    drawly.set_color(green_color)
    drawly.circle(x + 25, y + 105, 15)
    drawly.draw()


drawly.start("Traffic Light", background="light blue", terminal=True)
drawly.set_speed(10)
light = False

while True:

    draw_traffic_light(200, 120, lit=light)
    drawly.draw()

    light = drawly.terminal_input("Which light? (red, yellow, green) ")
    if light != "red" and light != "yellow" and light != "green":
        drawly.terminal_output("Invalid input - the traffic light isn't lit!")
```



### Phase 0 - Design It

Answer each of these questions in today's Wooclap:


0.  What is the user experience?
1.  How do I get the necessary data?
2.  What do I need to process and calculate?
3.  How am I going to process and calculate?
4.  What do I need to display as results?


### Phase 1 - Pseudocode It

Using the answers to the above questions as your guide, write *pseudocode* as a block of comments in your program.  Start by describing the flow of the program in plain English.  Refine your pseudocode until it is as specific as Python code.


### Phase 2 - Build It

When your pseudocode is basically line-for-line equivalent to real Python code, rewrite each comment as code.


### Phase 3 - Reflect On It

Answer these debrief questions in comments in today's Wooclap:

* Did my pseudocode line up with the code I wrote, or did I change course while coding? Why?
* What conditionals did I use to decide which light becomes bright?
* How did the `lit` parameter change the behavior of the function?


### Phase 4 - Stretch Challenges

Did you finish early?  Was this still too easy for you?  Here are some more features to implement:

0.  Add a new command `"cycle"` that automatically cycles through red → yellow → green several times.
0.  Add a `"quit"` command that stops the program and closes the window.
0.  Draw **multiple traffic lights** on the screen and control them independently.
0.  Make the yellow light **blink** when `"yellow"` is entered.
0.  Improve the user experience by printing instructions in the terminal when the program starts.


# Code Lab Challenge 1 - Cookie Cutter Neighborhood

In this challenge you will build a **Drawly house generator** composed of several smaller functions.
Your program will draw houses on the screen using a function.  
The appearance of the house can change depending on the **keyword arguments** passed to the function.

Each part of the house (roof, frame, window, door, chimney) is already implemented as a function.  
Your job is to figure out **how to call these functions correctly from `draw_house()`**.

Each sub-function uses **keyword arguments with default values** to control colors.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 4*


### Program Requirements

0.  Implement the function:

        draw_house(x, y)

0.  Modify `draw_house()` to accept **keyword arguments** that pass color choices to the helper functions.
0.  `draw_house()` calls helper functions to draw each part of the house:

    - the frame
    - the roof
    - the window
    - the door
    - the chimney

0.  Each helper function accepts **keyword parameters with default colors**.

0.  At least one call to `draw_house()` should override some colors using keyword arguments.

0.  The main program should draw **multiple houses** in different locations.



### Starter Code

The helper functions are already written.  
Your task is to **call them correctly inside `draw_house()`**.

```python
import drawly


def draw_frame(x, y, frame_color="burlywood"):
    drawly.set_color(frame_color)
    drawly.rectangle(x, y, 120, 90)
    drawly.draw()


def draw_roof(x, y, roof_color="firebrick"):
    drawly.set_color(roof_color)
    drawly.polygon_begin()
    drawly.add_poly_point(x - 10, y)
    drawly.add_poly_point(x + 60, y - 60)
    drawly.add_poly_point(x + 130, y)
    drawly.polygon_end()
    drawly.draw()


def draw_chimney(x, y, chimney_color="dimgray"):
    drawly.set_color(chimney_color)
    drawly.rectangle(x + 80, y - 50, 20, 40)
    drawly.draw()


def draw_window(x, y, window_color="lightblue"):
    drawly.set_color(window_color)
    drawly.rectangle(x + 20, y + 25, 30, 30)
    drawly.draw()


def draw_door(x, y, door_color="saddlebrown"):
    drawly.set_color(door_color)
    drawly.rectangle(x + 70, y + 40, 25, 50)
    drawly.draw()


def draw_house(x, y):
    """Draw a complete house by calling the helper functions."""

    # STUDENTS:
    # Call the helper functions here.
    #
    # draw_frame(...)
    # draw_roof(...)
    # draw_chimney(...)
    # draw_window(...)
    # draw_door(...)

    pass


drawly.start("Drawly Houses", background="lightskyblue1")
drawly.set_speed(9)

# Draw a lawn
drawly.set_color("darkgreen")
drawly.rectangle(0, 300, 1280, 720)
drawly.draw()

# Draw some houses
draw_house(120, 250)
draw_house(320, 250)
draw_house(520, 250)

drawly.done()
```



### Phase 0 - Design It

Answer each of these questions in today's Wooclap:


0.  What is the user experience?
1.  How do I get the necessary data?
2.  What do I need to process and calculate?
3.  How am I going to process and calculate?
4.  What do I need to display as results?


### Phase 1 - Pseudocode It

Using the answers to the above questions as your guide, write *pseudocode* as a block of comments in your program.  Start by describing the flow of the program in plain English.  Refine your pseudocode until it is as specific as Python code.


### Phase 2 - Build It

When your pseudocode is basically line-for-line equivalent to real Python code, rewrite each comment as code.


### Phase 3 - Reflect On It

Answer these debrief questions in comments in today's Wooclap:

* Is it useful to break a drawing into multiple functions? Why or why not?
* How do keyword arguments make the functions more flexible?
* How did the `(x, y)` parameters help position each part of the house?
* Which parameters did you override when calling the function?
* Why are default values useful when designing functions?



### Phase 4 - Stretch Challenges

Did you finish early?  Was this still too easy for you?  Here are some more features to implement:

0.  Add a **second window** to the house.
0.  Add a **tree drawing function** and place trees near the houses.
0.  Add a parameter `scale=1.0` that changes the size of the house.
0.  Use a **for loop** to draw an entire neighborhood of houses across the screen.
0.  Add **text labels** above each house using `drawly.text()`.


