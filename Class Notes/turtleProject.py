'''
    turtleProject.py
    Austin Lopez
    November 27, 2017
    Period 2
'''
import turtle

turtle1 = turtle.Pen()
turtle2 = turtle.Pen()

turtle1.penup()
turtle2.penup()
turtle1.setpos(-100,100)
turtle2.setpos(100,-100)
turtle.bgcolor('black')
turtle1.color('red')
turtle2.color('white')
turtle1.pendown()

colors = ['green', 'blue', 'yellow', 'white', 'red', 'orange']
for counter in range(200): #from 0 to 199 which = to 200 times
    turtle1.forward(counter)
    turtle1.left(25)
    turtle1.pencolor(colors[counter%6])

turtle2.setpos(-90, 100)
turtle2.pendown()

for counter in range(200): #from 0 to 199 which = to 200 times
    turtle2.forward(counter)
    turtle2.left(25)
    turtle2.pencolor(colors[counter%6])

input()