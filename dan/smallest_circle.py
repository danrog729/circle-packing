from random import shuffle
from math import sqrt

def create_from_diameter(point1, point2):
    centre = ((point1[0] + point2[0])/2, (point1[1] + point2[1])/2)
    diameter = sqrt( (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 )
    return (centre, diameter)

def create_circumcircle(point1, point2, point3):
    # this looks like black magic because i copied it from somewhere :)
    # https://stackoverflow.com/questions/56224824/how-do-i-find-the-circumcenter-of-the-triangle-using-python-without-external-lib
    ax = point1[0]
    ay = point1[1]
    bx = point2[0]
    by = point2[1]
    cx = point3[0]
    cy = point3[1]
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    radius = sqrt( (ux-ax)**2 + (uy-ay)**2 )
    return ((ux, uy), radius*2)

def in_circle(circle, point):
    centre = circle[0]
    radius = circle[1] / 2
    if ((point[0] - centre[0])**2 + (point[1] - centre[1])**2 <= radius**2):
        return True
    else:
        return False

def min_bounding_circle(points, begin, end, usePin1, usePin2, pin1, pin2):
    # uses this algorithm https://youtu.be/HojzdCICjmQ?si=wuTMoSPXpYmu_-JG
    current = begin
    circle = ((0,0),0)
    if (usePin1 and usePin2):
        circle = create_from_diameter(points[pin1], points[pin2])
        # print("NEW CIRCLE FROM DIAMETER, USING PIN 1 AND 2: PIN 1 = " + str(pin1) + ", PIN 2 = " + str(pin2))
        # print("CENTRE = (" + str(circle[0][0]) + ", " + str(circle[0][1]) + ")")
        # print("DIAMETER = " + str(circle[1]))
    elif (usePin1):
        current += 1
        circle = create_from_diameter(points[pin1], points[current])
        # print("NEW CIRCLE FROM DIAMETER, USING PIN 1: PIN 1 = " + str(pin1))
        # print("CENTRE = (" + str(circle[0][0]) + ", " + str(circle[0][1]) + ")")
        # print("DIAMETER = " + str(circle[1]))
    else:
        circle = create_from_diameter(points[current], points[current+1])
        # print("NEW CIRCLE FROM DIAMETER, USING NO PINS")
        # print("CENTRE = (" + str(circle[0][0]) + ", " + str(circle[0][1]) + ")")
        # print("DIAMETER = " + str(circle[1]))
        current += 2

    while (current != end):
        if (not in_circle(circle, points[current])):
            if (usePin1 and usePin2):
                circle = create_circumcircle(points[pin1], points[pin2], points[current])
                # print("NEW CIRCLE FROM CIRCUMCIRCLE, USING PIN 1 and 2: PIN 1 = " + str(pin1) + ", PIN 2 = " + str(pin2))
                # print("CENTRE = (" + str(circle[0][0]) + ", " + str(circle[0][1]) + ")")
                # print("DIAMETER = " + str(circle[1]))
            elif (usePin1):
                circle = min_bounding_circle(points, begin, current, True, True, pin1, current)
                # print("NEW CIRCLE FROM RECURSION, USING PIN 1: PIN 1 = " + str(pin1))
                # print("CENTRE = (" + str(circle[0][0]) + ", " + str(circle[0][1]) + ")")
                # print("DIAMETER = " + str(circle[1]))
            else:
                circle = min_bounding_circle(points, begin, current, True, False, current, (0,0))
                # print("NEW CIRCLE FROM RECURSION, USING NO PINS")
                # print("CENTRE = (" + str(circle[0][0]) + ", " + str(circle[0][1]) + ")")
                # print("DIAMETER = " + str(circle[1]))
        current += 1
    return circle

def calculate_bounding_circle(points):
    # uses this algorithm https://youtu.be/HojzdCICjmQ?si=wuTMoSPXpYmu_-JG
    centre = (0,0)
    radius = 0

    shuffle(points) # slightly increases speed as if the points are ordered in such a way that they're radiating from the centre then its a worst case, shuffling it avoids this
    # print(points)

    circle = min_bounding_circle(points, 0, len(points)-1, False, False, (0,0), (0,0))

    return circle