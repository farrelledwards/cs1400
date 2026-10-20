
while True:
    age = input("What's your age?  ")
    if not age.isdigit():
        print("Please enter your age as a number.")
        continue
    age_num = int(age)
    if age_num >= 0 and age_num <= 120:
        break
    print("That's not a good age")

print("Good age:  " + str(age_num))