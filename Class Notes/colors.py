import turtle
#here is an array with six different colors
colors = ['red','purple','blue','green','yellow','orange']
myTurtle = turtle.Pen()
turtle.bgcolor('black')
# for x in range(360):
#     #color() changes the color of the pen
#     myTurtle.color(colors[x % 6]) #what does this do? 
#     #hint - how do remainders work (can you ever get one as big as)
#     myTurtle.forward(x)
#     myTurtle.right(90)
#     #there are 6 speeds: slowes, slow, 
#     #normal, fast, and fastest
#     myTurtle.speed('fastest')

#input("Press enter to close screen")

myTurtle.reset()
myTurtle.color('white')
myTurtle.forward(100)
#lets make a circle
myTurtle.circle(30)
#the number inside the () is the radius in pixels
myTurtle.speed('fastest')
for radius in range(0,300):
    myTurtle.setpos(-400+radius,-300+radius)
    myTurtle.color(colors[radius%6])
    myTurtle.circle(radius)

input("Press enter to close screen")