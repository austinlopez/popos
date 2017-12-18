#first do this in the terminal
#sudo apt install python3-tk

#module for turtle drawing
import turtle
import random

#makes a pen turtle
myTurtle = turtle.Pen()

#moves it forward 100 pixels
#default start is moving east/right
myTurtle.forward(100)

#turn the turtle to the right (clockwise)
myTurtle.right(90)
myTurtle.forward(100)

#can also turn left (counter-clockwise)
myTurtle.left(180)
myTurtle.forward(200)
#the turtle can move backward
myTurtle.backward(400)
#the turtle can move without drawing
myTurtle.penup()
myTurtle.left(45)
myTurtle.forward(300)

#you must put the pen down again to start drawing
#try to guess what this one will be
myTurtle.pendown() #did you guess right?
#you can change colors
#it needs a string for the name
#there are a bunch of colors you can use
myTurtle.color('red')
myTurtle.right(90)
myTurtle.forward(200)

#input("press a button to close the window:")

myTurtle.reset() #everything resets to defaults

#ets change the background color

myTurtle.getscreen().bgcolor('black')
#better change the turtle color also (remember it reset)
myTurtle.color('white')
myTurtle.speed(0)

#now lets make our loop
# for pos in range(360):
#     myTurtle.forward(pos)
#     myTurtle.right(90)

def square(size):
    myTurtle.pendown()
    myTurtle.fillcolor('red')
    myTurtle.forward(size)
    myTurtle.right(90)
    myTurtle.forward(size)
    myTurtle.right(90)
    myTurtle.forward(size)
    myTurtle.right(90)
    myTurtle.forward(size)
    myTurtle.right(90)
    myTurtle.fillcolor('red')
    myTurtle.penup()


myTurtle.penup()
for gay in range(1000):
    myTurtle.setpos(random.randint(-300,300),random.randint(-300,300))
    square(gay)


input("press a button to close the window:")