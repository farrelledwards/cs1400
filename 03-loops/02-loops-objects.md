# Lecture 15: Loops

**Class:** CS 1400
**Date:** 10-15-2026
**Modules:** 3.5, 3.6

---

## Big Ideas
- Fix up the polygon thing from last time.
- Finish loops (break, continue, nested, choosing)
- Do a project


## Continue / Break 

### Input validation: - Easy
```python
age = int(input("Enter your age: "))
while age < 0 or age > 120:
    print("That's not a valid age.")
    age = int(input("Enter your age: "))
print("Thanks!")
```
### Better
```python
while True:
    age = int(input("Enter your age: "))
    if 0 <= age <= 120:
        break
    print("That's not a valid age.")
print("Thanks!")
```
### Best
```python
while True:
    age = input("Enter your age: ")
    if not age.isdigit():
        print("Please use only digits")
        continue
    age_int = int(age)
    if 0 <= age_int <= 120:
        break
    print("That's not a valid age.")
print("Thanks!")
```

## Nested Loops

### Print rectangle of stars: 
```python
for row in range(3):
    for col in range(5):
        print("*", end="")
    print()
```

### Triangle:
```python
for row in range(1, 6):
    for col in range(row):
        print("*", end="")
    print()
```

### Print multiplication table:
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(i*j, end="\t")
    print()
```

## How to choose?
| Scenario | loop type | Notes |
|----|----|----|
|Print the first 10 multiples of 5|for|Known count|
|Print every name in a class roster|for|A collection with a known end|
|Roll a die until you get a six|while|Ends on a random event|
|Compute interest for exactly 10 years|for|Known count|
|Find how many years until $1,000 at 5% interest doubles (answer: 15)|while|The count depends on the result|
|Count the vowels in a sentence|for|Walking through a string|
|Print a seating chart with 4 rows of 6 seats|for inside for|Both counts are known|
|Read lines the user types until they enter "quit", and count the vowels in each line|for inside while|Number of lines unknown; each line is a string to walk through|


## Types and objects
### *Polygon*
```python
class Polygon:
    pass

polygons = []
for i in range(4):
    polygon = Polygon()
    polygon.sides = int(input("How many sides in this polygon? "))
    polygon.length = int(input("How long are each of the sides? "))
    polygons.append(polygon)

for polygon in polygons:
    print("This polygon has " + str(polygon.sides) + " and the length is " + str(polygon.length))
```
### *Cars*
```python
 class Person:
    pass

class Car:
    pass

me = Person()
me.name = "Farrell Edwards"
me.pet = "Pepper"

car1 = Car()
car1.model = "Nissan"
car1.year = 2020

me.car1 = car1

# Do car2

# Switch to list but car1, car2
# Keep on list but reuse variable
# Do in loop
# Enter "Opel" when done
```

## Summary (write after class)
*3–5 bullet points you'd want to remember a week from now.*

- 
- 
- 
