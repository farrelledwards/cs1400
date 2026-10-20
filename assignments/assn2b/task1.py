from random import randint

print("Welcome to the guessing game")
print("Computer picked number")

correct = randint(1, 10)

guess = int(input("Enter your guess (1-10): "))

diff = abs(guess - correct)

if diff == 0:
    print("Honored to play with you, True Aggie")
elif diff == 1:
    print("You are a worthy opponent, Big Blue")
elif diff == 2:
    print("You have much to learn, Hurd")
elif diff == 3:
    print("Little Blue, your time will come")
else:
    print("Keep working hard on the Quad")
