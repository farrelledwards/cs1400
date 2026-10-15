---
# try also 'default' to start simple
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: Computer Science 1400
# apply UnoCSS classes to the current slide
class: text-center
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# https://sli.dev/features/drawing
drawings:
  persist: false
---

# Order of operations
# if-elif-else
# more... :)

---
layout: default
---

# Status

| Date | What |
|-----------|-----------|
| Oct 2 (Fri) | Exercises 2.1.2, 2.1.3, 2.2.3(a/b), 2.3.1 <br> Quizzes 2.1, 2.2, 2.3 |
| Oct 3 (Sat) | Assignment 1b Code Review |
| Oct 4 (Sun) | Assignment 2a - Investments & Polygon Area <br> Reflection |
| Oct 5 (Mon) | Exercises 2.5.2, 2.6.1, 2.6.3, 2.6.5 <br> Quizzes 2.4, 2.5, 2.6 |

---
layout: default
---

# Status-b

| Date | What |
|-----------|-----------|
| Oct 8 (Thurs) | No class |
| Oct 8 | Assignment 2a code review due |
| Oct 9 (Fri) | Exercises (3.1.1, 3.1.3, 3.1.5, 3.1.6, 3.2.1-a/b) <br> Quizzes (3.1, 3.2, 3.3) | 
| Oct 9-10 | Coaching Center closed |
| Oct 11 (Sun) | Assignment 2b |

---
layout: default
---

# Status-c

| Date | What |
|-----------|-----------|
| Oct 23 | Midterm (Units 1-3) |


---
layout: default
---

# Order of operations (python)

| Expression |
|----------|
| ```8 + 4 + 3``` |
| ```2 * 7 * 5``` |
| ```2 + 3 * 4``` |
| ```100 / 10 * 2``` |
| ```-3 ** 2``` |
| ```2 ** 3 ** 2``` |
| ```2 + 3 ** 2 * 4 - 1``` |

---
layout: default
---

# Order of operations (python)

| Level | Operators | Description |
|---|---|---|
| 1 | `(expr...)`, `[expr...]`, `{key: value...}`, `{expr...}` | Parenthesized expressions, list/dict/set displays |
| 2 | `x[i]`, `x[i:j]`, `x(...)`, `x.attr` | Subscription, slicing, call, attribute reference |
| 3 | `await x` | Await expression |
| 4 | `**` | Exponentiation (right-associative) |
| 5 | `+x`, `-x`, `~x` | Unary plus, minus, bitwise NOT |
| 6 | `*`, `@`, `/`, `//`, `%` | Multiplication, matrix multiplication, division, floor division, remainder |

---
layout: default
---

# Order of operations (python)

| Level | Operators | Description |
|---|---|---|
| 7 | `+`, `-` | Addition, subtraction |
| 8 | `<<`, `>>` | Bitwise shifts |
| 9 | `&` | Bitwise AND |
| 10 | `^` | Bitwise XOR |
| 11 | `\|` | Bitwise OR |
| 12 | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Membership, identity, comparisons (these chain) |

---
layout: default
---

# Order of operations (python)

| Level | Operators | Description |
|---|---|---|
| 13 | `not x` | Boolean NOT |
| 14 | `and` | Boolean AND |
| 15 | `or` | Boolean OR |
| 16 | `x if cond else y` | Conditional expression (ternary) |
| 17 | `lambda` | Lambda expression |
| 18 | `:=` | Assignment expression (walrus) |


---
layout: default
---

# Order of operations (python)

## Notes

- Operators at the same level group left to right, except `**`, which groups right to left (`2 ** 3 ** 2` is `2 ** 9`, or 512).
- `**` binds tighter than a unary operator on its left, so `-2 ** 2` is `-4`. On its right it binds looser, so `2 ** -1` is `0.5`.
- Comparisons share one level and chain: `1 < x < 10` means `1 < x and x < 10`, with `x` evaluated once.
- Bitwise operators bind tighter than comparisons in Python, unlike C, so `a & b == c` means `(a & b) == c`.
- When mixing less common operators, add parentheses for clarity.

---
layout: default
---

# Order of operations (python)

| Expression |
|----------|
| ```2 + 3 * 4``` |
| ```100 / 10 * 2``` |
| ```-3 ** 2``` |
| ```2 ** 3 ** 2``` |
| ```2 + 3 ** 2 * 4 - 1``` |

---
layout: default
---

# Order of operations (python)

| Expression | Actual |
|----------|-----------|
| ```2 + 3 * 4``` | *14* |
| ```100 / 10 * 2``` | *20* |
| ```-3 ** 2``` | *-9* |
| ```2 ** 3 ** 2``` | *512*|
| ```2 + 3 ** 2 * 4 - 1``` | *37* |

---
layout: default
---

# Order of operations (python)

| Expression | Readable |
|----------|-----------|
| ```2 + 3 * 4``` |  ```2 + (3 * 4)``` |
| ```100 / 10 * 2``` | ```(100 / 10) * 2``` |
| ```-3 ** 2``` | ```-(3 ** 2)``` |
| ```2 ** 3 ** 2``` | ```2 ** (3 ** 2)``` |
| ```2 + 3 ** 2 * 4 - 1``` | ```2 + ((3 ** 2) * 4) - 1)``` |

---
layout: default
---

# Watch Farrell type

---
layout: default
---

# Dangling else

```
is_raining = False
have_umbrella = False

if is_raining:
    if have_umbrella:
        print("Walk to school.")
else:
    print("Take the bus.")
```

---
layout: default
---

# Correct

```
is_raining = False
have_umbrella = False

if is_raining:
    if have_umbrella:
        print("Walk to school.")
    else:
        print("Take the bus.")
else:
    print("Walk to school.")
```
