import turtle

myT = turtle.Pen()

image = 'Dat_boi_move.gif'
screen = turtle.Screen()
screen.addshape(image)
myT.shape(image)

turtle.bgcolor('black')
myT.pencolor('red')
myT.fillcolor('white')

myT.speed(0)

myT.setpos(100,200)
myT.shape('turtle')
myT.shape(image)
myT.penup() #lifts the pen

myT.setpos(-100,-100)

pos = myT.position()
print(pos[0])
print(pos[1])

def drawRect():
    myT.pensize(3)
    myT.begin_fill()
    myT.forward(100)
    myT.left(90)
    myT.forward(100)
    myT.left(90)
    myT.forward(100)
    myT.left(90)
    myT.forward(100)
    myT.left(90)
    myT.end_fill()


myT.setpos(000,000)
colors = ['red','yellow','blue','green','purple','white','orange']
def drawShapes(numOfTurns):
    myT.pendown()
    #myTurtle = turtle.Pen()
    #turtle.bgcolor('black')
    myT.speed(0)
    for c in range(500):#,0,-1):
        myT.pencolor(colors[c%len(colors)])
        myT.forward(c+1)
        myT.right(360//numOfTurns)
        #myT.shape(image)

numOfSides = int(turtle.numinput("Number of Sides",
        "How many sides? (3-15)",6,1,15))

drawShapes(numOfSides)

def move():
    myT.penup()
    myT.setpos(-300,0)
    for x in range(-300,300):
        myT.setx(x)

#move()



input()