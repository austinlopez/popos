import pygame

pygame.init()
screen = pygame.display.set_mode([800,600])

#This defines the game clock
myClock = pygame.time.Clock()

keep_going = True

#These will control the sped of the circles
greenCircleSpeed = 200
redCircleSpeed = 400

#variables for colors
GREEN = (0,255,0)
RED = (255,0,0)

#x and y for green circle
greenX = 100
greenY = 100

#x and y for red circle
redX = 600
redY = 500

#defines the radii of our circles
greenRadius = 50
redRadius = 75

changeRedDirection = False
#game loop
while keep_going:
    #redraws the background, remove it to see why
    screen.fill([0,0,0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    
    #green circle
    pygame.draw.circle(screen, GREEN, (int(greenX), int(greenY)), greenRadius)
    #red circle
    pygame.draw.circle(screen, RED, (int(redX), int(redY)), redRadius)

    #gets how much time has passed since last called (loop time)
    timePassed = myClock.tick()
    #changes from milliseconds to seconds
    timePassedSeconds = timePassed / 1000.0

    #red and green distance moved each loop
    greenDistanceMoved = int(timePassedSeconds * greenCircleSpeed)
    redDistanceMoved = int(timePassedSeconds * redCircleSpeed)

    #make the red circle bounce
    if redX < 0 and redY < 0:
        changeRedDirection = True
    
    if redX > 800 and redY >600:
        changeRedDirection = False

    if changeRedDirection == True:
        redX += redDistanceMoved
        redY += redDistanceMoved
    else: 
        redX -= redDistanceMoved
        redY -= redDistanceMoved
    
    #move the green circle
    greenX += greenDistanceMoved

    pygame.display.update()

pygame.quit()