CS1400 - Tuesday, February 17 - Lecture 13 - Module 3

# Topics:
* [🟥Assn 3b - Don't Play With Mathes](#assn-3b---dont-play-with-mathes)
* [Code Lab Challenge 0 - Broken Loop Lab](#code-lab-challenge-0---broken-loop-lab)
* [Code Lab Challenge 1 - Countdown to Blast Off](#code-lab-challenge-1---countdown-to-blast-off)
* [Code Lab Challenge 2 - Crash-Proof Guessing Game](#code-lab-challenge-2---crash-proof-guessing-game)


------------------------------------------------------------
# Announcements

## *TONIGHT* FSLC - Get Nix'ed Up With NixOS

*   **When**    6:30 PM Tuesday, Feb 17th
*   **Where**   WIDT 007
*   **Website** https://linux.usu.edu/event/a74c51b4-f66a-40a4-8230-5ca49da8bb42
*   **Discord** https://discord.gg/PvgG6N2hsU

What happens when you cross theoretically awesome functional programming with your entire computer? Let's just say you might get a bit Nix'ed up. In this meeting we dive into what it means to have a truly reproducible system and leverage the power of lazy pure evaluation. We're diving head first into the Nix programming language, Nix the package manager, and NixOS itself.


## *TOMORROW* Student Organization for Cybersecurity - Homelabbing

- **When** 7 PM Wednesday, February 18th
- **Where** HH 360
- **Discord** https://discord.gg/JEVdRdfpEb

Come learn to get started with homelabbing and self-hosting! Learn about networking, Docker, and other key topics to create your own homelab. Want to have your own personal Netflix, Google Drive, iCloud, etc (not to mention save some money on subscription fees)? We'll teach you! It's easier than you think...


# Action Items

## Exam #1 is next week

*   This is the first of two exams. It covers material from **Units 1-3**.
*   The exam opens at 12 AM on **Monday, February 23** and closes at 11:59 PM on **Friday, February 27**
    -   You have **80 minutes** to complete the exam.
    -   You are not allowed any outside resources such as notes, books, websites, etc.
*   This exam is proctored by Proctorio, and is taken on your own computer.
    -   Ensure that you have a quiet space where you will be uninterrupted.
    -   Make sure to turn your phone off as well as other things that have pop up notifications (computer/watch/roommates/etc).
    -   Run through [Computer Setup (Remotely Proctored)](https://usu.instructure.com/courses/794745/quizzes/1417470) on Canvas to debug any issues with Proctorio.
*   We will do an exam review as part of our in-class code lab on **Tuesday, February 24**
    -   You are welcome to take the exam before Tuesday morning, or you can wait until after we do the in-class review


# [🟥Assn 3b - Don't Play With Mathes](https://usu.instructure.com/courses/794745/assignments/5122786)

*   This assignment has one task
*   Read the instructions *carefully*, but also look at the **rubric**
    *   Use the rubric as a checklist so you don't miss important requirements
*   This assignment is due **at 11:59 PM on Sunday, February 22nd**


## Task 1 - Don't Play With Mathes

The title of this task is correct. You are going to write a program that literally (in a figurative sense) catches on fire when you get enough math problems correct. It's a simple concept, but will require to think quite a bit about how to get everything to work correctly with your new knowledge of loops.

*   This is a *Drawly* program that also uses the *console* to take input from the user.
*   Put your code in a file called `task1.py` and your software development plan as `design1.md`
*   You will use knowledge from these sections of Unit 3
    *   **3.4: While Loops**
    *   **3.5: For Loops**
    *   **3.6: Project Demo**


| Task/Day           | **Tuesday**        | **Wednesday**                          | **Thursday**       | **Friday**                                                             | **Saturday** | **Sunday**                             | **Monday**                          |
| ------------------ | ------------------ | -------------------------------------- | ------------------ | ---------------------------------------------------------------------- | ------------ | -------------------------------------- | ----------------------------------- |
| **Classroom Time** | Classroom Lab Time | 3.5: For Loops <br/> 3.6: Project Demo | Classroom Lab Time |                                                                        |              |                                        | 4.1: Function Introduction          |
| **Items Due**      |                    |                                        |                    | Exercises 3.4.1, 3.5.2-a, 3.5.2-b, 3.5.2-c, 3.5.3<br/>Quizzes 3.4, 3.5 |              | Assignment 3b<br/>Reflection Survey 3b | Code Reviews for <br/>Assn 3b begin |


# Code Lab Challenge 0 - Broken Loop Lab

In this challenge you will diagnose and repair broken `while` loops.

Each example below contains a logic error. Some loops run forever. Some never run at all. Some produce incorrect results. Others crash when the user gives invalid input. Your job is to analyze each one, determine what is wrong, and fix it.  In some cases you will need to add another loop within the main loop.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 4*

### Program Requirements

0.  Each broken loop must be repaired so that it behaves correctly
0.  Infinite loops must be fixed without removing the loop entirely
0.  Off‑by‑one errors must be corrected
0.  Nested loops must correctly count their total number of iterations
0.  Your corrected code must not crash, even when the user gives invalid input
0.  Your corrected code must not contain an infinite loop


### Phase 0 - Design It

Answer each of these questions in today's Wooclap:

0.  What makes a `while` loop stop running?
0.  What causes an infinite loop?
0.  What is an off‑by‑one error?
0.  In a nested loop, which variable controls the inner loop?
0.  How can you count how many total iterations a loop performs?
0.  What must change inside every `while` loop?


### Phase 1 - Pseudocode It

For each broken example below:

Using the answers to the above questions as your guide, write *pseudocode* as a block of comments explaining:

-   What the loop is trying to do.
-   What is wrong with it.
-   How you will fix it.

Refine your pseudocode until it is as specific as Python code.


### Broken Loop 1

```python
count = 0

while count < 5:
    print("Count =", count)
```


### Broken Loop 2

```python
num = 10

while num > 0:
    print(num)
    num + 1
```


### Broken Loop 3

```python
total = 0

while total <= 100:
    number = int(input("Enter a number: "))
    number = total + number

print("Final total:", total)
```


### Broken Loop 4

```python
x = 1

print("Watch me count to 10!")
while x < 10:
    print(x)
    x = x + 1
```


### Broken Loop 5

```python
outer = 0
iterations = 0

while outer < 3:
    inner = 0

    while inner < 4:
        print("Outer:", outer, "Inner:", inner)
        inner = inner + 1

    outer = outer + 1
    iterations = outer

print("there were", iterations, "iterations in total (should equal 12)")
```


### Broken Loop 6

```python
valid = False

while not valid:
    print("Still not valid...")
```


### Broken Loop 7

```python
count = 10

print("Countdown to lift-off!")

while count = 0:
    print("T-minus", count, "seconds")
    count = count - 1
```



### Broken Loop 8

```python
n = 1

while n <= 10:
    print(n)
    n = n - 1
```


### Broken Loop 9

```python
outer = 0
inner = 0
total = 0

while outer < 10:
    while inner < 5:
        print("Outer:", outer, "Inner:", inner)
        inner = inner + 1
        total = inner
    outer = outer + 1

print("there were", total, "iterations in total (should equal 50)")
```



### Broken Loop 10

```python
outer = 0

while outer < 10:
    inner = 0
    total = 0
    while inner < 5:
        print("Outer:", outer, "Inner:", inner)
        total = total + 1
        inner = inner + 1
    outer = outer + 1

print("there were", total, "iterations in total (should equal 50)")
```



### Phase 2 - Build It

When your pseudocode is basically line-for-line equivalent to real Python code, rewrite each comment as actual Python.

You must:

-   Fix the loop so it terminates correctly
-   Ensure the loop produces the intended output
-   Correct off‑by‑one errors where present
-   In the nested loop example:
    -   Accurately count the total number of iterations of the **inner loop**
    -   Print the correct total at the end


### Phase 3 - Test It

For each repaired loop:

0.  Does it terminate correctly?
1.  Does it run the expected number of times?
2.  Does it avoid crashing?
3.  Does it avoid infinite looping?
4.  For nested loops:
    -   How many total iterations should occur?
    -   Does your program print that correct number?


### Phase 4 - Stretch Challenges

0.  Modify one example so that it intentionally creates an infinite loop. Then fix it again
0.  Create your own nested loop that runs 5 × 6 times. Verify the total iteration count
0.  Rewrite one repaired loop using a different loop condition that produces the same result
0.  Explain in plain English why each original loop was broken
0.  In **Broken Loop 5** ask the user how many outer & inner iterations to run; validate their input


# Code Lab Challenge 1 - Countdown to Blast Off

In this challenge you will add a countdown sequence to a Drawly rocket launch program.


*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 4*

### Program Requirements

The rocket and blast effects are already drawn for you.  Your job is to:

0.  Ask the user for a countdown starting value using the Drawly terminal
    *   The starting value must be a **positive integer greater than 0**
    *   Invalid input (non-integer, negative number, or 0) must be rejected
    *   Keep asking the user for a countdown until they provide valid input
0.  Use a `while` loop to control the countdown
    *   Print countdown numbers one per line in the Drawly terminal
    *   The loop exits when the countdown reaches 0
0.  Ensure that the program does not crash, nor contains an infinite loop


### Starter Code

Copy this into a new file called `countdown.py`.

```python
import drawly


drawly.start(title="Rocket Launch", background="skyblue", dimensions=(1280, 500), terminal=True)

# Draw rocket body
drawly.set_color("white")
drawly.rectangle(600, 150, 80, 200)

# Draw rocket nose
drawly.set_color("red")
drawly.polygon_begin()
drawly.add_poly_point(600, 150)
drawly.add_poly_point(680, 150)
drawly.add_poly_point(640, 90)
drawly.polygon_end()

# Draw fins
drawly.set_color("red")
drawly.polygon_begin()
drawly.add_poly_point(600, 300)
drawly.add_poly_point(560, 350)
drawly.add_poly_point(600, 350)
drawly.polygon_end()

drawly.polygon_begin()
drawly.add_poly_point(680, 300)
drawly.add_poly_point(720, 350)
drawly.add_poly_point(680, 350)
drawly.polygon_end()

drawly.draw()


# Add the countdown loop here

# call drawly.draw() after you print the current countdown number in
#   the drawly terminal

# Your code ends here


# Draw flames
drawly.set_color("orange")
drawly.polygon_begin()
drawly.add_poly_point(620, 350)
drawly.add_poly_point(660, 350)
drawly.add_poly_point(640, 420)
drawly.polygon_end()

drawly.set_color("yellow")
drawly.polygon_begin()
drawly.add_poly_point(630, 350)
drawly.add_poly_point(650, 350)
drawly.add_poly_point(640, 400)
drawly.polygon_end()

# Draw smoke
drawly.set_color("lightgray")
drawly.circle(610, 420, 30)
drawly.circle(670, 420, 30)
drawly.circle(640, 450, 40)

# Draw text
drawly.set_color("black")
drawly.text(500, 10, "BLAST OFF!", size=60)

drawly.draw()

drawly.done()
```


### Phase 0 - Design It

Answer each of these questions in today's Wooclap:

0.  What is the user experience from start to finish?
1.  How do you get the necessary data from the user?
2.  What needs to be validated before the countdown begins?
3.  What variable will control the countdown loop?
4.  How will the loop stop?
5.  When should `blast_off()` be called?
6.  What could cause an infinite loop in this program?


### Phase 1 - Pseudocode It

Using the answers to the above questions as your guide, write *pseudocode* as a block of comments in your program.

Start by describing the flow of the program in plain English.

Refine your pseudocode until it is as specific as Python code.


### Phase 2 - Build It

When your pseudocode is basically line-for-line equivalent to real Python code, rewrite each comment as actual Python.

Be sure to:

-   Use `drawly.terminal_input()` to get user input
-   Validate the user's input
-   Convert valid input to an integer
-   Use a `while` loop to count down to zero
-   Use `drawly.terminal_output()` to print each number
-   Stop the loop when `0` is printed
    -   Don't stop the loop before `0` is reached
    -   Don't go into negative numbers


### Phase 3 - Test It

Test your program with each of the following:

0.  Letters (abc)
1.  Empty input
2.  Negative numbers
3.  Zero
4.  A small valid number (5)
5.  A larger valid number (10)

Does your program:

0.  Reject invalid input clearly?
1.  Avoid crashing?
2.  Count down correctly?
3.  Stop exactly at zero?
4.  Trigger `blast_off()` only once?
5.  Avoid infinite loops?

Explain the results of your tests in today's Wooclap.


### Phase 4 - Stretch Challenges

0.  Add a nested loop that asks the user if they want to launch again
0.  Track how many launches have occurred in this session
0.  Add a maximum allowed countdown value and reject numbers that are too large
0.  Add stars to the sky using a loop and random coordinates
0.  Print a dramatic launch checklist before the countdown begins


# Code Lab Challenge 2 - Crash-Proof Guessing Game

In this challenge you will repair and upgrade a number guessing game so that it behaves like a well-written program instead of a fragile demo.


### Starter Code

```python
from random import randint


number = randint(1, 100) # number to guess

print("Guess a number from 1 to 100")

guess = -1  # not a valid match

while guess != number:

    guess = int(input("\tWhat is your guess (between 1 and 100)? "))

    if guess == number:
        print("You got it!")
    elif guess < number:
        print("You're too low")
    else:
        print("You're too high")

print("Thanks for playing")
```

### Phase 0 - Identify The Bug(s)

Answer each of these questions in today's Wooclap:

*   What specific user input(s) will crash this program? Give at least 3 examples.
*   What input(s) should be rejected even though they are integers?
*   What should the program do when the user enters invalid input (non-integer or out of range)?
*   Where should a guess counter be updated so it counts only valid guesses?
    -   Valid guesses are integers between 1-100
*   What does `guess = -1` accomplish before the loop begins?



### Phase 1 - Fix It

The original program will crash when the user types a non-numeric string. This happens because the output of `input()` is passed directly to `int()` without first checking whether it looks like a number. With a `while` loop you can keep asking the user to enter a number until they get it right.

You can do this by separating the steps taken by the line of code that uses `int()` and `input()` into multiple lines of code, and adding another `while` loop inside the `while guess != number` loop, like this:

0.  Initialize a new variable called `user_input` to the empty string `""`
0.  Then write a `while` loop that uses the test `not user_input.isdigit()`
    -   `.isdigit()` is a method on strings which returns `True` when *every* character in the string is a digit `0-9`
    -   It returns `False` if the string is empty or contains any non-digit characters
0.  As long as `user_input` does not pass the `.isdigit()` test, the user will be asked to


### Phase 2 - Test It

Run the program with a variety of inputs to make sure that

*   It never crashes, even with inputs like: empty string, words, floating-point numbers, negative numbers, punctuation, whitespace
*   It still provides correct "too low / too high / got it" feedback for valid guesses


### Phase 3 - Reflect On It

Answer these debrief questions in comments in today's Wooclap:

*   What would break if you removed the `guess = -1` initialization?
*   Explain (in plain English) how your input-validation loop works. What makes it stop?
*   What would happen if you forgot to change the value of `guess` inside the loop?
*   If you added a "play again" feature, what would the outer loop's condition be?


### Phase 4 - Stretch Challenges

Did you finish early?  Was this still too easy for you?  Here are some more features to implement:

0.  Count the number of **valid** guesses the user makes
    *   Do **not** count invalid inputs (read: non-numeric inputs) toward the total
0.  After the user wins, print performance feedback:
    *   1-3 guesses -> `Psychic.`
    *   4-7 guesses -> `Not bad.`
    *   8+ guesses -> `Brute force approach detected.`
0.  **Play Again Mode**
    -   After winning, ask the user if they want to play again.
    -   If they type "yes", start a new game.
    -   This requires a nested while loop.
0.  **Difficulty Levels**
    -   Let the user choose:
        -   Easy (1-10)
        -   Medium (1-50)
        -   Hard (1-500)
    -   Adjust the random number range accordingly.
0.  **Hint System**
    -   After 5 incorrect guesses, tell the player whether the number is even or odd.
0.  **Limited Attempts Mode**
    -   End the game after 10 guesses.
    -   Reveal the number if the user loses.
0.  **Statistics Tracker**
    -   If using Play Again mode, track:
        -   Total games played
        -   Average guesses per game


