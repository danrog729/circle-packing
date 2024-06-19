from random import random
import smallest_circle

points = []
for point in range(0,100,1):
    points.append((random(),random()))

circle = smallest_circle.calculate_bounding_circle(points)
print("RESULT:")
print("CENTRE = (" + str(circle[0][0]) + ", " + str(circle[0][1]) + ")")
print("DIAMETER = " + str(circle[1]))