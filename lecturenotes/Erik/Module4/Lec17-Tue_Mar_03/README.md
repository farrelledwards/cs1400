CS1400 - Tuesday, March 03 - Lecture 17 - Module 4

# Topics:
* [🟥Assn 4b - Chessmate & Patterns](#assn-4b---chessmate--patterns)
* [Exam #1 Recap](#exam-1-recap)
* [Code Lab Challenge 0 - Explore Python Types](#code-lab-challenge-0---explore-python-types)
* [Code Lab Challenge 1 - Python Object IDs](#code-lab-challenge-1---python-object-ids)
* [Code Lab Challenge 2 - Fix My Module Bug](#code-lab-challenge-2---fix-my-module-bug)


------------------------------------------------------------
# Announcements

## *TODAY* Cryptocurrency Club Guest Speaker

*   **When**  4:30 PM Tuesday, March 3rd
*   **Where** HH 220

Come hear **Jason Hayward**, an attorney specializing in regulatory strategy and
digital assets. He works with early- and growth-stage companies in the
blockchain and fintech space. Jason will share insights from working with
cutting-edge blockchain companies, along with his perspective on current
regulatory and structural trends shaping real business decisions.


## *TODAY* FSLC - GrapheneOS

*   **When**    6:30 PM Tuesday, March 3rd
*   **Where**   WIDT 007
*   **Website** https://linux.usu.edu
*   **Discord** https://discord.gg/PvgG6N2hsU

Are you tired of spyware on your phone? Are you even aware of the privacy vulnerabilities that come with a stock mobile operating system? Fear not, for there's alternatives! One such option is called Graphene OS. This presentation will be all about the security focused Android ROM from the open source community. We'll cover how installation works, all the biggest features, some software to go with it, and even how to de-google/debloat non-graphene OS Android phones.


## *TOMORROW* Student Organization for Cybersecurity - LEGOs and Lofi

- **When** 7 PM Wednesday, March 4th
- **Where** HH 360
- **Discord** https://discord.gg/JEVdRdfpEb


## ACM Mobile App Development Workshop

*   **When**  3:00 PM Thursday, March 5th
*   **Where** The Loop (SER 101)
*   **RSVP:** https://forms.gle/CmMPFN3YgnQdtLvm9

Build your first Social Camera app using React Native and Expo - in one hour. Donuts will be provided.

Bring a laptop and install the following beforehand:

*   Node.js
*   Git
*   Expo Go (on your phone)
*   Your preferred text editor

[Setup instructions](https://docs.google.com/document/d/1owAGwvi0YUmZF-VSlnmfwTRCZNOHitA7h26S3QsSq_E/view)


# [🟥Assn 4b - Chessmate & Patterns](https://usu.instructure.com/courses/794745/assignments/5122788)

*   This assignment has two tasks
*   Read the instructions *carefully*, but also look at the **rubric**
    *   Use the rubric as a checklist so you don't miss important requirements
*   Beginning with this assignment you are given **starter code**
    *   Look for the code in Canvas, either as a block of text to *copy and paste* or a *file to download*
    *   An important aspect of this assignment is to *study* the starter code to understand what it does
    *   A big mistake students make is to *modify* the starter code; don't do that unless you are explicitly directed to do so!
*   This assignment is due **at 11:59 PM on Sunday, March 8th**


## Task 1 - Chessmate

Prompt the user for some information in the console and then draw a chessboard in Drawly according to their specifications.

*   You will submit three files: `task1.py`, `chessboard.py`, and `design1.txt`
*   The design will only include three functions in your `chessboard.py` file
*   You will draw a chessboard based on user inputs.
    *   You will ask for the starting location (x, y) and a height and width of the board.
    *   The location is the top left corner of the chessboard.
*   You will use this information to draw the chessboard (just a single chessboard).
*   Keep in mind that it *may not be a square*.
*   You will use knowledge from these sections of Unit 4
    *   **4.2: More On Functions**
    *   **4.3: Functions In Practice**
*   There is a **starter code** template on the assignment in Canvas that you must copy into your program!


## Task 2 - Patterns

You're going to write a program that draws some mesmerizing pictures in Drawly.  Try not to get dizzy watching your creation when you're done.

*   There is a **starter code** file in the assignment in Canvas that you must download and use!
*   You will submit three files: `task2.py`, `pattern.py`, and `design2.txt`.
    *   You should add to the **starter code** in the areas indicated, but not modify any existing code.
*   You will use knowledge from this section of Unit 4
    *   **4.4: Super Target**



| Task/Day           | **Tuesday**        | **Wednesday**     | **Thursday**       | **Friday** | **Saturday** | **Sunday**                             | **Monday**                                                       |
| ------------------ | ------------------ | ----------------- | ------------------ | ---------- | ------------ | -------------------------------------- | ---------------------------------------------------------------- |
| **Classroom Time** | Classroom Lab Time | 4.4: Super Target | Classroom Lab Time |            |              |                                        | **Spring Break - No School**                                     |
| **Items Due**      |                    |                   |                    |            |              | Assignment 4b<br/>Reflection Survey 4b | Code Reviews for <br/>Assn 4b will happen<br/>after Spring Break |


# Exam #1 Recap

| Average | High | Low | Standard Deviation | Average Time |
|:-------:|:----:|:---:|:------------------:|:------------:|
|   87%   | 100% | 60% |        9.00%       |     26 min   |


#### __Question 41__ (47% answered correctly)

**Q:** What is the term that refers to the area in a program where you can use an identifier?

**A:** scope

Other responses:

-   body
-   variable
-   modules
-   function
-   object
-   code
-   solitude?


#### __Question 20.1__ (48% answered correctly)

**Q:** Fill in the blank in the code to produce the following output: `10 20 30 40 50 60`

```python
my_list = [10, 20, 30, 40, 50, 60]

for i in ______:
    print(i)
```

**A:** `my_list`

Distractors:

*   (26%)  `range(len(my_list))`
*   (19%)  `range(my_list)`
*   (3%)   `len(my_list)`
*   (3%)   *Output is not possible*
*   (2%)   `my_list < 6`



#### __Question 23.2__ (55% answered correctly)

**Q:** How many times will the message print?

```python
for i in range(1, 12, 2):
    print("Loopy!")
```

**A:**  None of the Above

Distractors:

-   (40%) 5
-   (3%) 4
-   (2%) 10
#### __Question 12.1__ (56% answered correctly)

**Q:** What is the output of the following program? (Assume the user enters `12`)

```python
my_num = int(input("Enter a number: "))
print("Adding 10:", my_num + 10)
```

**A:** Adding 10: 22

Distractors:

*   (42%) Error because the addition didn't work
*   (2%) Adding 10: 12



#### __Question 25__ (61% answered correctly)

**Q:** Fill in the missing piece of code, such that the print statement executes 5 times.

```python
done = False
count = 1

while not done:
     print("in the loop")
     if ______:
          done = True
     count += 2
```

**A:** `count >= 9`

Distractors:

*   (24%) `count > 10`
*   (6%) `count >= 7`
*   (6%) `count <= 7`
*   (2%) `count < 7`



#### __Question 23.1__ (73% answered correctly)

**Q:** How many times will the message print?

```python
for i in range(1, 5):
    print("Loopy!")
```

**A:** 4

Distractors:

-   (27%) 5
-   (0%) 3
-   (0%) 6
-   (0%) More than 6


# Code Lab Challenge 0 - Explore Python Types

In this challenge you will explore Python's `type()` function by running and modifying the `types.py` program to see how Python identifies different kinds of values.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 2*

### Phase 0 - Experiment

0.  Copy the provided **`types.py`** file into your PyCharm project.
1.  Run the program once as-is and read the output carefully.  Observe which message prints and what the `type()` function returns.
2.  Next, modify the value of the variable `a` several times and re-run the program.  Try values such as:
    -   ```python
        a = 42
        a = 3.14
        a = [1, 2, 3]
        a = "hello"
        a = MyNumber()
        a = None
        a = False
        ```
3.  Each time, record in Wooclap what the output shows and what branch of the `if`/`elif` statement executes.  Identify what `type()` returns for each kind of value.
    -   (for example: "`a = 'hello'`  # printed ‘some other kind of value'")
4.  Do not delete or rewrite the existing code - just change the value assigned to `a` and re-run the file.



#### types.py

```python
# types.py

class MyNumber:
    pass


a = MyNumber();

if type(a) == int:
    print("the variable 'a' contains an integer")
elif type(a) == float:
    print("the variable 'a' contains a floating-point number")
elif type(a) == list:
    print("the variable 'a' contains a list")
elif type(a) == MyNumber:
    print("the variable 'a' contains a MyNumber object")
else:
    print("the variable 'a' contains some other kind of value")
```



### Phase 1 - Reflect On It

Then, answer each of these questions in Wooclap:

0. What is the user experience of this program?
1. What data am I changing or testing?
2. What is the program processing or comparing?
3. How does it decide which message to print?
4. What result should I expect for each different type of value I assign to `a`?
* How does `type()` help you understand what kind of data your variable holds?
* When you changed `a`, which values triggered the `else` branch? Why?


### Phase 2 - Stretch Challenges

0.  Add another `elif` branch for strings or booleans. Re-run the program to confirm it works.
0.  What happens if you use `if isinstance(a, MyNumber)` instead of comparing with `if type(a) == MyNumber`?
    -   Add print statements to see how object identity differs from type equality.
0.  Create two instances of `MyNumber` and use `==` and `is` to compare them.  Fill in the blanks in the snippet below:
    -    ```python
        a = MyNumber()
        b = MyNumber()

        if a == b:
            print(...)
        else:
            print(...)

        if a is b:
            print(...)
        else:
            print(...)
        ```


# Code Lab Challenge 1 - Python Object IDs

In this challenge you will explore Python's `id()` function by running and modifying the `id.py` program to see how Python identifies values and variables.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 2*

### Phase 0 - Experiment

0.  Copy the provided **`id.py`** file into your PyCharm project.
1.  Run the program and read the output carefully.


#### id.py

```python
# id.py

print("These ID number are hard to read; focus on the last 4 digits")
print("id(7) is    ", id(7))
print("id(8) is    ", id(8))

a = 7
b = 8
seven = 7

print("\n'a' and 'seven' share the same ID with id(7) above")
print("id(a) is    ", id(a))
print("id(b) is    ", id(b))
print("id(seven) is", id(seven))


print("\nIncrementing seven...\n")
seven += 1

print("now 'b' and 'seven' have the same ID")
print("id(a) is    ", id(a))
print("id(b) is    ", id(b))
print("id(seven) is", id(seven))

print("\nIdentical integers share an ID, but identical lists and tuples do not")
l0 = [0, 1, 2, 3]
l1 = [0, 1, 2, 3]
print("id(l0) is   ", id(l0), "and the object looks like this:", l0)
print("id(l1) is   ", id(l1), "and the object looks like this:", l1)
print("l0 == l1 is ", l0 == l1)
print("l0 is l1 is ", l0 is l1)

print("\nAssigning l0 = l1...\n")
l0 = l1
print("l0 == l1 is ", l0 == l1)
print("l0 is l1 is ", l0 is l1)

print("\nAssigning l0[1] = 'hello world'...\n")
l0[1] = 'hello world'
print("Now the l0 object looks like this:", l0)
print("And the l1 object looks like this:", l1)
print("l0 == l1 is ", l0 == l1)
print("l0 is l1 is ", l0 is l1)

print("\nMaking tuples out of l0...\n")
t0 = tuple(l0)
t1 = tuple(l0)
print("id(t0) is   ", id(t0), "and the object looks like this:", t0)
print("id(t1) is   ", id(t1), "and the object looks like this:", t1)
print("t0 == t1 is ", t0 == t1)
print("t0 is t1 is ", t0 is t1)
```



### Phase 1 - Reflect On It

Answer each of these questions in Wooclap:

0. What is the difference between `==` and `is`?
1. When did you observe two values that were *equal* (`==`) but not the *same object* (`is`)?
2. Why do identical small integers like `7` and `7` share the same ID, while identical lists do not?
3. After reassigning `seven += 1`, what happened to its ID? Why?
4. What does the line `l0 = l1` do differently from `l0 = [0, 1, 2, 3]`?
5. When you modified `l0[1] = 'hello world'`, why did that also change `l1`?
6. Why do tuples created from the same data (`t0`, `t1`) have different IDs even though they compare as equal?
7. Based on what you observed, how would you explain Python’s “pass by value” or “pass by object reference” behavior in one sentence?


### Phase 2 - Stretch Challenges

0. **String Interning:**
    -    Create two identical short string literals (`"hi"`) and two long strings (`"this is a long string"`) and compare their IDs.
    -    What pattern do you see? Why might Python reuse IDs for short strings?
1. **Aliasing Challenge:**
    -    Create a list `x = [1, 2, 3]` and a second variable `y = x`.
    -    Modify one element through `y`.
    -    Predict and confirm how this affects `x` and the IDs of both variables.
2. **Copy Experiment:**
    -    Try each of the following and record whether `is` and `==` return the same results:
    -   ```python
        a = [1, 2, 3]
        b = a[:]          # slice copy
        c = list(a)       # constructor copy
        d = a             # alias
        ```
    -   Summarize which versions share the same ID.
3. **Function Identity Test:**
    -   Write a function that accepts a list and modifies it in place.
    -   Use `id()` inside and outside the function to show that both refer to the same object.
4. **Tuple vs List Mutation:**
    -   Create a tuple containing a list:
    -   ```python
        t = ([1, 2, 3], 4)
        ```
    -   Change an element inside the list and observe what happens to `t`.
    -   What does this show about “immutability” and object references?
5. **Memory Detective:**
    -   Make a list of 10 integers, print all their IDs, then add or remove elements.
    -   Observe whether the list’s ID changes or stays constant.
    -   What conclusion can you draw about how Python stores mutable objects?


# Code Lab Challenge 2 - Fix My Module Bug

Find and fix the bugs in this program.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 4*

#### random.py

```python
# random.py
from random import randint


def make_random_list(count):
    num_list = []
    for i in range(count):
        num_list.append(randint(10, 30))
    return num_list


def find_num_in_list(num_list, key):
    location = -1
    for i in range(len(num_list)):
        if num_list[i] == key:
            location = i
            break
    return location
```

**main.py**

```python
# main.py
from random import get_random_list, find_num_in_list


def main():
    my_list = make_random_list(10)
    print(my_list)
    result = find_num_in_list(my_list, 20)
    print(result)


main()
```


### Phase 0 - Identify The Bug(s)

Answer each of these questions in today's Wooclap:

* What happens when `random.py` executes `from random import randint`? Why does this happen?
* Why does `from random import get_random_list, find_num_in_list` fail in `main.py`?
* Which names should `main.py` import, and from which module?
* After fixing the import collision, what `NameError` remains and why?


### Phase 1 - Fix It

Enact your proposed changes in the program.


### Phase 2 - Test It

Run the program with a variety of inputs to make sure that

* The standard library `random.randint` is accessible from your helper module after the rename.
* `main.py` runs without `NameError` or `ImportError`.
* Lists have the requested length and values fall within `[low, high]`.
* Stretch: overriding bounds works, e.g., `make_random_list(5, low=1, high=3)` only yields 1–3.

Suggested quick checks to paste at the bottom of `main.py` during testing:

* Generate a list of length 10. Assert its length is 10.
* Generate another list of length 50. Assert its length is 50.
* Search for a known present value and a known absent value. Verify indices `>=0` and `-1`.


### Phase 3 - Reflect On It

Answer these debrief questions in comments in today's Wooclap:

* How did the filename collision with the standard library cause the observed error? Describe Python’s module search order.
* What are two safe import patterns that keep namespaces clear in multi-file programs?


### Phase 4 - Stretch

* Change `make_random_list(count)` to `make_random_list(count, low=10, high=30)` so callers can override bounds.
* Update call sites and docstrings to reflect defaults and parameter behavior.


