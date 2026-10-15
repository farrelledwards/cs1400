CS1400 - Tuesday, February 10 - Lecture 11 - Module 3

# Topics:
* [🟥Assn 3a - Fronkian & Doofenlittle](#assn-3a---fronkian--doofenlittle)
* [Code Lab Challenge 0 - Untangling Scope Dependencies](#code-lab-challenge-0---untangling-scope-dependencies)
* [Code Lab Challenge 1 - Lucky Number Detector](#code-lab-challenge-1---lucky-number-detector)
* [Code Lab Challenge 2 - Regular Polygon Painter](#code-lab-challenge-2---regular-polygon-painter)


------------------------------------------------------------
# Announcements

## *TONIGHT* FSLC - Homelabbing

*   **When**    6:30 PM Tuesday, February 10th
*   **Where**   WIDT 007
*   **Website** https://linux.usu.edu
*   **Discord** https://discord.gg/PvgG6N2hsU

Ever wanted to host your own alternative to google drive and/or photos? How about your own git forge, like GitHub? What about your own streaming service to let you access your movies and music on the go? Come learn about homelabbing - Nextcloud, Gitea, Jellyfin, etc., and replace your online services with ones you control. We'll talk about hosting services in Docker, wrangling Docker compose files, and Coolify, a web UI that makes the whole process stupid simple.


## *TOMORROW* Student Organization for Cybersecurity - Password Cracking

*   **When**  7:00 PM Wednesday, February 11th
*   **Where** HH360

We'll be diving deep into password cracking, including more complex topics like rulesets, extracting hashes from locked files, and more.

We plan to have some hardware for people to use, but feel free to bring your own.


# Action Items

## Join today's Wooclap before 11:45 AM

https://app.wooclap.com/BXBSFM


##  Canvas lesson to study before our next code lab on Thursday, Feb 12

*   3.3: Data in Objects


# [🟥Assn 3a - Fronkian & Doofenlittle](https://usu.instructure.com/courses/794745/assignments/5122785)

*   This assignment has two tasks
*   Read the instructions *carefully*, but also look at the **rubric**
    *   Use the rubric as a checklist so you don't miss important requirements
*   This assignment is due **at 11:59 PM on Sunday, February 15th**


## Task 1 - Fronkian Calendar

Write a program that takes a year and determines if it's a Leap Year in the lesser-known Fronkian Calendar.

*   This is a *console* program (i.e. text-only interface) 
    *   You **do not** need to `import drawly`; instead, use `print()` and `input()`
*   Put your code in a file called `task1.py` and your software development plan as `design1.md`
*   Test your program with a variety of inputs and double check its accuracy by hand or with a calculator (the assignment page on Canvas contains some test cases for you to try)
*   You will use knowledge from these sections of Unit 3
    *   **3.1: Pickups I**
    *   **3.2: Logic Operations**
        

## Task 2 - Dr. Doofenlittle

*   This is a *console* program (i.e. text-only interface) 
*   Put your code in a file called `task2.py` and your software development plan as `design2.md`
*   You will use knowledge from this section of Unit 3
    *   **3.3: Data in Objects**
        


| Task/Day           | **Tuesday**        | **Wednesday**        | **Thursday**       | **Friday**                                                                       | **Saturday** | **Sunday**                             | **Monday**                       | **Tuesday**                         |
| ------------------ | ------------------ | -------------------- | ------------------ | -------------------------------------------------------------------------------- | ------------ | -------------------------------------- | -------------------------------- | ----------------------------------- |
| **Classroom Time** | Classroom Lab Time | 3.3: Data in Objects | Classroom Lab Time |                                                                                  |              |                                        | 3.4: While Loops                 |                                     |
| **Items Due**      |                    |                      |                    | Exercises 3.1.1, 3.1.3, 3.1.5, 3.1.6, 3.2.1-a, 3.2.1-b<br/>Quizzes 3.1, 3.2, 3.3 |              | Assignment 3a<br/>Reflection Survey 3a | Campus closed for Presidents Day | Code Reviews for <br/>Assn 3a begin |



# Code Lab Challenge 0 - Untangling Scope Dependencies

In this code lab challenge you are tasked with solving a puzzle in code.  Untangle a scrambled calculation that converts **Unix epoch time** into an approximate calendar breakdown using many intermediate variables. The goal is to reveal scope and dependency errors by fixing line order and minimal logic issues.

**What is _Unix_?**  Unix is an influential operating system first built at Bell Labs in the late 1960s. Think of it as the quiet OS behind the scenes. Its design philosophy inspired most modern operating systems: macOS is Unix-based, Linux and Android are Unix-like, and the best parts of Windows were copied from Unix. Most servers and cloud machines run something Unix-y.

**What is the _Unix epoch_?**: This is the "zero" time that marks the beginning of the calendar for Unix-based systems: *00:00:00 UTC, January 1, 1970*. Time, to a computer, is measured in “seconds since the epoch,” which makes dates easy to compare and compute.


For instance, the epoch time that I wrote this lecture was `1770604924`, or 1,770,604,924 seconds after New Year's 1970.

By using division and remainder operations, you can figure out when that was, in human terms.  That is what this program can do, once you fix it! 

*   To be clear, the **only** problem with this program is that the lines of source code are scrambled
*   The shape of the starter code is correct (hint, hint!)
    *   By this I mean that the pattern of blank and non-blank lines in the starter code follows the outline of the correct program



### Starter Code

```python
rem = total_seconds % SECONDS_PER_YEAR


minutes = rem // SECONDS_PER_MINUTE
seconds = rem % SECONDS_PER_MINUTE
days = rem // SECONDS_PER_DAY
total_seconds = int(time.time())

print(f"Year {year_estimate}, {days}d {hours:02d}:{minutes:02d}:{seconds:02d}")

SECONDS_PER_YEAR = 365 * SECONDS_PER_DAY
import time
SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE

rem = rem % SECONDS_PER_HOUR
SECONDS_PER_DAY = 24 * SECONDS_PER_HOUR

years = total_seconds // SECONDS_PER_YEAR
hours = rem // SECONDS_PER_HOUR

SECONDS_PER_MINUTE = 60
rem = rem % SECONDS_PER_DAY

year_estimate = 1970 + years
```


### Phase 0 - Identify The Bug(s)

Before changing the source code, write answers to these questions in Wooclap:

- Which names are used before definition? List each occurrence.
- Which computations require a previous value of `rem`? In what order must the `%` steps occur?
- Which constants depend on other constants? In what order must constants be defined?
- Where must `import time` appear relative to `time.time()`?
- Are `//` and `%` used on the correct value of `rem` at each stage (year, day, hour, minute, second)?
- Do we need any conversions to integer besides `int(time.time())`?
- Which lines of code could be simplified with augmented assignment operators (e.g. `+=`, `//=`, or `%=`)?


### Phase 1 - Fix It

Reorder the lines of code so that:

- The time module is imported before `time.time()` is called
- All CONSTANTS are defined before use
- First compute years, then days, hours, minutes, and finally seconds
- The variable `rem` carries the remainder to the next stage of the calculation
- Keep the 365-day-year assumption and the final print format


### Phase 2 - Test It

Temporarily replace `total_seconds = int(time.time())` with fixed values and verify exact outputs:

- `total_seconds = 0` → Year 1970, 0d 00:00:00
- `total_seconds = 59` → Year 1970, 0d 00:00:59
- `total_seconds = 60` → Year 1970, 0d 00:01:00
- `total_seconds = 3600` → Year 1970, 0d 01:00:00
- `total_seconds = 86400` → Year 1970, 1d 00:00:00
- `total_seconds = 365*86400` → Year 1971, 0d 00:00:00
- `total_seconds = 365*86400 + 1*86400 + 1*3600 + 1*60 + 1` → Year 1971, 1d 01:01:01

Now, restore `time.time()` and confirm the program prints a timestamp that's toward the end of the current year (we are nearly 300 days into this year).

- Because this code does not take leap years into account it will be a few days off.
- The hours may be off by ±6 depending on your computer's timezone setting.


### Phase 3 - Reflect On It

Answer these debrief questions in Wooclap:

* Which lines depended on which earlier values? Give two concrete dependency chains.
* How did you ensure rem always represented the remaining seconds for the next unit?
* What ordering rule will you apply next time to avoid “use before definition” bugs?
* Why are named constants preferable to magic numbers here, and how did that influence order?
* According the Unix epoch time given above, when did Erik draft this lecture (± seven hours)?


# Code Lab Challenge 1 - Lucky Number Detector

I have a theory about which numbers are lucky, and an algorithm to prove it.  But my program is long, repetitive, and complex.  The set of deeply nested `if` statements is hard to read and makes my head spin every time I look at it.


### Phase 0 - Understand the Starter Code

```python
print("Welcome to the Lucky Number Detector")
print("Tell me your number, and I'll tell you whether it is lucky")
number = int(input("\nEnter an integer: "))

if number == 42:  # this number has significance to nerds
    print("Congratulations! That is today's lucky number!")
elif number % 2 == 0: # even
    if number < 0:    # even and negative
        if number % 3 == 0:    # divisible by 3
            print("Sorry, your number is not lucky today :(")
        elif number % 5 == 0:  # divisible by 5
            print("Sorry, your number is not lucky today :(")
        else:
            print("Congratulations! That is today's lucky number!")
    else:
        print("Sorry, your number is not lucky today :(")
elif number % 2 == 1: # odd
    if number > 0:    # odd and positive
        if number % 3 == 0:    # divisible by 3
            print("Sorry, your number is not lucky today :(")
        elif number % 5 == 0:  # divisible by 5
            print("Sorry, your number is not lucky today :(")
        else:
            print("Congratulations! That is today's lucky number!")
    else:
        print("Sorry, your number is not lucky today :(")
else:
    print("Sorry, your number is not lucky today :(")
```

The program works perfectly.  Here is a table of some of its results:

| **Number** | **Is Lucky?** |
|:----------:|:-------------:|
| 0          | No            |
| 1          | Yes           |
| -1         | No            |
| 2          | No            |
| -2         | Yes           |
| 3          | No            |
| -3         | No            |
| 4          | No            |
| -4         | Yes           |
| 11         | Yes           |
| -11        | No            |
| 13         | Yes (contrary to popular belief) |
| -13        | No            |
| 14         | No            |
| -14        | Yes           |
| 42         | Yes (by special request) |
| 1337       | Yes           |
| -1337      | No            |

These all align with my theory, so I am confident there is no bug in this program.  **You should try it for yourself.**


### Phase 1 - Design One Boolean Expression To Rule Them All

However, I really do not like that crazy `if` statement.  It is long and hard to follow, plus many of the messages are duplicated, There must be a way to collapse all of those `if/elif/else` statements down into a single `if/else` by making use of the logical operators `and`, `or`, and `not`.

In pseudocode, design a single compound condition that replicates the logic of the multi-branched `if/elif/else` statement.


### Phase 2 - Fix It

Add your proposed `if/else` statement to the bottom of the program.  Your addition will have this form:

```python
if ( ... big compound condition ... ):
    print("Congratulations! That is today's lucky number!")
else:
    print("Sorry, your number is not lucky today :(")
```

*   The new `if` statement **must have exactly two branches** and be **four lines long**
*   Keep the original algorithm intact to compare your new formula's output with the original


### Phase 3 - Test It

*   Re-run all of the inputs from the table to make sure that both algorithms yield the same results
*   Think of other numbers to test


### Phase 4 - Reflect On It

Answer these debrief questions in Wooclap:

* How many tries did it take you to get the formula right?  What did each attempt teach you?
* Which version of the program do you think is better?  Why do you prefer it?
* Which logical operators (`and`, `or`, `not`) did you use in your final condition? Why were they necessary?
* Did you group sub-conditions with parentheses? How did parentheses affect the meaning of your expression?
* Was there any part of the condition that was especially tricky to reason about? How did you simplify it?
* How does collapsing many `if/elif` branches into one Boolean expression affect readability and maintainability?
* If the "lucky number" rules changed (for example, divisible by 7 instead of 5), which version of the program would be easier to update - the long `if/elif` tree or the single `if`? Why?


# Code Lab Challenge 2 - Regular Polygon Painter

*Note: This is a stretch task for students with deeper programming experience*

Your challenge today is to build a Drawly app that collects user-defined **regular polygons**, stores them as `Shape` objects, and then draws them. Each `Shape` knows how to draw itself from a given starting $`(x,y)`$ coordinate using polygon geometry.

### Program Requirements

* Define a `Shape` class with attributes: `sides:int`, `color:str`, `size:str` and a method `draw(self, x, y)` that renders the polygon using Drawly.
* Map size to side length:
  - **big → 100 px**
  - **medium → 66 px**
  - **small → 33 px**
* Prompt repeatedly: `size`, `color`, number of `sides`.
  - Create a `Shape` object and append to `shapes: list[Shape]`
  - Ask if the user wants another; stop when they decline
* Validate input:
  - $`n \ge 3`$
  - `size ∈ {big, medium, small}`
  - `color` is any Drawly-accepted color string
* After input ends:
  - Open a Drawly window and draw all shapes
  - Call `shape.draw(x, y)` for each, choosing reasonable ($`x,y`$) positions (row or grid)
* In `Shape.draw()`, build the polygon using `drawly.polygon_begin()`,  `drawly.add_poly_point(...)`, and  `drawly.polygon_end()`
* Use one of these formulas:
  * **Turn/step method (first vertex at $`(x_0,y_0)`$)**
    - Interior angle: $`\alpha=\frac{(n-2)\pi}{n}`$
    - Exterior turn (step): $`\theta=\frac{2\pi}{n}`$
    - With side length $`s`$ and initial heading $`\phi_0`$ (e.g., $`0`$), vertices:
    - $`
      P_0=(x_0,y_0),\quad
      P_{k+1}=P_k + s\big(\cos(\phi_0+k\theta),,\sin(\phi_0+k\theta)\big)
      `$
      - *(If your screen $`y`$ increases downward, use $`-\sin`$ for the $`y`$ increment.)*
  * **Center-radius method (center at $`(c_x,c_y))`$**
    - $`R=\dfrac{s}{2\sin(\pi/n)}`$, then
    - $`
      V_k=\big(c_x+R\cos(\phi_0+\tfrac{2\pi k}{n}),;c_y+R\sin(\phi_0+\tfrac{2\pi k}{n})\big)
      `$
* Keep code tidy: constants for canvas size and spacing, input normalization, simple placement (row or grid).


### Phase 0 - Design It

Answer these questions in Wooclap:

0. What is the user experience?
1. How do I get the necessary data?
2. What do I need to process and calculate?
3. How am I going to process and calculate?
4. What do I need to display as results?


### Phase 1 - Pseudocode It

Write pseudocode in a file called `design.md`. Refine it until it is nearly line-for-line code.


### Phase 2 - Build It

When your pseudocode is code-like, copy it into a Python script and translate it into working code.


### Phase 3 - Reflect On It

Answer in Wooclap:

* Which drawing approach did you choose (step vs. center-radius)? Why?
* How did you pick $`\phi_0`$ (initial rotation)? What rotation looks best?
* How did you place multiple shapes so they don’t overlap?
* What input validations did you implement and why?
* Where did you use constants instead of magic numbers?


### Phase 4 - Stretch Challenges

Did you finish early? Here are more features:

* **Rotation control:** Let the user supply a rotation angle $`\phi_0`$ in degrees.
* **Fill and stroke:** Add outline thickness and optional fill toggle; support both `set_color` and fill color.
* **Grid layout:** Auto-wrap shapes into rows; spacing depends on side length $`s`$ and $`n`$ (use $`R=\dfrac{s}{2\sin(\pi/n)}`$).
* **Rainbow series:** If color is `rainbow`, assign a different color to each vertex or to each shape.
* **Labeling:** Draw the number of sides at the centroid; compute centroid as the average of vertex coordinates.
* **Star polygons:** Support a step $`m`$ (e.g., $`n=5, m=2`$) and connect $`P_k`$ to $`P_{(k+m)\bmod n}`$.
* **Input shortcuts:** Allow `done` at any prompt to exit input cleanly and begin drawing.
* **Export/Import:** Save the `shapes` list to a simple text format and reload it later.


