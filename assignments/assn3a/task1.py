print("Welcome message Fronkian Calendar")

year = int(input("\tWe're going to calculate.  Give me a 4 digit year: "))

print_str = "\nThis is the result"

remainder_9 = year % 9
centuries = year // 100
two_digit_year = year % 100
third_digit = two_digit_year // 10
fourth_digit = two_digit_year % 10


if remainder_9 == 0 and third_digit != fourth_digit:
    print_str += "\n\t" + str(year) + " is a leap year in the fronkian calendar"
elif third_digit + fourth_digit == centuries and third_digit % 2 == 0 and third_digit < fourth_digit:
    print_str += "\n\t" + str(year) + " is a leap year in the fronkian calendar"
else:
    print_str += "\n\t" + str(year) + " is not a leap year in the fronkian calendar"

print(print_str)
