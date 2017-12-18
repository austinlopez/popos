import turtle

turd1 = turtle.Pen()
turd2 = turtle.Pen()

turtle.bgcolor('black')
turd1.color('red')
turd2.color('white')
turd2.penup()
turd2.setpos(100,100)
turd2.pendown()

turd2.pensize(10)
turd2.forward(50)
turd2.left(60)
turd2.forward(100)
turd2.dot(30)
turd2.forward(50)


print(turd1.distance(turd2))


input()