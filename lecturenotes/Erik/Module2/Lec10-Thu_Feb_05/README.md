CS1400 - Thursday, February 05 - Lecture 10 - Module 2

# Topics:
* [🟥Assn 2b - What Kind of Aggie & Superhero Decisions](#assn-2b---what-kind-of-aggie--superhero-decisions)
* [Code Lab Challenge 0 - Grading Helper](#code-lab-challenge-0---grading-helper)
* [Code Lab Challenge 1 - Blindfolded Dart Throw](#code-lab-challenge-1---blindfolded-dart-throw)
* [Code Lab Challenge 7 - Two-Decision Adventure (Design & Write)](#code-lab-challenge-7---two-decision-adventure-design--write)


------------------------------------------------------------
# Announcements

## *TODAY* DC435

*   **When**  7:00 PM Thursday, February 5th
*   **Where** Bridgerland Technical College - Room 840 (1301 N 600 W, Logan UT 84321)

@exactlyhalfofan11lblackforestham is presenting on OpenClaw Hacking!


## Student Organization for Cybersecurity - Password Cracking

*   **When**  7:00 PM Wednesday, February 11th
*   **Where** HH360

We'll be diving deep into password cracking, including more complex topics like rulesets, extracting hashes from locked files, and more.

We plan to have some hardware for people to use, but feel free to bring your own.


# Action Items

*   Erik has office hours today from 1 PM to 4 PM
    -   Find me in SER 301E or on [Zoom](https://usu-edu.zoom.us/my/erik.falor?pwd=ZE4zNXRpNVl4VVhHNkN5Q2wwV3VrUT09)


# [🟥Assn 2b - What Kind of Aggie & Superhero Decisions](https://usu.instructure.com/courses/794745/assignments/5122784)


| Task/Day           | **Thursday**       | **Friday**                                                     | **Saturday** | **Sunday**                             | **Monday**                                 |
| ------------------ | ------------------ | -------------------------------------------------------------- | ------------ | -------------------------------------- | ------------------------------------------ |
| **Classroom Time** | Classroom Lab Time |                                                                |              |                                        | 3.1: Pickups I <br/> 3.2: Logic Operations |
| **Items Due**      |                    | Exercises 2.5.2, 2.6.1, 2.6.3, 2.6.5<br/>Quizzes 2.4, 2.5, 2.6 |              | Assignment 2b<br/>Reflection Survey 2b | Code Reviews for <br/>Assn 2b begin        |


# Code Lab Challenge 0 - Grading Helper

I was in a terrible hurry when I wrote this program to help convert percentage scores to letter grades.  Now it prints the wrong output.  Can you help me fix the bug(s)?


### Starter Code

```python
score = float(input("Enter a score (0-100): "))

if score < 0.0:
	print("I think it's broken")

if score >= 73.0:
	print("You earned a C")

if score >= 83.0:
	print("You earned a B")

if score > 60.0:
	print("You earned a D")

if score >= 70.0:
	print("You earned a C-")

if score > 80.0:
	print("You earned a B-")

if score > 77.0:
	print("You earned a C+")

if score > 87.0:
	print("You earned a B+")

if score >= 93.0:
	print("You earned an A")

if score > 67.0:
	print("You earned a D+")

if score > 0.0:
	print("You earned an F")

if score >= 90.0:
	print("You earned an A-")

if score >= 100.0:
	print("Overachiever! You still earned an A")
```

I expect to see only one of the messages.  However, it prints out many messages.  In this example I want only the C- message:

```
Enter a score (0-100): 70
You earned a D
You earned a C-
You earned a D+
You earned an F
```


### Phase 0 - Identify The Bug(s)

Write answers to these questions in Wooclap:

*   How can I make the program print only one grade per score?
*   How can I make the program print the right grade for each score?


### Phase 1 - Fix It

Enact your proposed changes in the program.


### Phase 2 - Test It

Run the program with a variety of inputs to make sure that

-   every letter grade can be printed
-   every score is matched to the appropriate letter grade
-   only one letter grade is possible for each score


### Phase 3 - Reflect On It

Answer these debrief questions in Wooclap:

* Did I order my `if/elif/else` checks so they don't "short-circuit" incorrectly?
* How did I make sure every score isn't misclassified?
* Could I simplify or group ranges differently without losing accuracy?
* How could I test this program systematically to ensure that every grade category works?
* What test cases did I use in Phase 2 to ensure that the mapping from scores to grades was correct?
* What happens if the user enters a floating-point number?
* What happens if the user types non-numeric input?


### Phase 4 - Stretch Challenges

Did you finish early?  Was this still too easy for you?  Here are some more features to implement:

* If the user inputs a non-numeric score, give them a 2nd chance to entering a valid score
    *   You can test whether their input is a number with `score.isdigit()`; this returns `True` or `False`
* Ask the user for 5 scores, store them in a list, and convert them to letter grades
* Ask the user for an arbitrary number of scores, stored in a list, then convert them into letter grades
    *   Keep asking for more scores until the user enters something that fails the `.isdigit()` test


# Code Lab Challenge 1 - Blindfolded Dart Throw

In this Drawly challenge you will create a dart throwing game that exercises `if/else` logic

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 4*


### Program Requirements

0.  Create a Drawly window
    -   Set the title to "Blindfolded Dart Throw"
    -   Enable the Drawly terminal
    -   Choose dimensions so the window comfortably fits your display
    -   Make the background black (because you're wearing a blindfold at first)
0.  Welcome the user to the game in the Drawly terminal with some idle chit-chat
0.  Ask the user to enter X,Y coordinates for their dart throw with the Drawly terminal
    -   We don't know where the dart board is yet, so this will be a guess
    -   Include the valid range for the throw in the prompt
        -   For X that will be `[0..SCREEN_WIDTH]`
        -   For Y that will be `[0..SCREEN_HEIGHT]`
    -   Make sure the user's guess looks like an integer with this `if` statement: `if not dart_x.isdigit():`
        -   Give them one more chance by repeating the prompt
        -   If they fail their *second* attempt, print a message saying that it is unsafe to proceed and stop the program with this sequence of commands:
            -   ```python
                drawly.done()
                sys.exit()
                ```
            -   These commands keep the Drawly window open until the user closes it, then exits the program so nobody gets hurt.
    -   This will result in two blocks of code (one for the X coord, one for Y) each with **two layers** of nesting
0.  If the user managed to successfully input two integers, convert them with `int()` now
0.  Print the message `"Now let's take off your blindfold and see how you did"`
0.  Use `random.randint()` to pick X,Y coordinates for the center of the dart board
    -   The dart board will be 200 pixels across. Choose a range of numbers to ensure that the entire dart board is on the screen
0.  Set the drawly color to red and draw a circle of radius 200
    -   Call `drawly.draw()` so that circle appears on the screen
0.  Set the drawly color to white and draw a circle with a radius `50` pixels less than the previous one
    -   Call `drawly.draw()` so that circle appears on the screen
0.  Continue drawing circles of alternating colors and radii reduced by `50` until a bullseye of radus `50` is drawn
0.  Now draw the dart as a blue circle of radius `20`
0.  Use the distance formula to calculate the distance between the centers of the dart and bullseye
    -   $`d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}`$
0.  Print different message based on which ring the dart lands in.  Here are some suggestions:
    -   "BULLSEYE!!!  Congratulations!"
    -   "Nice!"
    -   "That's not bad"
    -   "At least you hit the board"
    -   "Ouch!  Watch where you throw that thing!" (the dart missed the board)


### Phase 0 - Design It

Write answers to these questions in Wooclap:

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

Answer these debrief questions in Wooclap:

* Did my pseudocode line up with the code I wrote, or did I change course while coding? Why?
* How did I structure my nested if/else blocks for input validation? Was there any redundancy?
* What happened in my program if the user entered invalid input twice? Did I handle it gracefully?
* How did I decide the valid ranges for the dartboard coordinates? Could they break if I change the window size?
* Where in my code did I convert the user input from string to integer? Why was that the right spot?
* How did I apply the Euclidean distance formula—was it clear and reusable?
* Did I check the ring conditions in the right order (bullseye first, outer rings later)? What would happen if the order were wrong?
* Was there any code I copy–pasted that could have been a function if I were allowed to use them here?
* How did the sequence of `if/elif/else` reflect my design? Did any branch overlap or miss an edge case?
* If I played my own game 10 times, would the output feel fair and consistent? Why or why not?


### Phase 4 - Stretch Challenges

Did you finish early?  Was this still too easy for you?  Here are some more features to implement:

*   Replace the second chance `if/else` blocks with a loop-based input validator that prevents the game from proceeding until suitable values are entered.
    -   Also bounds-check the numeric coordinates so that the dart always lands on the screen
*   Create a full game loop that repeats the game until the user quits
    -   Blank out the screen every time the game starts over (in other words, put the blindfold back on the player's face)
    -   Mark the location of every previous dart throw as a grey circle drawn on the screen before the dart board appears
*   Implement a scoring system
    -   Bullseye is worth 100 points
    -   1st ring is worth 50 points
    -   2nd ring is worth 25 points
    -   3rd ring is worth 0 points
    -   Missing the board costs 50 points
    -   Draw the score on the lower right corner of the screen
*   Create a high-score table
    -   Record the top 3 high scores in a file
    -   Print the high-score table at the start of the program
    -   The game ends when the player closes the Drawly window; before the program exits check whether player earned a spot on the table
    -   Using the regular terminal, ask the player for their name
    -   Update the high-score file on disk
*   Do your players think this game is too easy? Make it unwinnable by placing the bullseye such that the dart **never** hits the board
    -   Turn the frustration up to 11 by strategically placing the dart board 1 pixel away from the dart so that the user is *so* close, but not quite there


# Code Lab Challenge 7 - Two-Decision Adventure (Design & Write)

In this challenge you will design and write a short choose-your-own-adventure program from scratch. The user will make two choices, and your program will respond with one of four different endings.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 4*


### Program Requirements

0.  Your program must ask the user exactly two questions using `input()`.
0.  Your program must use `if`, `elif`, and `else` to select between mutually-exclusive paths.
0.  Your program must print exactly one ending message per run (one outcome, not multiple).
0.  Your program must handle unexpected input for at least the first question (with a fallback ending).


#### Gameplay demo

```
You wake up late for your CS class.
Do you [check] Canvas or go back to [sleep]?  > check

You see an announcement about a surprise quiz.
Do you [study] quickly or [hope] for the best?  > study

You cram the key ideas and just barely pass the quiz.
CONGRATULATIONS!

THE END
```


```
You wake up late for your CS class.
Do you [check] Canvas or go back to [sleep]?  > sleep

You miss an important announcement and arrive late and unprepared.
Do you [grovel] to the teacher for a second chance, or [commit] to do better next time?  > grovel

Your teacher is unmoved by your plea and tells you that they know you are better than this.
That cuts deep, but you know it is true.

THE END
```


### Phase 0 - Design It

Answer each of these questions in today's Wooclap:


0.  What is the user experience?
    -   What is the opening scene you will print?
    -   What are the two choices the user can make for Question 1?
    -   What are the two choices the user can make for Question 2 (in each branch)?
    -   What are your four possible endings (one per combination of choices)?
1.  How do I get the necessary data?
    -   What exact prompt strings will you use for Question 1 and Question 2?
    -   What exact input values will you accept (example: `"left"` and `"right"`)?
2.  What do I need to process and calculate?
    -   What comparisons will you make to decide which branch to execute?
    -   What do you consider "invalid input"?
3.  How am I going to process and calculate?
    -   Sketch your `if / elif / else` structure for the first question.
    -   Inside each first-branch, sketch the `if / else` (or `if / elif / else`) for the second question.
    -   Where will your fallback ending go so that the program always prints something?
4.  What do I need to display as results?
    -   What exactly will you print for each of the four endings?
    -   What exactly will you print for invalid input?


### Phase 1 - Pseudocode It

Using the answers to the above questions as your guide, write *pseudocode* as a block of comments in your program.  Start by describing the flow of the program in plain English.  Refine your pseudocode until it is as specific as Python code.

Minimum expectation for pseudocode:

-   A comment for the opening scene
-   A comment for asking Question 1
-   A comment describing the first `if / elif / else` decision
-   A comment for asking Question 2 in each branch
-   A comment describing the second decision in each branch
-   A comment for printing the ending


### Phase 2 - Build It

When your pseudocode is basically line-for-line equivalent to real Python code, rewrite each comment as code.

Testing checklist (run your program multiple times):
-   Try the two valid answers for Question 1 and confirm you reach different branches.
-   In each branch, try the two valid answers for Question 2 and confirm you get different endings.
-   Enter an invalid answer for Question 1 and confirm your fallback ending prints.
-   Confirm you never see two endings in a single run.


### Phase 3 - Reflect On It

Answer these debrief questions in comments in today's Wooclap:

* Did my pseudocode line up with the code I wrote, or did I change course while coding? Why?
* Which decision (Question 1 or Question 2) was harder to reason about, and why?
* What invalid input did I test, and what did my program do in response?
* If I accidentally used a second `if` instead of `elif`, what could go wrong?
* What is one small change I could make to improve readability (better variable names, clearer prompts, simpler conditions)?


### Phase 4 - Stretch Challenges

Did you finish early?  Was this still too easy for you?  Here are some more features to implement:

0.  Normalize user input so that `Left`, `LEFT`, and `left` (or similar variations) are treated the same.
0.  Add a second layer of validation: if Question 2 is invalid, print a branch-specific fallback ending (still only one ending per run).
0.  Refactor your conditionals so you never compare the same variable to the same string more than once.
0.  Keep the logic identical, but completely rewrite the story theme (space, fantasy, campus, survival, detective, etc.) without changing the number of questions.


