# Lecture: Functions

**Class:** CS 1400
**Date:** Oct. 27, 2026
**Modules:** 4.2

---

## Why do we use functions:
- Reuse
  - Polygon
- Organize
- Simplify

```python
print("--- ORDER ---")
print("Customer: Maria")
print("Size: large")
print("Number: 3")
print("Topping: pepperoni")
print("Thanks for ordering 3 pizzas, Maria!")

print("--- ORDER ---")
print("Customer: Devon")
print("Size: small")
print("Number: 2")
print("Topping: mushroom")
print("Thanks for ordering 2 pizzas, Devon!")

print("--- ORDER ---")
print("Customer: Priya")
print("Size: medium")
print("Number: 20")
print("Topping: olives")
print("Thanks for ordering 20 pizzas, Priya!")
```

## Void function

In python -- None

## Positional arguments

- Same number of arguments
- Same order
- Compatible type

## Keyword

```python
    info(name=my_name, age=my_age, food=my_food)
```

- Can change order
- Can use positional and keyword
- Can't do positional before keyword

## Default value

```python
def info(name, age=30, food="ramen"):
    print(name + " is " + str(age) + " years old and likes to eat " + food)
```

***Use default age but actual food***

