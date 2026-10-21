import random

def sum(x, y):
    if (x > y):
        return x + y
    return x - y

print(sum(1, 2))

def ave(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

class_grades = [98, 23, 63, 56]
print("The class average is: " + str(ave(class_grades)))

animal_suffix = "joe"

# randomly shuffle a word
def word_shuffle(word, append_str):
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list) + append_str


print(word_shuffle("alligator", animal_suffix))
