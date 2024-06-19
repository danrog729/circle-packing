import math
def pythagoras(a,b):
    x=abs(a[0]-b[0])
    y=abs(a[1]-b[1])
    hypotenuse = math.sqrt(x**2+y**2)
    return hypotenuse
    
def fine_test(a,b):
    hypotenuse=pythagoras(a,b)
    if hypotenuse < 1 and hypotenuse != 0:
        Invalid=True
    else:
        Invalid=False
    return(Invalid)

def valid_solution(coordinates):
    Valid=True
    length=len(coordinates)
    for Loop1 in range(length):
        for Loop2 in range(length):
            if abs(coordinates[Loop2][0]-coordinates[Loop1][0]) < 1 and abs(coordinates[Loop2][1]-coordinates[Loop1][1]) < 1:
                Invalid = fine_test(coordinates[Loop1],coordinates[Loop2])
            if Invalid:
                Valid=False
    return Valid

def smallest_circle(coordinates):
    greatest = 0
    length=len(coordinates)
    for Loop in range(length):
        hypotenuse=pythagoras(coordinates[Loop],[0,0])
        if hypotenuse>greatest:
            greatest=hypotenuse
    radius=greatest+1
    return radius


def checksolution(coordinates):
    valid=valid_solution(coordinates)
    radius=smallest_circle(coordinates)
    diameter=2*radius
    return valid,diameter

coordinates=[[1,0],[-1,0],[2,3]]
valid,diameter=checksolution(coordinates)
print(valid)
print(diameter)


            