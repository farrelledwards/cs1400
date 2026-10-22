print("Show the sum of the squares for a particular number")

def square(n):
    result = n * 2
    return result

def sum_of_squares(limit):
    total = 0
    i = 1
    while i < limit:
        total = total + square(i)
        i = i + 1
    return total

start = 3
answer = sum_of_squares(start)
print("Sum of squares up to", start, "is", answer)
start = 4
answer = sum_of_squares(start)
print("Sum of squares up to", start, "is", answer)
