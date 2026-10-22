# Lecture: Debugging

**Class:** CS 1400
**Date:** Oct. 22, 2026
**Modules:** 4.1

---

## Main hits
- Activation record / Stack frame
- Global variable
- Show variables inside functions unavailable
- Inadvertantly global
- Protect with main
- Protect with main (more complicated)
- Walk through refactoring


## Main

### Activation record / stack frame / global frame

```python
def square(n):
    result = n * n
    return result

def sum_of_squares(limit):
    total = 0
    i = 1
    while i <= limit:
        total = total + square(i)
        i = i + 1
    return total

start = 4
answer = sum_of_squares(start)
print("Sum of squares up to", start, "is", answer)
start = 6
answer = sum_of_squares(start)
print("Sum of squares up to", start, "is", answer)
```

### Global scope

```python
val = 4
def double():
    result = val * 2
    return result

print(double())
```

### Local scope (and only local)
```python
def double(n):
    result = n * 2
    return result

print(double(4))
print(result)
```

### Another kind of Global

```python
def double(n):
    result = val * 2
    return result

val = 10
print(double(val))
print(double(4))
```

### Use main to protect

```python
def double(n):
    result = val * 2
    return result

def main():
    val = 10
    print(double(val))
    print(double(4))
    
main()
```

### More complicated (with bug)

```python
def square(n):
    result = n * n
    return result

def sum_of_squares(limit):
    total = 0
    i = 1
    while i <= start:
        total = total + square(i)
        i = i + 1
    return total

start = 4
answer = sum_of_squares(start)
print("Sum of squares up to", start, "is", answer)

answer = sum_of_squares(10)
print("Sum of squares up to", 10, "is", answer)
```

### Refactor

```python
print("Making a sandwich...")
print("two slices of toast")
print("Put filling between", bread)
```

```python
def make_sandwich():
    print("Making a sandwich...")
    bread = get_bread()
    print("Put filling between", bread)

def get_bread():
    return "two slices of toast"

def main():
    make_sandwich()
    
main()
```

```python
def main(): # bottom and top
    make_sandwich()

main()
```

### Slightly more complicated

```python
def print_receipt(item, quantity):
    subtotal = get_price(item) * quantity
    total = add_tax(subtotal)
    print(quantity, item + "(s):", "$" + str(total))

def get_price(item):
    if item == "latte":
        return 4.00
    if item == "muffin":
        return 2.50
    return 0.00

def add_tax(amount):
    return round(amount * 1.07, 2)

print_receipt("latte", 2)
print_receipt("muffin", 3)
```

**Then switch to using main for the receipts.**

## Debugging
- Break at top
- Step over
- Inspect
- Continue
- Other breakpoints
- Step in
- Step out

```python
print("This is our debugging program")

def double(n):
    result = n * 2
    return result

count = 1
while count < 5:
    print(double(count))
    count += 1
    
print("Thanks for playing")
```

**Switch to while**

```python
while True:
    value = int(input("Please give me a number to double (-1 to quit): "))
    if value == -1:
        break
    print(double(value))
    
print("Thanks for playing")
```

### More complicated and buggy:

```python
print("Show the sum of the squares for a particular number")

def square(n):
    result = n * 2
    return result

def sum_of_squares(limit):
    total = 0
    i = 1
    while i < start:
        total = total + square(i)
        i = i + 1
    return total

start = 3
answer = sum_of_squares(start)
print("Sum of squares up to", start, "is", answer)

answer = sum_of_squares(10)
print("Sum of squares up to 10 is", answer)
```
