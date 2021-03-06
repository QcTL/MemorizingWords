from tracemalloc import start
from turtle import pos
import pygame
import random
import os


class TextShow():
    def __init__(self,x,y, srcimageBkgrnd,srcimageDelete,srcimageCorrect,scale,screen,OfftextX,OfftextY,complexity):

        #BackGround
        self.imageCharBack = pygame.image.load(srcimageBkgrnd).convert_alpha()
        self.imageNewCharBack = pygame.transform.scale(self.imageCharBack,(int(self.imageCharBack.get_width()*scale),int(self.imageCharBack.get_height()*scale)))
        self.imageNewCharrectBack = self.imageNewCharBack.get_rect()
        self.imageNewCharrectBack.topleft = (x,y) 
        self.TextVisible = True
        #Button:
        self.button = Button(x-35,y+9,srcimageDelete,scale,screen)
        self.showingButton = True
        #Correct
        self.CorCharBack = pygame.image.load(srcimageCorrect).convert_alpha()
        self.CorNewCharBack = pygame.transform.scale(self.CorCharBack,(int(self.CorCharBack.get_width()*scale),int(self.CorCharBack.get_height()*scale)))
        self.CorNewCharrectBack = self.CorNewCharBack.get_rect()
        self.CorNewCharrectBack.topleft = (x,y)
        self.ShowCorrect = False
        #Text
        self.screen = screen
        self.text = ""
        pygame.font.init()
        self.base_font = pygame.font.Font(None,35)
        self.x = OfftextX
        self.y = OfftextY
        self.complexity = complexity

    def draw(self):
        self.screen.blit(self.imageNewCharBack,(self.imageNewCharrectBack.x, self.imageNewCharrectBack.y))
       
        if self.TextVisible:
            text_surface = self.base_font.render(self.text,True,(0,0,0))
            self.screen.blit(text_surface,(self.imageNewCharrectBack.x+self.x,self.imageNewCharrectBack.y+self.y))
            if self.ShowCorrect:
                self.screen.blit(self.CorNewCharBack,(self.CorNewCharrectBack.x,self.CorNewCharrectBack.y))


        if self.showingButton:
            if self.button.draw():
                self.regenerateText()
        
    def setText(self,text):
        self.text= text

    def getText(self):
        return self.text

    def regenerateText(self):
        word = getWord(self.complexity)
        self.setText(word)
        self.ShowCorrect = False

    def turnOffOnButton(self,newValue):
        self.showingButton = newValue
    
    def changeVisibility(self,newVis):
        self.TextVisible = newVis
    
    def setComplexity(self,complexity):
        self.complexity = complexity
    def setCorrect(self,correct):
        self.ShowCorrect = correct

class Image():
    def __init__(self,x,y, srcimageBkgrnd,scale,screen):

        #BackGround
        self.imageCharBack = pygame.image.load(srcimageBkgrnd).convert_alpha()
        self.imageNewCharBack = pygame.transform.scale(self.imageCharBack,(int(self.imageCharBack.get_width()*scale),int(self.imageCharBack.get_height()*scale)))
        self.imageNewCharrectBack = self.imageNewCharBack.get_rect()
        self.imageNewCharrectBack.topleft = (x,y) 
        self.screen = screen
    def draw(self):
        self.screen.blit(self.imageNewCharBack,(self.imageNewCharrectBack.x, self.imageNewCharrectBack.y))

class Button():
    def __init__(self,x,y, image,scale,screen):
        self.imageReal = pygame.image.load(image).convert_alpha()
        width = self.imageReal.get_width()
        height = self.imageReal.get_height()
        self.imageReal = pygame.transform.scale(self.imageReal,(int(width*scale),int(height*scale)))
        self.rect = self.imageReal.get_rect()
        self.rect.topleft = (x,y) 
        self.pressed = False
        self.screen = screen
        self.lastImages = []

    def draw(self):
        #Get mouse position
        pos = pygame.mouse.get_pos() 
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not self.pressed:
            self.pressed = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False
        self.screen.blit(self.imageReal,(self.rect.x, self.rect.y))
        return self.pressed

