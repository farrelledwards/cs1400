CS1400 - Tuesday, January 27 - Lecture 7 - Module 2

# Topics:
* [🟥Assn 2a - Investments & Polygon Area](#assn-2a---investments--polygon-area)
* [Code Lab Challenge 0 - Omni Calculator](#code-lab-challenge-0---omni-calculator)
* [Code Lab Challenge 1 - Formula Translation](#code-lab-challenge-1---formula-translation)
* [Code Lab Challenge 2 - One-Line Fix Programs](#code-lab-challenge-2---one-line-fix-programs)


------------------------------------------------------------
# Announcements

## *TODAY* FSLC - Self-Hosting a Minecraft Server

*   **When**    6:30 PM Tuesday, January 27th
*   **Where**   WIDT 007
*   **Website** https://linux.usu.edu
*   **Discord** https://discord.gg/PvgG6N2hsU

Your friends will really like you if you come let @Samwell (Samuel Powell) teach you how to self host a Minecraft server!

You've finally got your own home-server! Be it an old computer given new life, or a purpose built powerhouse, you probably want to do something with it. But how? In this showcase, we'll demonstrate from start to finish setting up and configuring a Minecraft server. Along the way we'll discuss several tools and terms (watch for `wget`, systemd services, NAT forwarding and more) to power up your self-hosting experience.


## *TOMORROW* ACM Lightning Presentations

![](./00-acm-lightning-presos.png)

*   **When**  11:30 PM Wednesday, January 28th
*   **Where** The Loop - SER 101 
*   **Refreshments Provided**


# [🟥Assn 2a - Investments & Polygon Area](https://usu.instructure.com/courses/794745/assignments/5122783)

*   This assignment has two tasks
*   Read the instructions *carefully*, but also look at the **rubric**
    *   Use the rubric as a checklist so you don't miss important requirements
*   This assignment is due **at 11:59 PM on Sunday, February 1st**


## Task 1 - Investments

*   This is a *console* program (i.e. text-only interface) that computes the future value of an investment
    *   You **will not** need to `import drawly`; instead, use `print()` and `input()`
    *   Translate the given formula into Python using variables, arithmetic, the `round()` function and type conversion functions (i.e. `int()`, `float()`)
*   Put your code in a file called `task1.py`
*   Test your program with a variety of inputs and double check its accuracy by hand or with a calculator (the assignment page on Canvas links to one)
*   You will use knowledge from these sections of Unit 2
    *   **2.1: Arithmetic**


## Task 2 - Polygon Area

*   Put your code in a file called `task2.py`
*   This is also a *console* program
    *   Use different importing techniques to access the functions from the `math` module
*   Test your program with a variety of inputs and double check its accuracy by hand or with a calculator (the assignment page on Canvas links to one)
*   You will use knowledge from these sections of Unit 2
    *   **2.2: Modules and Importing**
    *   **2.3: Lists and Data**


| Task/Day           | **Tuesday**        | **Wednesday**                                        | **Thursday**       | **Friday**                                                                | **Saturday** | **Sunday**                             | **Monday**                               |
| ------------------ | ------------------ | ---------------------------------------------------- | ------------------ | ------------------------------------------------------------------------- | ------------ | -------------------------------------- | ---------------------------------------- |
| **Classroom Time** | Classroom Lab Time | 2.2: Modules and Importing <br/> 2.3: Lists and Data | Classroom Lab Time |                                                                           |              |                                        | 2.4: Software Design <br/> 2.5: Booleans |
| **Items Due**      |                    |                                                      |                    | Exercises 2.1.2, 2.1.3, 2.2.3-a, 2.2.3-b, 2.3.1<br/>Quizzes 2.1, 2.2, 2.3 |              | Assignment 2a<br/>Reflection Survey 2a | Code Reviews for <br/>Assn 2a begin      |


# Code Lab Challenge 0 - Omni Calculator

In this challenge you will write a console program that asks the user for two floating-point numbers (any mix of positive or negative).  It will apply all of Python's arithmetic operators to these inputs and display the results.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 4*


### Program Requirements

Make your program's output match this example:

```
Welcome to the Omni-Calculator, your one-stop shop for all of your arithmetic needs!
What is the first number? -21.5
What is the second number? 8

unary + applied to -21.5 is -21.5
unary + applied to 8.0 is 8.0
unary - applied to -21.5 is 21.5
unary - applied to 8.0 is -8.0
-21.5 + 8.0 = -13.5
-21.5 - 8.0 = -29.5
-21.5 * 8.0 = -172.0
-21.5 / 8.0 = -2.6875
-21.5 // 8.0 = -3.0
-21.5 % 8.0 = 2.5
-21.5 ** 8.0 = 45657032334.37891

Thank you for using the Omni-Calculator!
```

#### Necessary Jargon

*   **Operator**: An arithmetic symbol
*   **Operand**: the values the operator acts on; usually numbers
*   **Unary Operator**: Operator that uses a single operand
    *   The operand appears on the right
*   **Binary Operator**: Operator that uses two operands
    *   The operands *surround* the symbol

#### Python's Arithmetic Operators

*   **Unary `+`**: signifies a positive number (very rarely used)
*   **Binary `+`**: addition - yields a sum (with numeric operands) or concatenation (with string operands)
*   **Unary `-`**: signifies a negative number
*   **Binary `-`**: subtraction - yields a difference
*   **Binary `*`**: multiplication - yields a product
*   **Binary `/`**: division - yields a floating-point quotient (`dividend / divisor = quotient`)
*   **Binary `//`**: "integer" or "floor" division operator (always yields an integer quotient)
*   **Binary `%`**: modulus, but is also called remainder
    *   *Technically*, a modulus is different than a remainder with a negative dividend
    *   In Python `%` performs the **modulo** operation and *only* yields positive results, even though the [official documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) calls this the *remainder* operator
    *   Just so you are aware, in other programming languages this same symbol performs the **remainder** operation
        *   Moduli can only be *positive*
            *   ex. `2` is the modulo left over by `-7 % 3` in Python
        *   Remainders can be *negative*
            *   ex. `-1` is the remainder left over by `-7 % 3` in languages like C, C++, and JavaScript
    *   *For math nerds*: [Wikipedia's article on Modulo](https://en.wikipedia.org/wiki/Modulo)
*   **Binary `**`**: exponentiation - raises the number on the left to the power on the right



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

0.  Which operator's result surprised you the most, and why?
0.  If the user enters `0` for the second number, which of your calculations break?
0.  How does changing the order of the two inputs affect each operation's result?
0.  How do Python's arithmetic operators behave differently with integers vs. floats, and where do you see that difference in your output?
0.  Why does floor division `//` sometimes feel "wrong" with negative numbers, and what rule is Python actually following?
0.  What assumptions does your program make about user input, and which of those assumptions are risky in real software?
0.  If you were grading this as an assignment, which mistakes do you think would be most common?


### Phase 4 - Stretch Challenges

Did you finish early?  Was this still too easy for you?  Here are some more features to implement:

0.  **Repeat mode:** allow the user to run the calculator again without restarting the program.
0.  **Input validation loop:** keep re-prompting until the user enters a valid number (no crashes on bad input like `hello`).
0.  **Division-by-zero handling:** if the second number is `0`, print a friendly message for the affected operations instead of crashing, but still show the other operations.
0.  **Make the output a table:** align the results in neat columns and let the user choose how many decimal places to display (try using `round()` or f-string formatting).
0.  **Precedence mode:** ask for a third number and print the results of a few expressions that differ *only* by parentheses, e.g. `a + b * c` vs `(a + b) * c` (include the expression text in the output).
0.  **Exact vs. approximate mode:** let the user choose between floating-point math and integer-only math (with clear warnings about truncation).
0.  **Operator map:** store operators and their symbols in a data structure (e.g., list of tuples or dict) and loop over it instead of writing each operation manually.
0.  **IDK, surprise me:** the program randomly picks an integer when the user inputs no number at all (e.g. the user just hits `Enter` at a prompt)


# Code Lab Challenge 1 - Formula Translation

In this challenge you will translate each formula into Python syntax.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 4*


### Hints

0.  Be careful with **parentheses** - operator precedence matters.
0.  After writing your code, test with the sample values to check correctness.
0.  Use `**` for powers, `/` for division.
0.  Write `import math` math at the top of your program to access the square root  function `math.sqrt()`.
    -   You can also use a fractional exponent with `**`
0.  Verify your results against the expected outputs.  Use the links to online calculators to test more values.


### Phase 0 - Write It

#### Ideal Gas Law (Volume)
Formula:
$`V = \frac{nRT}{p}`$

Sample values: `n=230, R=8.3145, T=298, p=273154`

Expected output: ~`2.09`

https://www.omnicalculator.com/physics/ideal-gas-volume


#### Coulomb's Law
Formula:
$`F = k \cdot \frac{q_1 q_2}{r^2}`$

Sample values: `k=8.99e9, q1=1e-6, q2=2e-6, r=0.05`

Expected output: ~`7.19`

https://www.omnicalculator.com/physics/coulombs-law


#### Thin Lens Equation
Formula:
$`\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}`$

Sample values: `do=30, di=60`

Expected output: `f=20.0`

https://www.omnicalculator.com/physics/thin-lens-equation


#### Quadratic Formula
*Do this in two parts, separately calculating x1 and x2*

Formula:
$`x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}`$

Sample values: `a=1, b=-3, c=2`

Expected outputs: `x1=2.0, x2=1.0`

https://www.omnicalculator.com/math/quadratic-formula


#### Relativistic Time Dilation
Formula:
$`t' = \frac{t}{\sqrt{1 - (v^2/c^2)}}`$

Sample values: `t=1, v=2.5e8, c=3.0e8`

Expected output: ~`1.81`

https://www.omnicalculator.com/physics/time-dilation


#### Compound Interest
Formula:

$`A = P \cdot (1 + \frac{r}{n})^{n \cdot t}`$

Sample values: `P=1000, r=0.05, n=12, t=10`

Expected output: ~`1647.01`

https://www.omnicalculator.com/finance/compound-interest


#### Net Present Value (2 periods)
Formula:

$`NPV = \frac{CF_1}{(1+r)} + \frac{CF_2}{(1+r)^2} - C_0`$

Sample values: `CF1=500, CF2=600, r=0.08, C0=900`

Expected output: ~`77.37`

https://www.omnicalculator.com/finance/net-present-value


#### Future Value of an Annuity
Formula:
$`FV = P \cdot \frac{(1 + r/n)^{n \cdot t} - 1}{r/n}`$

Sample values: `P=1000, r=0.05, n=12, t=10`

Expected output: ~`15529.13`

https://www.omnicalculator.com/finance/annuity-future-value


### Phase 1 - Reflect On It

Answer these debrief questions in comments in today's Wooclap:

* Which formula required the most careful use of parentheses, and what went wrong the first time you tried it?
* How did translating math notation (fractions, exponents, square roots) into Python syntax differ from how you normally write math on paper?
* Which variables or constants were easiest to confuse or mistype, and how did you catch the mistake?
* How did testing with the provided sample values help you verify that your translation was correct?


### Phase 2 - Stretch Challenges

Did you finish early?  Was this still too easy for you?  Here are some more features to implement:

0. Rewrite at least two formulas using intermediate variables to make each step more readable.
0. For one formula, intentionally remove parentheses and observe how the result changes; explain why in a comment.
0. Prompt the user for input values instead of hardcoding the sample values.
0. Choose one formula and format the output to include both the formula name and the final computed value in a clean sentence.


# Code Lab Challenge 2 - One-Line Fix Programs

There are three broad categories of errors that you will encounter while programming. Knowing their names helps you to more quickly identify and fix them.

0. **Syntax error**
    * A problem with the construction of the code; one of the "rules" was not followed
    * Identifying question: did the program even start to run?
    * Examples: missing quote marks, missing parentheses, misspelled key words
1. **Run-time error**
    * An invalid operation was attempted and caused the program to crash
    * May only happen some of the time, depending on user input or other external factors
    * Identifying question: did the program fail after it began running?
    * Examples: undefined arithmetic operations (division by zero), misspelled function names
2. **Logic error**
    * The program doesn't crash, but also doesn't behave how you expected it to
    * From the programming language's perspective, nothing is wrong with your program, so no error messages are given
    * These are the most difficult bugs to find because they are so *subtle*!
    * Identifying question: did the program behave in an unexpected way?


Each of the following programs contains **exactly one bug**. Your job is to:

0. Run each and observe what happens.
0. Decide what category of error it is (**syntax**, **run-time**, or **logic**).
0. Fix the bug by changing *only* what is necessary.
0. Re-run the program to prove the fix worked.
0. Write your findings in today's WooClap


#### Program A

```python
name = input("What is your name? ")
print("Hello, " + name + "!)
```


#### Program B

```python
PI = 3.141592653589793

r = float(input("Radius (try 1, 1.0, one, etc.: "))
area = PI * r**r
print("Area:", area)
```


#### Program C

```python
total = int(input("Input a number of seconds (e.g. 120, 3611, 86521): "))
minutes = total // 60
seconds = total % 60
hours = minutes // 60
minutes = minute % 60
days = hours // 24
hours = hours % 24

print(days, "days,", hours, "hours,", minutes, "minutes,", seconds, "seconds")
```


#### Program D

```python
print("""Welcome to the MPG calculator!
How efficient is your car?  You're about to find out!
""")

miles = float(input("Miles driven: "))
gallons = float(input("Gallons used (input 0 for electric cars): "))
mpg = miles / gallons
print("MPG:", mpg)
```


#### Program E

```python
width = float(input("Width: "))
height = float(input("Height: "))
area = width * height
print("Area:", area))
```



#### Program F

```python
total = int(input("Input a number of seconds (e.g. 120, 3611, 86521): "))
minutes = total // 60
seconds = total % 60
hours = total // 60
minutes = hours % 60
days = hours // 24
hours = hours % 24

print(days, "days,", hours, "hours,", minutes, "minutes,", seconds, "seconds")
```


