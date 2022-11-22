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
wallText = objects.GroupText(3,3,50,50,59*5,16*5,screen,currentPath+'/assets/TextShow.png',currentPath+'/assets/TextDelete.png',currentPath+'/assets/TextShowCorrect.png',5,SCALE)

StartButton = objects.StartButton(750, 344,currentPath+'/assets/StrtButtn.png',SCALE,screen,wallText)
CheckButton =objects.CheckButton(462,538,currentPath+'/assets/CheckBtn.png',SCALE,screen,wallText)

clockTimer = objects.TimeCountDown(450,380,60,screen)
backGround = objects.Image(0,0,currentPath+'/assets/Bkgnd_Ll.png',5,screen)
backGndDiffSel = objects.Image(0,0,currentPath+'/assets/Bkgnd_DiffSelector.png',5,screen)

sliderDiff = objects.DifficultySlider(200,366,currentPath+'/assets/BallSelect.png',5,screen)
inputText = objects.TextInput(55,535,currentPath+'/assets/EnterTxtAtri.png',5,screen)

RerollButton = objects.RerollButton(625, 340,currentPath+'/assets/RerollButton.png',SCALE,screen,wallText,sliderDiff)
run = True

CLOCKDOWN = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKDOWN, 1000)

wordTextInput = ''
hasStarted = False

while run:
    backGround.draw()
    backGndDiffSel.draw()

    sliderDiff.draw()
    wallText.draw()
    clockTimer.draw()
    RerollButton.draw()
    CheckButton.draw()
    StartButton.draw()
    StartButton.draw()

    if RerollButton.ifPressed() or sliderDiff.sliderAndChange():
        RerollButton.bActive();
        clockTimer.setTime(60)
        hasStarted = False
        wordTextInput = ""
    if CheckButton.ifPressed():
        CheckButton.bActive(wordTextInput)
        wordTextInput = ""
    if StartButton.ifPressed():
        StartButton.bActive();
        hasStarted = True
    
    inputText.draw(wordTextInput)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == CLOCKDOWN and hasStarted:
            if clockTimer.getTime() > 0:
                 clockTimer.clockDown() 
            else:
                hasStarted = False
        ######## Input Text:
        if event.type == pygame.KEYDOWN and hasStarted:
            if event.key == pygame.K_BACKSPACE:
                wordTextInput = wordTextInput[0:-1]
            elif event.key == pygame.K_SPACE or event.key == 13:
                ##Summit by enter
                wallText.showIfExist(wordTextInput)
                wordTextInput = ""
            elif event.key != 96:
                wordTextInput += event.unicode
    pygame.display.update()

pygame.quit()