class CheckButton():
    def __init__(self,x,y, image,scale,screen,groupText):
        self.imageReal = pygame.image.load(image).convert_alpha()
        width = self.imageReal.get_width()
        height = self.imageReal.get_height()
        self.imageReal = pygame.transform.scale(self.imageReal,(int(width*scale),int(height*scale)))
        self.rect = self.imageReal.get_rect()
        self.rect.topleft = (x,y) 
        self.pressed = False
        self.screen = screen
        self.lastImages = []

        self.groupText = groupText
    def draw(self,text):
        #Get mouse position
        pos = pygame.mouse.get_pos() 
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not self.pressed:
            self.groupText.showIfExist(text)
            self.pressed = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False
        self.screen.blit(self.imageReal,(self.rect.x, self.rect.y))
        return self.pressed

class StartButton():
    def __init__(self,x,y, image,scale,screen,groupText):
        self.imageReal = pygame.image.load(image).convert_alpha()
        width = self.imageReal.get_width()
        height = self.imageReal.get_height()
        self.imageReal = pygame.transform.scale(self.imageReal,(int(width*scale),int(height*scale)))
        self.rect = self.imageReal.get_rect()
        self.rect.topleft = (x,y) 
        self.pressed = False
        self.screen = screen
        self.lastImages = []

        self.groupText = groupText
    def draw(self):
        #Get mouse position
        pos = pygame.mouse.get_pos() 
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not self.pressed:
            
            ## START THE GAME ## 
            self.groupText.changeAllVisible(False)
            self.pressed = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False
        self.screen.blit(self.imageReal,(self.rect.x, self.rect.y))
        return self.pressed

class RerollButton():
    
    def __init__(self,x,y, image,scale,screen,groupText,selComplexity):
        self.imageReal = pygame.image.load(image).convert_alpha()
        width = self.imageReal.get_width()
        height = self.imageReal.get_height()
        self.imageReal = pygame.transform.scale(self.imageReal,(int(width*scale),int(height*scale)))
        self.rect = self.imageReal.get_rect()
        self.rect.topleft = (x,y) 
        self.pressed = False
        self.screen = screen
        self.lastImages = []
        self.selComplexity = selComplexity
        
        
        self.groupText = groupText
    def draw(self):
        #Get mouse position
        pos = pygame.mouse.get_pos() 
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not self.pressed:
            ## Restarts The game
            self.groupText.reloadAll(self.selComplexity.getDifficulty())
            self.groupText.changeAllVisible(True)
            self.pressed = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False
        self.screen.blit(self.imageReal,(self.rect.x, self.rect.y))
        return self.pressed

class GroupText():

    def __init__(self,nX,nY,iniSpaceX,iniSpaceY,sizeX,sizeY,screen,BackImage,DeleteImage,ShowImage,complexity,scale):
        self.matText = list(list())
        self.nX = nX
        self.nY = nY
        actX = iniSpaceX
        actY = iniSpaceY
        self.complexity = complexity
        for i in range(0,nY):
            self.matText.append(list())        
            for j in range(0,nX):
                ts = TextShow(actX + sizeX*i,actY+sizeY*j,BackImage,DeleteImage,ShowImage,scale,screen,19,13,complexity)
                #Sanatize the text get form the dicc: 

                word = getWord(self.complexity)
                ts.setText(word)
               
                self.matText[i].append(ts)
    def reloadAll(self,complexity):
        self.complexity = complexity
        for i in range(0,self.nY):   
            for j in range(0,self.nX):
                word = getWord(complexity)
                self.matText[i][j].setComplexity(complexity)
                self.matText[i][j].setText(word)
                self.matText[i][j].setCorrect(False)
    def draw(self):
        for i in range(0,self.nY):      
            for j in range(0,self.nX):
                self.matText[i][j].draw()

    def changeAllVisible(self,newVis):
        for i in range(0,self.nY):      
            for j in range(0,self.nX):
                self.matText[i][j].changeVisibility(newVis)
                self.matText[i][j].setCorrect(False)

    def showIfExist(self, text):
        i = 0
        j = 0
        found = False
        while not found and i < self.nX:
            while not found and j < self.nY:
                if self.matText[i][j].getText() == text:
                    self.matText[i][j].changeVisibility(True)
                    self.matText[i][j].setCorrect(True)
                    found = True
                else:
                    j = j + 1
            if not found:
                j = 0
                i =  i + 1
        

    def changeVisible(self, posX, posY, newVisible):
        self.matText[posX][posY].changeVisibility(newVisible)

