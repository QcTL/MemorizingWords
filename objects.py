from tracemalloc import start
import pygame
import random
import os


class TextShow():
    def __init__(self,x,y, srcimageBkgrnd,srcimageDelete,scale,screen,OfftextX,OfftextY,complexity):

        #BackGround
        self.imageCharBack = pygame.image.load(srcimageBkgrnd).convert_alpha()
        self.imageNewCharBack = pygame.transform.scale(self.imageCharBack,(int(self.imageCharBack.get_width()*scale),int(self.imageCharBack.get_height()*scale)))
        self.imageNewCharrectBack = self.imageNewCharBack.get_rect()
        self.imageNewCharrectBack.topleft = (x,y) 

        #Button:
        self.button = Button(x-35,y+9,srcimageDelete,scale,screen)
        self.showingButton = True
        #Text
        self.screen = screen
        self.text = ""
        pygame.font.init()
        self.base_font = pygame.font.Font("CALIBRI.TTF",35)
        self.x = OfftextX
        self.y = OfftextY
        self.complexity = complexity

    def draw(self):
        self.screen.blit(self.imageNewCharBack,(self.imageNewCharrectBack.x, self.imageNewCharrectBack.y))
        text_surface = self.base_font.render(self.text,True,(0,0,0))
        self.screen.blit(text_surface,(self.imageNewCharrectBack.x+self.x,self.imageNewCharrectBack.y+self.y))
        
        if self.showingButton:
            if self.button.draw():
                self.regenerateText()
        
    def setText(self,text):
        self.text= text

    def regenerateText(self):
        word = getWord(self.complexity)
        self.setText(word)

    def turnOffOnButton(self,newValue):
        self.showingButton = newValue
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

class RerollButton():
    
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
            self.groupText.reloadAll()
            self.pressed = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False
        self.screen.blit(self.imageReal,(self.rect.x, self.rect.y))


class GroupText():

    def __init__(self,nX,nY,iniSpaceX,iniSpaceY,sizeX,sizeY,screen,BackImage,DeleteImage,complexity,scale):
        self.matText = list(list())
        self.nX = nX
        self.nY = nY
        actX = iniSpaceX
        actY = iniSpaceY
        self.complexity = complexity
        for i in range(0,nY):
            self.matText.append(list())        
            for j in range(0,nX):
                ts = TextShow(actX + sizeX*i,actY+sizeY*j,BackImage,DeleteImage,scale,screen,19,13,complexity)
                #Sanatize the text get form the dicc: 

                word = getWord(self.complexity)
                ts.setText(word)
               
                self.matText[i].append(ts)
    def reloadAll(self):
        for i in range(0,self.nY):   
            for j in range(0,self.nX):
                word = getWord(self.complexity)
                self.matText[i][j].setText(word)
    def draw(self):
        for i in range(0,self.nY):      
            for j in range(0,self.nX):
                self.matText[i][j].draw()

def getWord(complexity):
        word = random.choice(open('ca.txt','r',encoding="utf-8").readlines())
        if '/' in word:
            head, sep, tail = word.partition('/')
            print(head+ " " + sep + " " + tail )
        else:
            head = word[:len(word)-1]
            print(head)
    
        while len(head) > complexity:
            word = random.choice(open('ca.txt','r',encoding="utf-8").readlines())
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
        self.base_font = pygame.font.Font("CALIBRI.TTF",35)
        #TODO: Cahnge to a more pixelated font

    def draw(self):
        text_surface = self.base_font.render(str(self.Time),True,(255,255,255))
        self.screen.blit(text_surface,(self.nX,self.nY))

    def clockDown(self):
        self.Time = self.Time - 1