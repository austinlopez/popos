import pygame
import sys


pygame.init()

class Circle(pygame.sprite.Sprite):

    def __init__(self, color, radius):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((radius * 2,radius * 2))
        self.image.fill((0,0,0))
        pygame.draw.circle(self.image,color, (radius, radius), radius, 0)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

screen = pygame.display.set_mode([800,600])
background = pygame.Surface(screen.get_size())
background.fill([0,0,0])
screen.blit(background,(0,0))

circle = Circle(([255,0,0]),40)
allSprites = pygame.sprite.Group(circle)

pygame.mouse.set_visible(False)
keepGoing = True
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    
    allSprites.clear(screen,background)
    allSprites.update()
    allSprites.draw(screen)

    pygame.display.flip()

    #return mouse
pygame.mouse.set_visible(True)