from math import tan, pi
import math

lengths = []
num_sides = []
areas = []

for i in range(4):
    lengths.append(float(input("Give the the length of polygon " + str(i+1) + ": ")))
    num_sides.append(int(input("Give the number of sides of polygon " + str(i+1) + ": ")))
    areas.append((num_sides[i]*math.pow(lengths[i], 2)) / (4 * tan(pi/num_sides[i])))

for i in range(4):
    print("The area of polygon " + str(i) + ": " + str(round(areas[i], 5)))
