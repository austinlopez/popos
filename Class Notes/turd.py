import turtle
from random import randrange

screen = turtle.Screen()

screen.screensize(800,800)
turt = turtle.Pen()
turt2 = turtle.Pen()
#turtle.bgcolor('black')
turt.speed(0)
turt2.speed(0)

def something():
    turt.penup()
    turt2.penup()
    turt.setpos(-100,0)
    turt2.setpos(100,0)
    turt.pendown()
    turt2.pendown()
    #turt.color('red')
    turt.down()
    turt2.down()
    #turt.pensize(3)
    for i in range(1000):
        turt.forward(i)
        turt2.forward(i)
        turt.left(262)
        turt2.right(262)


def star(x,y,color,size):
    turt.penup()
    turt.setpos(x,y)
    turt.fillcolor(color)
    turt.pendown()
    turt.begin_fill()
    #turt.forward(20)
    for gay in range(5):
        turt.forward(size)
        turt.left(72)
        turt.forward(size)
        turt.right(144)
    turt.end_fill()
    turt.penup()

#star()

def randomStars():
    colors = ['red','blue','orange','green','pink']
    for i in range(100):
        turt.right(i)
        starX = randrange(-450,350)
        starY = randrange(-350,350)
        starC = colors[randrange(0,4)]
        starSize = randrange(10,50)
        star(starX,starY,starC,starSize)

randomStars()
input()