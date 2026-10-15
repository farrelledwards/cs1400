CS1400 - Tuesday, January 20 - Lecture 5 - Module 1

# Topics:
* [🟥Assn 1b - Faceinator](#assn-1b---faceinator)
* [Basic Python I/O](#basic-python-io)
* [The Drawly Terminal](#the-drawly-terminal)
* [Code Lab Challenge 0 - What Does + Mean In Python](#code-lab-challenge-0---what-does--mean-in-python)
* [Code Lab Challenge 1 - Drawing Happy Little Trees Interactively](#code-lab-challenge-1---drawing-happy-little-trees-interactively)


------------------------------------------------------------
# Announcements

## *TOMORROW* USU SPRING STEM CAREER FAIR

![](./00-spring-stem-career-fair-2026.png)

*   **When**  January 21st 3:00 PM-7:00 PM
*   **Where** TSC Ballroom

Career Fairs are one of the most important events a student can attend while going to school. It is one of the most personable ways students and employers can network with each other for career opportunities.

The USU STEM Career Fair is open to all majors but is targeted towards Science, Technology, Engineering and Mathematics majors.  The STEM Fair provides students with the opportunity to network/recruit with technology-based companies.


## *TOMORROW* Student Organization for Cybersecurity (SOC) - BOT vs Bots

Are you interested in learning how to hack (ethically), find vulnerabilities, and secure your applications? Join us as we explore cybersecurity skills, participate in competitions, get certifications, network with cyber professionals, and meet like-minded students!

- **When** Wednesdays 7PM
- **Where** Huntsman Hall 360
- **Discord** https://discord.gg/JEVdRdfpEb

This Week: **BOT vs Bots**

- A collaboration with the Baddies of Tech club
- Explore some common web exploitation vulnerabilities and exploit them to hack robots
- Connect with other tech and cyber-focused students!


# [🟥Assn 1b - Faceinator](https://usu.instructure.com/courses/794745/assignments/5122782)

*   This assignment has one task
*   Read the instructions *carefully*, but also look at the **rubric**
    *   The rubric can be used as a checklist for your assignments
*   This assignment is due **at 11:59 PM on Sunday, January 25th**

## Task 1 - Faceinator

It's time to make an interactive program. You will use everything you know to create a program to interact with a user. The user will enter information to draw a face.

*   This is a *Drawly* program that also uses the *console* to take input from the user.
*   Put your code in a file called `task1.py`
*   You will use knowledge from these sections of Unit 1
    *   **1.4: Input and Variables**
    *   **1.5: On Data Types**
    *   **1.6: Commenting and Demo Project**


| Task/Day           | **Tuesday**        | **Wednesday**                    | **Thursday**       | **Friday**                                                     | **Saturday** | **Sunday**                             | **Monday**                          |
| ------------------ | ------------------ | -------------------------------- | ------------------ | -------------------------------------------------------------- | ------------ | -------------------------------------- | ----------------------------------- |
| **Classroom Time** | Classroom Lab Time | 1.6: Commenting and Demo Project | Classroom Lab Time |                                                                |              |                                        | 2.1: Arithmetic                     |
| **Items Due**      |                    |                                  |                    | Exercises 1.3.2, 1.4.3, 1.5.2, 1.5.3<br/>Quizzes 1.4, 1.5, 1.6 |              | Assignment 1b<br/>Reflection Survey 1b | Code Reviews for <br/>Assn 1b begin |


# Basic Python I/O

*I/O is short for Input/Output,* and is how we refer to the ways we get data into and out of a computer.  A computer without I/O capabilities is useless (unless you want to warm up the room).

The most basic way a program can perform I/O is by printing text to a screen called a **Terminal** and reading keystrokes typed by a user.  When you run a program from within PyCharm, the terminal appears as a black window with white text that pops up from the bottom of the screen.  You can dismiss it by clicking the minimize button (which looks like an underscore `_`)

Python has two built-in functions basic text I/O:

*   `print()`
    -   Writes a single line of output in the terminal
        -   With no parameters a blank like is printed.
        -   A space is inserted between multiple parameters.
*   `input()`
    *   This function is how we get can information from the keyboard into a program
        *   It takes a string value as an argument, which becomes a **prompt**
        *   For readability's sake, it's a good idea to end prompts with a *colon* followed by a *space* `: `
        *   The `input()` function yields a **return value**, which is how we get output back from a function
    *   The return value is whatever the user typed; this can be saved in a variable

**Example:**

```python
print("WELCOME TO MY PROGRAM")
print()  # output a blank line before the prompts

user_name = input("Enter your name: ")
age = input("Enter your age: ")
fav_color = input("Enter your favorite color: ")

print("Hello,", user_name, ". I like blue, but", fav_color, "is okay.  Wow,", age, "years old!")
input("PRESS ENTER TO CONTINUE")
input("PRESS ENTER TO QUIT")
```


# The Drawly Terminal

Basic text I/O with `print()` and `input()` is tedious for some students because of the need to switch between the Drawly window and PyCharm.  Drawly can draw a terminal in its window to remove this hassle.

*   The Drawly terminal is enabled by giving the named parameter `terminal=True` to `drawly.start()`
*   If the Drawly terminal spills off the bottom of your computer's screen, make these adjustments:
    *   Make the Drawly window shorter with `dimensions=(640, 480)` (experiment with these values)
    *   Give a smaller value to `drawly.start()`'s `terminal_lines` parameter (its default is `8`)
    *   Give a smaller value to `drawly.start()`'s `terminal_line_height` parameter (its default is `25`)


Three functions in the Drawly package let users interact with the terminal:

#### `drawly.terminal_output()`

-   This function works just like ordinary `print()`, and outputs a single line of text to the terminal
    -   With no parameters a blank like is printed
    -   A space is inserted between multiple parameters
-   *An exception is raised if the Drawly terminal was not enabled*


#### `drawly.terminal_input()`

-   Prompts user for a line of input in the terminal
    -   The user's input is returned as a string value; this can be saved in a variable
-   An optional prompt string can be given as an argument; it defaults to the empty string
-   *An exception is raised if the Drawly terminal was not initialized*


#### `drawly.terminal_clear()`

-   Clears the terminal window

**Example:**

```python
import drawly


drawly.start(terminal=True, terminal_lines=6, terminal_line_height=17)

drawly.terminal_output("WELCOME TO MY PROGRAM")
drawly.terminal_output()  # output a blank line before the prompts

user_name = drawly.terminal_input("Enter your name: ")
age = drawly.terminal_input("Enter your age: ")
fav_color = drawly.terminal_input("Enter your favorite color: ")

drawly.terminal_output("Hello,", user_name, ". I like blue, but", fav_color, "is okay.  Wow,", age, "years old!")
drawly.terminal_input("PRESS ENTER TO CONTINUE")
drawly.terminal_clear()
drawly.terminal_input("PRESS ENTER TO QUIT")

# No call to drawly.done() means this program will quit now
```


# Code Lab Challenge 0 - What Does + Mean In Python?

### Phase 0 - Study it

Discuss with your neighbor: what will this program print?  Write your guesses in today's Wooclap.


```python
# plus.py

cups = input("Enter the number of cups of flour: ")
print("To double your recipe you need", cups + cups, "cups of flour")
```


### Phase 1 - Try It

Run the program on your computer.  There's something off about it, isn't there?

*   How could you fix the bug?
*   Rewrite this program to **avoid** using commas `,`
    *   Take care that the words aren't smooshed together!


Enact the changes called for above and observe how the output changes.

<details>
<summary>Hints</summary>

*   How does `+` behave differently when used with strings vs. numbers?
    *   When `+` operates on two numbers it performs *addition*
    *   When `+` operates on two strings it performs *concatenation*
    *   It is an error when `+` operates on two values of differing type
*   The `int()` function converts *strings* into *integers* (a.k.a. whole numbers, including negative numbers)
*   The `float()` function converts *strings* into *floating-point numbers* (a.k.a. real numbers)
*   The `str()` function converts *numbers* back into *strings*

</details>


### Phase 2 - Reflect On It

Summarize what you learned about `+` in today's Wooclap.


# Code Lab Challenge 1 - Drawing Happy Little Trees Interactively

Upgrade your "Happy Little Trees" program into something that more closely resembles [Assignment 1B - Faceinator](https://usu.instructure.com/courses/794745/assignments/5122782).

This version of the program will ask the user for input at various points, thus creating a custom piece of art each time it is run!  Join up with a partner and work together on this task.

Didn't finish this program last time?  That's okay, you can start from my code.

<details>
<summary><h3>Erik's Bob Rossinator</h3></summary>

```python
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
```

Download [bob-rossinator.py](./bob-rossinator.py)

</details>


### Project Requirements

0.  Ask the user for two adjectives to be part of the title of the Drawly window (á là "happy little trees")
0.  Ask the user for a color to paint the sky
    *   Show the address of the Pygame colors list (https://www.pygame.org/docs/ref/color_list.html)
    *   Draw the sky as a large rectangle that encompasses the entire canvas
0.  Ask the user for an X coordinate for the sun
    *   Hard-code the Y coordinate of the sun
0.  Ask the user for X coordinates for a high cloud and a low cloud that appear in front of the mountain peaks
    *   Draw white ellipses at each user-provided X coordinate but at hard-coded Y coordinates
    *   Draw each cloud one after the other, asking for the user's input before each
0.  Draw mountains as a complex grey polygon
    *   Ask the user for three Y coordinates for the peaks of the mountains
    *   Hard-code the X coordinates for each peak/trough
    *   Show the user the range of allowed Y coordinates (pick numbers such that the mountains don't look funny)
    *   Draw the polygon, using each Y coordinates as the mountain peaks
    *   Take care that the penultimate point ends on the same Y coordinate as the very first point,
    *   And that the final point has coordinates equal to the first point's
0.  Ask the user for a shade of blue for the foreground lake
    *   Draw a lake (two overlapping ellipses) on top of the grass
0.  Ask for a shade of green to paint trees
    *   Draw 5 happy little triangles at carefully chosen points around the lake
    *   You, the programmer decide where the trees go
0.  Sign the painting as "Bob Rossinator" in black text in the lower-right corner of the image


### Phase 0 - Preventing Bugs

Write your answers in today's Wooclap, along with your reasoning:

*   Most of these questions can be asked using the Drawly terminal, but one of them *cannot* be asked through that interface.  Which one is it?
*   Which user inputs should be `ints`, and which should be text `strings`?


### Phase 1 - Code It

Enact your proposed changes in the program.


### Phase 2 - Test It

Run the program with a variety of inputs to make sure that

*   The Drawly window title is set appropriately
*   The prompts that yield numbers work correctly


### Phase 3 - Reflect On It

Answer these debrief questions in comments in today's Wooclap:

*   Where is `(0, 0)` in Drawly: top-left or bottom-left?
*   If you increase y, does the shape move up or down?
*   What happens if a shape is drawn partly off-screen (negative x/y or too large width/height)?
*   What happens if the user types `"750"` (with quotes) or `seven hundred and fifty` when the program expects a number?


### Phase 4 - Stretch Challenges

Did you finish early?  Was this still too easy for you?  Here are some more features to implement:

0.   Make the sun size adjustable
    *   Ask for the sun radius (with a sane range).
    *   Keep the y-coordinate hard-coded.
0.  Add a second mountain layer (parallax)
    *   Draw a second, darker mountain polygon behind the first one.
    *   Ask for peak y-values for the second layer too (with different allowed ranges).
0.  Simple Input validation
    *   If the user enters a number outside your allowed range:
        *   print a warning message in the terminal
        *   replace it with a safe default (you choose the default)
    *   Your goal is that this program *never* crashes from bad numeric input
0.  Add a "frame" and a caption
    *   Draw a brown rectangle outline around the whole canvas like a picture frame.
    *   Add a caption on a golden plaque centered near the bottom: "Happy little trees, generated by YOU"
0.  Random-ish without randomness
    *   Ask the user for two different greens:
        *   one for "near trees"
        *   one for "far trees"
    *   Use the far-tree color for triangles on the mountainside and near-tree color around the lake.


