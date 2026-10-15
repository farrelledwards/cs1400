CS1400 - Thursday, February 26 - Lecture 16 - Module 4

# Topics:
* [🟥Assn 4a - Design Number Pyramid](#assn-4a---design-number-pyramid)
* [Code Park Tycoon](#code-park-tycoon)
* [Code Lab Challenge 0 - Taking Home The Gold](#code-lab-challenge-0---taking-home-the-gold)
* [Code Lab Challenge 1 - Function Arguments](#code-lab-challenge-1---function-arguments)


------------------------------------------------------------
# Announcements

## *THIS WEEKEND* HackUSU 2026

HackUSU is Utah's largest collegiate 24-hour innovation challenge and hackathon. Participants create innovative applications while networking with industry professionals and attending educational workshops.

*   **When**  February 27th-28th, 2026.
*   **Where** Huntsman Hall
*   [**Registration**](https://huntsman.usu.edu/hackusu/) is open to all college students and high school seniors.
    *   Register with the code `USU26` to save $5!


## Cryptocurrency Club Guest Speaker

*   **When**  4:30 PM Tuesday, March 3rd
*   **Where** HH 220

Come hear **Jason Hayward**, an attorney specializing in regulatory strategy and
digital assets. He works with early- and growth-stage companies in the
blockchain and fintech space. Jason will share insights from working with
cutting-edge blockchain companies, along with his perspective on current
regulatory and structural trends shaping real business decisions.


## ACM Mobile App Development Workshop

*   **When**  3:00 PM Thursday, March 5th
*   **Where** The Loop (SER 101)
*   **RSVP:** https://forms.gle/CmMPFN3YgnQdtLvm9

Build your first Social Camera app using React Native and Expo  -  in one hour. Donuts will be provided.

Bring a laptop and install the following beforehand:

*   Node.js
*   Git
*   Expo Go (on your phone)
*   Your preferred text editor

[Setup instructions](https://docs.google.com/document/d/1owAGwvi0YUmZF-VSlnmfwTRCZNOHitA7h26S3QsSq_E/view)



# Action Items

*   Erik has office hours today from 1-2PM, and 3-4PM
    -   Find me in SER 301E or on [Zoom](https://usu-edu.zoom.us/my/erik.falor?pwd=ZE4zNXRpNVl4VVhHNkN5Q2wwV3VrUT09)
*   Exam #1 closes on Friday
    *   This exam covers material from **Units 1-3** and closes at 11:59 PM on **Friday, February 27**.
    *   The quizzes in Canvas are the best way to prepare for the exam.
        *   This will incur late penalties, but **I will remove them next week after the exam is over.**
    *   This exam is proctored by Proctorio, and is taken on your own computer.
        -   Run through [Computer Setup (Remotely Proctored)](https://usu.instructure.com/courses/794745/quizzes/1417470) on Canvas to debug any issues with Proctorio.
        -   If your computer is incompatible, use the CS computer lab on the 1st floor of the ESLC, or the Engineering computer lab on the 3rd floor of ENGR.


# [🟥Assn 4a - Design Number Pyramid](https://usu.instructure.com/courses/794745/assignments/5122787)


| Task/Day           | **Thursday**       | **Friday**                  | **Saturday** | **Sunday**                             | **Monday**                                              |
| ------------------ | ------------------ | --------------------------- | ------------ | -------------------------------------- | ------------------------------------------------------- |
| **Classroom Time** | Classroom Lab Time |                             |              |                                        | 4.2: More On Functions <br/> 4.3: Functions In Practice |
| **Items Due**      |                    | Exercise 4.1.2<br/>Quiz 4.1 |              | Assignment 4a<br/>Reflection Survey 4a | Code Reviews for <br/>Assn 4a begin                     |


# Code Park Tycoon

*   Research by: Wei-Jung Lin (Wayne)
    -   Email: wei-jung.lin@usu.edu
*   Advisor: Dr.Yang Shi
    -   Email: yang.shi@usu.edu
*   Team member: Uche Nnaji


### Pre-Survey

*   [Participation Interest Survey & Download Informed Consent](https://usu.co1.qualtrics.com/jfe/form/SV_bCLOTBW5R1dM8XY)
*   [Pre-Survey & Obtain your Participant Code](https://usu.co1.qualtrics.com/jfe/form/SV_2nTwrPhjfvUadMO)


### Download & Install Code Park Tycoon

*Note: These instructions are for Windows users. If you do not have a Windows laptop, you may participate by going to the computer lab upstairs*

0.  Download the program from https://drive.google.com/file/d/1TdsZ9xusy2ifqG0bS5kCbdURliL98NJG/view?usp=drive_link
0.  Unzip the archive
0.  Double click on "FirstProject"


### Post-Survey

*   [Post-Survey: Re-enter your participant code](https://usu.co1.qualtrics.com/jfe/form/SV_57wtCOpIgioUXd4)
*   [Amazon Gift Card Sign-Up](https://usu.co1.qualtrics.com/jfe/form/SV_3l08imejvzsWFh4)


# Code Lab Challenge 0 - Taking Home The Gold

Find and fix the bugs in this program.

### Starter Code

<details>
<summary><h3>Click to reveal the starter code</h3></summary>

```python
# medals.py

def award_medal(points):
    if points >= 9.0:
        print("You got a Gold medal!!!")
        return "Gold"
    if points >= 7.0:
        print("You got a Silver medal!")
    print("You got a Bronze medal.")
    return "Bronze"


def verb(n):
    # TODO: handle the singular case
    return 'are'

def pluralize(n):
    # TODO: handle the singular case
    return 's'


# Award medals
medals = []
scores = [ 9.8, 6.9, 8.0, 10.0, 7.6, 8.5, 9.9 ]
for score in scores:
    medals.append(award_medal(score))


# Count the number of medals awarded
golds = medals.count("Gold")
# TODO: count the other medals, too.


# TODO: using the verb() and pluralize() functions, print messages like these:
#   There are 3 Gold medals
#   There is 1 Bronze medal


# TODO: Did we give out the right medals?
```

</details>


### Phase 0 - Identify The Bug(s)

Answer these questions in today's Wooclap:

*   What does `award_medal(8.0)` print and return? Why?
*   Which control-flow keyword is missing and causes multiple messages to print?
*   For inputs `9.8`, `6.9`, `8.0`, list the printed line(s) and the return value for each.
*   Which rule is violated if this function is ever used on the right-hand side of `=`?
*   Where are unimplemented behaviors in `verb(n)` and `pluralize(n)` visible in the output?
*   What counts are missing before printing the summary?



### Phase 1 - Fix It

Implement these changes:

*   Make `award_medal(points)` a **total function**: one and only one message is printed and there is one `return` statement on every path.
    *   Use `elif` and `else` correctly.
*   Finish `verb(n)` so it returns `"is"` and `"are"` appropriately
*   Finish `pluralize(n)` so it returns `"s"` and `""` appropriately
*   Count Silver and Bronze medals in the variables `silvers` and `bronzes`.
*   Print three grammatically-correct messages using the helper functions.


### Phase 2 - Test It

Run the program with varied inputs.  Record the results in Wooclap:

*   Edge cases: `9.0`, `7.0`, `6.9999`, `9.0000`.
*   Mixed set: `[9.0, 8.99, 7.0, 6.5, 10.0]`.
*   Confirm:
    *   Exactly one message printed per score.
    *   Return values match printed messages.
    *   Summary grammar is correct for 0, 1, and many medals.


### Phase 3 - Reflect On It

Answer these debrief questions in comments in today's Wooclap:

*   Why is mixing side-effects and partial returns risky?
*   What off-by-one risks exist at the threshold values and how did you test them?


# Code Lab Challenge 1 - Function Arguments

In this challenge you will master positional vs keyword arguments, defaults, and keyword-only parameters by designing tiny APIs and proving valid vs invalid calls.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 4*


### Program Requirements

0.  Create a Python file named `person.py`.
1.  Define a function called `person_info(...)` that prints and returns a short description of a person.  The function should demonstrate correct use of **positional**, **keyword**, and **default** arguments.
2. Your program must include a short test section that shows at least **six valid function calls** using different combinations of arguments.
   Here are some examples of what these calls might look like and what strings they should return:

```python
person_info("Alice")
# "Alice is 30 years old and likes ramen in Logan"

person_info("Bob", 22)
# "Bob is 22 years old and likes ramen in Logan"

person_info("Cara", food="sushi")
# "Cara is 30 years old and likes sushi in Logan"

person_info("Dan", 40, "tacos", city="Ogden")
# "Dan is 40 years old and likes tacos in Ogden"
```


### Phase 0 - Design It

Answer each of these questions in Wooclap:

0. What is the user experience?
1. How do I get the necessary data?
2. What do I need to process and calculate?
3. How am I going to process and calculate it?
4. What do I need to display as results?


### Phase 1 - Pseudocode It

Using the answers to the above questions as your guide, write *pseudocode* as a block of comments in your program.  Start by describing the flow of the program in plain English.  Refine your pseudocode until it is as specific as Python code.


### Phase 2 - Build It

When your pseudocode is basically line-for-line equivalent to real Python code, rewrite each comment as code.


### Phase 3 - Reflect On It

Answer these debrief questions in comments in today's Wooclap:

* Did my pseudocode line up with the code I wrote, or did I change course while coding? Why?
* Which three rules did you verify for arguments?  Give a failing example for each.
* What keyword name did you choose for the 2nd parameter (the integer)?
* What advantage do keyword parameters provide?
* How do defaults interact with positional and keyword passing at the call site?


### Phase 4 - Stretch Challenges

0. Add an optional keyword-only parameter `verbose` which causes the function to immediately print its string in addition to returning it.  It defaults to `False`.
    -   An optional keyword-only parameter is created by placing `*,` (asterisk followed by a comma) in the parameter list, followed by a named parameter with a default value.  The resulting parameter can *only* be specified by name.  Python will raise an error if you try to treat it as a positional parameter.
    -   Add tests that call `person_info("Lee", verbose=True)` and confirm both printed side-effect and returned value.
1. Add a second function called `enroll` with a *required* keyword-only parameter `student`.
    -   A required keyword-only parameter is created by placing `*,` in the parameter list, followed by a named parameter **without** a default value.  The resulting parameter can *only* be specified by name, and *must* be given a value.  Python will raise an error if you try to treat it as a positional parameter.
    -   `enroll`'s parameters are:
        1.  `course`, required positional, no default
        2.  `section`, optional with a default value of `1`
        3.  `student`, required keyword-only
        4.  `credit_hours`, optional keyword-only with a default value of `3`


