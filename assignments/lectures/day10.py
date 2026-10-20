# PSA
# Hello [name].  At [degrees] degrees, you should [do something]

name = input("What is your name? ")
temperature = int(input("What are the degrees? "))

output_str = "PSA\nHello " + name + ".  At " + str(temperature) + " degrees, you should "

if temperature < 30:
    output_str += "wear a coat"
elif temperature < 50:
    output_str += "wear a sweater"
elif temperature < 70:
    output_str += "wear shorts"
else:
    output_str += "enjoy the day"

print(output_str)
