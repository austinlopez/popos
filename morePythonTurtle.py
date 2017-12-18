import turtle

colors = ['red','yellow','blue','green','purple','white','orange']
def drawShapes(numOfTurns):
    myTurtle = turtle.Pen()
    turtle.bgcolor('black')
    myTurtle.speed(0)
    for c in range(100,0,-1):
        myTurtle.pencolor(colors[c%len(colors)])
        myTurtle.forward(c+1)
        myTurtle.right(360//numOfTurns)

numOfSides = int(turtle.numinput("Number of Sides",
        "How many sides? (3-15)",6,3,15))

drawShapes(numOfSides)
input()