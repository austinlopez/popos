import pygame
#this program will create a game window and draw a green circle

#initialize the pygame modules
pygame.init()

#creates a game "Surface", set mode defines the [width, height]
screen = pygame.display.set_mode([800,600])

#used for the game loop
keep_going = True

#assigns the rgb color code for green to the GREEN variable
GREEN = (0,255,0)

#defines the radius of our circle
radius = 50

#this is the game loop
while keep_going:
    #gets all the game events
    for event in pygame.event.get():
        #stops the game loop if the event is pygame.QUIT(the window closes)
        if event.type == pygame.QUIT:
            keep_going = False
    
    #draws the circle
    #pygame.draw.circle(Surface, color, pos, radius, width=0)
    pygame.draw.circle(screen, GREEN, (100,100),radius)

    #updates (redraws) the screen
    pygame.display.update()

pygame.quit()