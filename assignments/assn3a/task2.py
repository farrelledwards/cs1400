
class Animal:
    pass

animals = []
count = 0

for i in range(3):
    animal = Animal()
    animal.type = input("\tWhat was the type of animal number " + int(i+1) + " that you saw: ")
    animal.count = int(input("\tHow many of them did you see? "))
    count += animal.count
    animal.sound = input("\tAnd what did they say? ")
    animals.append(animal)

input("\nPutting the animals in the animalinator")

print("Total number of animals:", count)
print("They were ", end="")
for animal in animals:
    print(animal + "s")