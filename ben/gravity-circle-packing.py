import math

import random

def pythagoras(a,b):
    '''
    Gives the distance from the origin of a point
    '''
    # Calculate hypotenuse using pythagoras
    hypotenuse=math.sqrt(a**2+b**2)
    return hypotenuse

def convertcart(polarcoordinates):
    '''
    Converts from polar coordinates to cartesian coordinates
    '''

    # Builds a list of the values generated
    cartcoords=[]
    for points in range(len(polarcoordinates)):
        # Calculates coordinates using trigonometry
        x=polarcoordinates[points][0]*math.cos(math.radians(polarcoordinates[points][1]))
        y=polarcoordinates[points][0]*math.sin(math.radians(polarcoordinates[points][1]))
        cartcoords+=[[x,y]]
    return cartcoords

def convertpol(cartcoords):
    '''
    Converts from cartesian coordinates to polar coordinates
    '''

    # Builds a list of the values generated
    polcoords=[]
    for points in range(len(cartcoords)):

        # Calculates coordinates using trigonometry
        displacement=pythagoras(cartcoords[points][0],cartcoords[points][1])
        try:
            angle=math.degrees(math.atan(cartcoords[points][1]/cartcoords[points][0]))
            if cartcoords[points][0]<0:
                angle=angle+180
        except:
            if cartcoords[points][0]==0:
                angle=90
        polcoords+=[[displacement,angle]]

    return polcoords
    
def generatepoints(number):
    '''
    Generates specified numbers of circles in random coordinates
    '''
    coordsofcircles=[]

    # Iterates for how many circles
    for point in range(number):

        # Generates circle coordinates at random locations
        xcoord=random.randint(-number*5,number*5)
        ycoord=random.randint(-number*5,number*5)
        coordsofcircles+=[[xcoord,ycoord]]
    return coordsofcircles

def test(polcoords,circle1,circle2):
    cartcoords=convertcart(polcoords)
    x=abs(cartcoords[circle1][0]-cartcoords[circle2][0])
    y=abs(cartcoords[circle1][1]-cartcoords[circle2][1])
    hypotenuse=pythagoras(x,y)
    if hypotenuse<1:
        clipped=True
    else:
        clipped=False
    return clipped

def findclipped(polcoords):
    '''
    analyses which circles are clipped into each other after cycle
    '''
    swapmade=True
    while swapmade==True:
        swapmade=False
        for circle1 in range(len(polcoords)):
            for circle2 in range(len(polcoords)):
                if circle1 != circle2:
                    clipped=test(polcoords,circle1,circle2)
                    if clipped:
                        #if they are clipped they are unclipped and this carries on for every other circle
                        polcoords=unclip(polcoords,circle1,circle2)
                        swapmade=True
    return polcoords                  

def unclip(polcoords,circle1,circle2):
    
    '''
    unclips all circles which are clipped together by moving them in a spiral shape
    '''
    oppositeside=0.5
    while oppositeside<1.1:
        #moves circle 2 outwards in a spiral pattern and checks if still clipped
        polcoords[circle1][0]+=0.2
        polcoords[circle1][1]+=3
        angle=polcoords[circle1][1]-polcoords[circle2][1]
        oppositeside=math.sqrt(polcoords[circle1][0]**2+polcoords[circle2][0]**2+polcoords[circle1][0]*polcoords[circle2][0]*2*math.cos(math.radians(angle)))
    return polcoords

def applygravity(polcoords):
    '''
    pulls all circles in towards the origin
    '''

    # Iterates through coordinates and pulls them all towards the origin
    for points in range(len(polcoords)):
        polcoords[points]=[(polcoords[points][0])/random.uniform(1.3,1.7),polcoords[points][1]]
    return polcoords

def desmos(coordinates):
    '''
    converts coordinates form 2d array form into an xtable and ytable so desmos can read it
    '''
    xtable=[]
    ytable=[]

    # Iterates through coordinates and builds separates two parts to form x and y tables
    for point in range(len(coordinates)):
        xtable+=[round(coordinates[point][0],5)]
        ytable+=[round(coordinates[point][1],5)]
    
    # Prints both tables to be inputted into desmos
    print(xtable)
    print(ytable)
    

numberofcircles=int(input("Enter number of circles"))
coordinates=generatepoints(numberofcircles)
coordinates=convertpol(coordinates)
for Loop in range(10000):
    coordinates=applygravity(coordinates)
    coordinates=findclipped(coordinates)
coordinates=convertcart(coordinates)
desmos(coordinates)
    

