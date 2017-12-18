import math
import turtle

turtle.bgcolor('black')
myTurt = turtle.Pen()
myTurt2 = turtle.Pen()
myTurt3 = turtle.Pen()

myTurt.screen.setworldcoordinates(0,-1,720,1)

myTurt.color('white')
myTurt3.color('white')
myTurt2.color('red')
myTurt3.speed(0)
myTurt.speed(0)
myTurt2.speed(0)

myTurt3.setpos(720,0)
for ang in range(720):
    y1 = math.sin(math.radians(ang))
    y2 = math.cos(math.radians(ang))
    myTurt.setpos(ang, y1)
    myTurt2.setpos(ang, y2)

input()