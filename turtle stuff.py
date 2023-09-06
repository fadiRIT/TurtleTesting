#Turtle is a basic python program which can be used to draw

# it responds to bSic commands, such as up, to lfit the pen up, and down, to put it down. turtle.up()
# There's also left or right to rotate an amount of degrees, forward to move in the direction its facing a certain distance. turtle.left(90)
# Home to move to the origin, which is 0,0 by default. turtle.home()
# setheading can be used to rotate the turtle to a specific angle. turtle.setheading(180)
# a circle to tell the turtle to draw a circle to its left, not your left.




import turtle as t

def testdrive():
    t.forward(100)
    t.left(87)
    t.setheading(127)

    t.delay(60)
    t.up()

    t.down()
    t.circle(80)
    t.goto(50,50)
    t.home()

testdrive()

