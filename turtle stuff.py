#Turtle is a basic python program which can be used to draw

# it responds to bSic commands, such as up, to lfit the pen up, and down, to put it down. turtle.up()
# There's also left or right to rotate an amount of degrees, forward to move in the direction its facing a certain distance. turtle.left(90)
# Home to move to the origin, which is 0,0 by default. turtle.home()
# setheading can be used to rotate the turtle to a specific angle. turtle.setheading(180)
# a circle to tell the turtle to draw a circle to its left, not your left.
# turtle_state prints the current state of the turtle.
# turtle.isdown() prints true if pen is down, and false if its up
# turtle.heading( returns the current angle of orientatio nof the turtle
# turtle.xcor(), turtle.ycor() return x and y coordinates of the turtle



import turtle as t

def testdrive():
    t.forward(100)
    t.left(87)
    t.setheading(127)

    t.delay(20)
    t.up()
    
    t.down()
    t.goto(50,50)
    t.home()
    t.circle(25)

def turtle_state():
    updown = t.isdown()
    heading = t.heading()
    xcor = t.xcor()
    ycor = t.ycor()
    print("Pen Status :",updown,"\nHeading :",heading, "\nThe coordinates are\nX:",xcor,"\nY:",ycor)

def square():
    t.up()
    t.goto(100,100)
    t.down()
    t.forward(90)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(90)

def main():
    testdrive()
    square()
    turtle_state()
    input("Press enter to continue . . .")

main()

