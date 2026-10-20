# Lecture 16: Functions

**Class:** CS 1400
**Date:** Oct. 19, 2026
**Modules:** 4.1

---

## Why functions?

- Repetitive code
- Change the repetition

```python
print("Hello Ana, from CS1.")
print("Hello Alice, from CS1.")
print("Hello Arty, from CS1.")
```

*To change that to a different greeting is a pain.*

## Defining functions

*A function is a named, reusable chunk of code.*

- print()
- len()
- input()
- str(), int(), float()
- math.randint()
- abs()

## In Class Demo

#### Clap function

#### Double function

#### Sum function

## Syntax

```python
def function_name(parameter1, parameter2):
    # statement1
    # statement2
    return some_value #optional

# Calling the function
val = function_name(a1, a2)
```

Definitions
- def
- function_name
- parameters
- colon
- statements (watch the indent)
- return (what does this mean)

Using it:
- Call the function
- Provide arguments
- Store or use the return value

### Examples

```python
def greet():
    print("Hello!")

greet()
greet()
```

```python
def greet(name):
    print("Hello " + name + "!")

greet("Laura")
greet("Eddie")
```

```python
def square(x):
    return x ** 2

x = 16
x_squared = square(x)
y = 13
y_squared = square(y)

print(x_squared)
print(y_squared)
```

## Parameters vs arguments

```python
def square(x): # x = parameter
    return x ** 2

print("16 squared is: " + str(square(16))) # 16 = argument

for x in range(10):
    print(str(x) + " squared is: " + str(square(x+1)))
```

## Find Student (bigger example)

I want to see if a student has registered for a class.

Now I want to know what index they are in the list

```python
def find_student(roster, name):
    for i in range(len(roster)):
        if roster[i] == name:
            return i
    return -1

roster = ["Ana", "Ben", "Chloe", "Dev", "Eli"]
print(find_student(roster, "Chloe"))   # 2
print(find_student(roster, "Zoe"))     # -1
```

## Common errors

- Forgetting the colon or the indentation.
- Calling a function with the wrong number of arguments (TypeError).
- Forgetting return and getting None.
- Using a variable defined inside a function from outside it (a gentle preview of scope).

## Exercises

### double(n)

Write a function that returns double it's input and prints it

### fahrenheit_to_celsius(temp)

Write a function that converts a fahrenheit temperature to celsius and prints the result.

``celsius = (f - 32) * 5 / 9``

### double(n)

Write a function that returns double it's input and prints it

### Scramble string

Write a function that accepts a string and returns that same string, scrambled