def getWord(complexity):
        word = random.choice(open('es.txt','r',encoding="utf-8").readlines())
        if '/' in word:
            head, sep, tail = word.partition('/')
            print(head+ " " + sep + " " + tail )
        else:
            head = word[:len(word)-1]
            print(head)
    
        while len(head) > complexity:
            word = random.choice(open('es.txt','r',encoding="utf-8").readlines())
            if '/' in word:
                head, sep, tail = word.partition('/')
                #print(head+ " " + sep + " " + tail )
            else:
                head = word[:len(word)-1]
                #print(head)
        return head

class TimeCountDown():

    def __init__(self,nX,nY,startTime,screen):
        self.nX = nX
        self.nY = nY
        self.startTime = startTime
        self.screen = screen
        self.Time = startTime
        pygame.font.init()
        self.base_font = pygame.font.Font(None,60)
        #TODO: Cahnge to a more pixelated font

    def draw(self):
        text_surface = self.base_font.render(str(self.Time),True,(255,255,255))
        self.screen.blit(text_surface,(self.nX,self.nY))

    def clockDown(self):
        self.Time = self.Time - 1
    
    def getTime(self):
        return self.Time

    def setTime(self,time):
        self.Time = time
class TextInput():

    def __init__(self,x,y,srcimage,scale,screen):
        self.imageChar = pygame.image.load(srcimage).convert_alpha()
        self.imageNewChar = pygame.transform.scale(self.imageChar,(int(self.imageChar.get_width()*scale),int(self.imageChar.get_height()*scale)))
        self.imageNewCharrect = self.imageNewChar.get_rect()
        self.imageNewCharrect.topleft = (x,y) 
        self.screen = screen
        self.pressed = False
    
    def draw(self):

        #Get mouse position
        pos = pygame.mouse.get_pos() 

        if self.imageNewCharrect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not self.pressed:
            self.pressed = True
            print('Hola')
        
        if pygame.mouse.get_pressed()[0] == 1 and not self.imageNewCharrect.collidepoint(pos):
            self.pressed = False
        
        self.screen.blit(self.imageNewChar,(self.imageNewCharrect.x, self.imageNewCharrect.y))

    def get_pressed(self):
        return self.pressed

class DifficultySlider():
    def __init__(self,x,y,srcimage,scale,screen):
        self.ballChar = pygame.image.load(srcimage).convert_alpha()
        self.ballNewChar = pygame.transform.scale(self.ballChar,(int(self.ballChar.get_width()*scale),int(self.ballChar.get_height()*scale)))
        self.ballNewCharrect = self.ballNewChar.get_rect()
        self.ballNewCharrect.topleft = (x,y) 
        self.screen = screen
        self.pressed = False
        self.ballPos = 1
        self.x = x
        self.y = y
        self.listPoints = [[-125,0], [-75,0],[-25,0],[+25,0],[+75,0],[+125,0]]
    def draw(self):
        #Get mouse position
        pos = pygame.mouse.get_pos() 

        if self.ballNewCharrect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            self.pressed = True

        if self.pressed:
            if((self.listPoints[self.ballPos][0]+self.x - pygame.mouse.get_pos()[0]) > 25 and self.ballPos > 0):
                self.ballPos  = self.ballPos - 1
            elif((self.listPoints[self.ballPos][0]+self.x - pygame.mouse.get_pos()[0]) < -25 and self.ballPos < 5):
                self.ballPos  = self.ballPos + 1
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False
        
        self.ballNewCharrect.topleft = (self.listPoints[int(self.ballPos)][0] + self.x + -15, self.y - 16)
        self.screen.blit(self.ballNewChar,(self.ballNewCharrect.x,self.ballNewCharrect.y))


    def getDifficulty(self):
        return self.ballPos + 4