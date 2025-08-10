import pygame
 
pygame.init()

#General setup
SCREEN_WIDTH,SCREEN_HEIGHT = 1200,600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Green-Suit")

clock = pygame.time.Clock()

running =True

while running :
    dt = clock.tick() / 1000
     
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

    #The game!!
    screen.fill("steelblue") 
    pygame.display.flip()

pygame.quit()