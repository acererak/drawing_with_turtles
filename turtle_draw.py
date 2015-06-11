#   Name:  Zak Garriss

from math import sin, asin, cos, sqrt, pi
from TurtleWorld import *

def square(turtle,length):
    """ instructs a turtle to draw a square """
    turtle.pd()
    for i in range(4):
        turtle.fd(length)
        turtle.lt(90)
    turtle.pu()

###############################################################################
# Exercise 1
#
# This procedure takes a turtle and a length and produces a hexagon accordingly.
#

def hexagon(turtle,length):

    turtle.pd()

    for i in range(6):

        turtle.fd(length)
        turtle.lt(60)

    turtle.pu()

###############################################################################
# Exercise 2
#
# For this exercise, I am fixing the code in the grid() provided.
# The new function successfully creates a grid of given shapes
# with given dimensions.

def grid(turtle,shape,rows,columns,size,spacing):
    """ instructs a turtle to draw a grid of shapes """
    for i in range(rows):
        
        for j in range(columns):
            shape(turtle,size)
            turtle.fd(spacing)
        
        turtle.rt(90)
        turtle.fd(spacing)
        turtle.rt(90)

        for j in range(columns):
            turtle.fd(spacing)

        turtle.rt(180)

###############################################################################
# Exercise 3
#
# This is a generalized polygon solution that uses a curried function
# to return a dynamically generated polygon procedure using only
# the value (n) as the number of sides the polygon is to have.
#

def polygon_maker(n):

    def polygon(turtle,length):

        turtle.pd()

        for i in range(n):

            turtle.fd(length)
            turtle.lt(360/n)

        turtle.pu()

    return polygon


square = polygon_maker(4)
hexagon = polygon_maker(6)
decahedron = polygon_maker(12)
hechahedron = polygon_maker(100)

###############################################################################
# Exercise 4
#
# This procedure generates a function for drawing an n-sided star.
#

def star_maker(n):

    def star(turtle,length):

        turtle.pd()

        for i in range(n):

            turtle.rt(180-(360/n))
            turtle.fd(length)
            turtle.lt(180-(720/n))
            turtle.fd(length)

        turtle.pu()

    return star

sixer = star_maker(6)
thricer = star_maker(3)
niner = star_maker(9)
center = star_maker(100)
fourer = star_maker(4)

###############################################################################
# Exercise 5
#
# This procedure instructs sven the turtle to draw a circle
# of a given radius.
#

def circle(turtle,radius):


# sketch out some code
# we're given r, and to make a circle, we need to generate n number of ls.

    # let's start by saying arbitrarily that n will be equal to r. This
    # will result in the number of polygons increasing as the radius increases.
    n = radius

    # some trig magic. a == angle determined by n.
    a = (2*pi)/n
    l = 2 * (radius * sin(a/2))

    turtle.fd(radius)
    turtle.pd()
    turtle.lt(90)

    for i in range(n):

        turtle.fd(l)
        turtle.lt(360/n)

    turtle.lt(90)
    turtle.pu()
    turtle.fd(radius)
    turtle.lt(180)

###############################################################################
# Exercise 6 BONUS
#
# This procedure draws a really cool arc.
#

def right_arc(turtle,radius,length):

    # let's start by saying arbitrarily that n will be equal to r. This
    # will result in the number of polygons increasing as the radius increases.
    n = radius

    # some trig magic. a == angle determined by n.
    a = (2*pi)/n
    l = 2 * (radius * sin(a/2))

    turtle.fd(radius)
    turtle.pd()
    turtle.lt(90)

    #####################################################
    # above code borrowed from (my own) def circle above, and uses
    # the for loop below. In this space between, adding code
    # to carve an arc.

    # what I want to do now is use radius and length to determine the angle
    # formed at the point in the center of the circle where they meet.
    # this angle tells me what fraction of the circle I then want to draw.

    # using inverse sine with length and radius as opp/hyp:
    m = asin((length/2)/radius)

    # note: that returns radians. Now I want to double it (because I only looked
    # at half the length to form a 90* angel above)

    m = 2 * m

    # and now I want to take the fraction of 2pi that represents
    # and apply that fraction to the range of circle painting
    # that occurs below

    m = m / (2 * pi)

    # note on this solution: length must be less than 2 x the radius.

    ######################################################

    for i in range(int(n*m)):

        turtle.fd(l)
        turtle.lt(360/n)

    turtle.lt(90)
    turtle.pu()
    turtle.fd(radius)
    turtle.lt(180)

    turtle.pu()

