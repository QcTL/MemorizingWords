import pygame
import objects
import os
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 950

SCALE = 4.5

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Memoritzador')
currentPath = os.path.dirname(__file__)

#t1 = objects.TextShow(100,100,currentPath+'/assets/TextShow.png',5,screen,19,18)
#t1.setText("PatataBrabesSalades")
wallText = objects.GroupText(3,3,50,50,59*5,16*5,screen,currentPath+'/assets/TextShow.png',currentPath+'/assets/TextDelete.png',5,SCALE)
RerollButton =objects.RerollButton(700, 300,currentPath+'/assets/RerollButton.png',SCALE,screen,wallText)
clockTimer = objects.TimeCountDown(500,500,60,screen)

run = True

CLOCKDOWN = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKDOWN, 1000)

while run:
    wallText.draw()
    RerollButton.draw()
    clockTimer.draw()
    #TODO:Create a background so the sprites don't sit one top of another
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == CLOCKDOWN:
            clockTimer.clockDown()  
    pygame.display.update()

pygame.quit()