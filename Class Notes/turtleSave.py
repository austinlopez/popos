import turtle
from PIL import Image

def saveDrawing(drawName):
    print(f"saving drawing to {drawName}.eps/png")
    #get the tkinter canvas
    canvas = turtle.getcanvas()
    #save the drawing as a postscript image
    canvas.postscript(file = drawName + '.eps')
    #use the Pillow module to convert the poscript image file
    img = Image.open(drawName + '.eps')
    img.save(drawName + '.png','png')

myTurtle = turtle.Pen()
myTurtle.penup()
myTurtle.speed(0)
screenWidth = myTurtle.screen.window_width()
screenHeight = myTurtle.screen.window_height()

#the second argument is the fill color
myTurtle.color('black','black')

#this will create a background color
myTurtle.setpos(-screenWidth//2,screenHeight//2)
myTurtle.pendown()
myTurtle.begin_fill()
myTurtle.setpos(screenWidth//2, screenHeight//2)
myTurtle.setpos(screenWidth//2, -screenHeight//2)
myTurtle.setpos(-screenWidth//2, -screenHeight//2)
myTurtle.setpos(-screenWidth//2, screenHeight//2)
myTurtle.end_fill()

myTurtle.color('white')
myTurtle.setpos(0,0)

def drawBoi():
    myT = turtle.Pen()

    image = 'Dat_boi_move.gif'
    screen = turtle.Screen()
    screen.addshape(image)
    myT.shape(image)
    myT.speed(0)
    myT.penup()
    myT.setpos(-screenWidth//2,screenHeight//2)
    for x in range(-screenWidth//2,screenWidth//2):
        for y in [-screenHeight//4,screenHeight//4]:
            myT.setpos(x,y)

#drawBoi()

def drawPP():
    myT = turtle.Pen()
    myT.color('purple')

    myT.circle(10)
    myT.forward(20)
    myT.circle(10)
    myT.backward(14)
    myT.forward(8)
    myT.left(90)
    myT.forward(100)
    myT.left(90)
    myT.forward(8)
    myT.left(90)
    myT.forward(100)

#drawPP()

choice = input('Press s to save your drawing ')
if choice == 's':
    name = input("What do you want to call your drawing? ")
    saveDrawing(name)