###############################################################################
# Exercise 7 BONUS
#
# This bad ass function creates a flower with n petals.
#

def flowerPower(turtle,length,number):

    # let's start by saying arbitrarily that 'n' will be equal to r, which
    # (unlike the function above) will also be equal to length. This
    # should result in a constant size of petals.
    n = length

    # arbitrarily assigning the radius of the subsected circle a radius of l.
    radius = length

    # some trig magic. a == angle determined by n.
    a = (2*pi)/n
    l = 2 * (radius * sin(a/2))

    turtle.pd()

    #####################################################
    # above code borrowed from (my own) def circle above, and uses
    # the for loop below. In this space between, adding code
    # to carve an arc.

    # what I want to do now is use radius and length to determine the angle
    # formed at the point in the center of the circle where they meet.
    # this angle tells me what fraction of the circle I then want to draw.

    # using inverse sine with length and radius as opp/hyp:
    m = asin((length/2)/radius)

    # note: that returns radians. Now I want to double it (because I only looked
    # at half the length to form a 90* angel above)

    m = 2 * m

    # and now I want to take the fraction of 2pi that represents
    # and apply that fraction to the range of circle painting
    # that occurs below

    m = m / (2 * pi)

    ######################################################

    for i in range(number):

        # choosing starting angle out...
        turtle.rt(30)

        # first arc
        for i in range(int(n*m)):

            turtle.fd(l)
            turtle.lt(360/n)

        # ...so I can choose a corresponding angle back.
        turtle.lt(120)

        # second arc
        for i in range(int(n*m)):

            turtle.fd(l)
            turtle.lt(360/n)

        turtle.rt(210)

        turtle.rt(360/number)
https://github.com/acererak/drawing_with_turtles
    turtle.pu()

###############################################################################
# Exercise 8
#
# The legendary koch snowflake.
#

def snowflake(turtle,n,l):

    turtle.pd()


    # ok, so I definitely need a helper function to do the work
    # of constructing one of the three legs. Each iteration of the
    # snowflake will be of variable complexity, but all versions
    # will have only three faces. I'll put the work of recursively
    # constructing increasingly complex versions of only one of the 
    # faces here, then rotate and do it again, two more times below.
    def snowflakeHelper(turtle,n,l):

        # base case
        if n == 0:

            turtle.fd(l)

        # call it again with increasingly tinier legs
        else:

            snowflakeHelper(turtle,n-1,l/3)
            turtle.lt(60)
            snowflakeHelper(turtle,n-1,l/3)
            turtle.rt(120)
            snowflakeHelper(turtle,n-1,l/3)
            turtle.lt(60)
            snowflakeHelper(turtle,n-1,l/3)

    # and here, do the work of building three faces total with 120
    # degree hinges
    for i in range(3):

        snowflakeHelper(turtle,n,l)
        turtle.rt(120)







#################################################################################
# Test Cases
# initialize a world with a turtle named Sven
world = TurtleWorld()
sven = Turtle()

# set up Sven's status and location
sven.delay = 0.01
sven.pu()
# sven.lt(180)
# sven.fd(100)
# sven.lt(180)

# Exercise 1 [Hexagon]
# hexagon(sven,100)

# draw a square
# square(sven,25)

# Exercise 2
# draw a grid of squares
# grid(sven,square,3,5,10,25)

# Exercise 3
# decahedron(sven,50)
# hechahedron(sven,50)

# Exercise 4
# sixer(sven,50)
# niner(sven, 50)
# sixer(sven,50)
# center(sven,50)

# Exercise 5
# circle(sven,100)
# circle(sven,5)
# circle(sven,50)

# Exercise 6 BONUS
# right_arc(sven,150,160)

# Exercise 7 BONUS
# flowerPower(sven,100,25)

# Exercise 8 BONUS
snowflake(sven,4,300)

input('Hit [RETURN] to exit.\n')

