class Polygon:
    pass

polygons = []
for i in range(4):
    polygon = Polygon()
    polygon.sides = int(input("How many sides in this polygon? "))
    polygon.length = int(input("How long are each of the sides? "))
    polygons.append(polygon)

for polygon in polygons:
    print("This polygon has " + str(polygon.sides) + " and the length is " + str(polygon.length))
