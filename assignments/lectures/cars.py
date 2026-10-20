
class Person:
    pass

class Car:
    pass

me = Person()
me.name = "Farrell"
me.dog_name = "Pepper"
me.cars = []

while True:
    car = Car()
    car.make = input("Enter the make: ")
    if car.make == "Opel":
        break
    car.model = input("Enter the model: ")
    me.cars.append(car)

for car in me.cars:
    print("Car: " + car.make)