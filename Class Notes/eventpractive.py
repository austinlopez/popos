import turtle

shit = turtle.Pen()
turtle.bgcolor('black')
shit.color('red')
colors = ['red','green','blue','purple','yellow','white']
shit.speed(0)

currentColorVal = 0

#mouse events
#turtle.onscreenclick(shit.setpos)



def shitty(x,y):
    shit.setpos(x,y)
    global currentColorVal
    shit.color(colors[currentColorVal])

    if currentColorVal == 5:
        currentColorVal = 0
    else:
        currentColorVal += 1

turtle.onscreenclick(shitty)
#keboard events
#turtle.onkeypress(shitty,'Up')
#turtle.listen()

input()