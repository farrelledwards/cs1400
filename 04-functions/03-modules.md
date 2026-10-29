# Lecture: Modules

**Class:** CS 1400
**Date:** Oct. 29, 2026
**Modules:** 4.3

## Modules

### Gradebook.py

```python
# gradebook.py -- everything in one file

def average(scores):
    """Return the average of a list of numbers."""
    return sum(scores) / len(scores)


def letter_grade(avg):
    """Convert a numeric average to a letter grade."""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    return "F"


def format_report(name, scores):
    """Build one line of text summarizing a student."""
    avg = average(scores)
    return f"{name}: average {avg:.1f} -> {letter_grade(avg)}"


def main():
    student_names = ["Ada", "Grace", "Linus", "Mork"]
    student_scores = [[95, 88, 92, 89], [72, 85, 78, 81], [55, 62, 48, 0], [25, 53, 68, 81]]

    for i in range(4):
        print(format_report(student_names[i], student_scores[i]))

main()
```

### Modules
- What is a module
- Why modules
-- Readability
-- One place to fix
-- Reuse
-- Teamwork


### Steps

- Move grading (average, letter_grade) to module
```python
import grades
from grades import average
```

- Add a student class

## Pass by value / stack / memory

### Basic

```python
def callout(val):
    print(val)
    val += 1
    print(val)
    
val = 5
print(val)
```

### List

```python
def callout(val):
    print(val)
    val.append(1)
    print(val)
    
val = [5]
print(val)
```

### User defined type (class)

```python
class Person:
    pass
    
def callout(student):
    print(student.name)
    student.name = "Farrell"
    print(student.name)
    
student = Person()
student.name = "Pepper"
callout(student)
print(student.name)
```

## Variable scope

- Local variables
- Global variables

## Watch 4.4 Super Target Demo
