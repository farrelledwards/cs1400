import drawly

def print_order(name, topping, number=1, size="Large"):
    print("--- ORDER ---")
    print("Customer: " + name)
    print("Size: " + size)
    print("Number: " + str(number))
    print("Topping: " + topping)
    print("Thanks for ordering " + str(number) + " " + size + " " + topping + " pizzas, " + name + "!")

def main():
    farrells_little_dog = "Pepper"
    drawly.start()
    print_order("Maria", topping="pepperoni")
#    print_order("Devon", "Small", 2, "mushroom")
#    print_order("Priya", "Medium", 20, "asbestos")
    print(farrells_little_dog)

