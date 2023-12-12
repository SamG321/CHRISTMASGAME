import pygame
from pygame import mixer
from Present import *
from Santa import *
import chimney
from Particles import *
import random

#Opens the credit files
file_obj = open("assets/credits.txt", "r")
lines = file_obj.read().splitlines()
file_obj.close()

def mplayer(name):
    '''  for playing music  '''
    mixer.init()
    mixer.music.load(name)
    mixer.music.set_volume(1)
    mixer.music.play(-1)

mplayer('assets/intro.mp3')

#Main Class Code

class Main:
    def __init__(self):
        pygame.init()
        #Stars the features.
        self.screen = pygame.display.set_mode([1920,1080])
        self.clock = pygame.time.Clock()
        self.running = True
        self.play = False
        self.endgame = False
        self.font = pygame.font.SysFont(None, 48)
        self.cooldown = 60

        self.titleFont = pygame.font.SysFont(None, 100)
        self.drop_cooldown = 0
        self.amount_of_frames = 0
        self.goleft = False
        self.goright = False

        self.chimneyspeed = 3
        self.max_cooldown = 60
        self.time = 60

        self.sliderOne = pygame.Rect(330,396,30,30)
        self.sliderTwo = pygame.Rect(900,396,30,30)
        self.sliderThree = pygame.Rect(1470,396,30,30)

        self.slideBarOne = pygame.Rect(334,396,22,487)
        self.slideBarTwo = pygame.Rect(904,396,22,487)
        self.slideBarThree = pygame.Rect(1474,396,22,487)
        
        self.nextColour = random.choice(["red","green","blue"])
        chimney.create_list(5)

        #Loads the image due to technical bugs may not be found 
        try:
            self.clouds = pygame.image.load("assets\\clouds.png").convert_alpha()
            self.introBackground = pygame.image.load("assets\\intro_background.png").convert()
            self.playButton = pygame.image.load("assets\\intro_play.png").convert_alpha()
            self.playAgainButton = pygame.image.load("assets\\intro_playAgain.png").convert_alpha()
            self.playButtonHover = pygame.image.load("assets\\intro_play_inverted.png").convert_alpha()
            self.playAgainButtonHover = pygame.image.load("assets\\intro_playAgain_inverted.png").convert_alpha()
            self.settingsIcon = pygame.image.load("assets\\settings_icon.png").convert_alpha()
            self.settingsIconHover = pygame.image.load("assets\\settings_icon_inverted.png").convert_alpha()
            self.settingsText = pygame.image.load("assets\\settings.png").convert_alpha()
        except FileNotFoundError:
            self.clouds = pygame.image.load("Cool_Game_Cuchulainn\\assets\\clouds.png").convert_alpha()
            self.introBackground = pygame.image.load("Cool_Game_Cuchulainn\\assets/intro_background.png").convert()
            self.playButton = pygame.image.load("Cool_Game_Cuchulainn\\assets/intro_play.png").convert_alpha()
            self.playAgainButton = pygame.image.load("Cool_Game_Cuchulainn\\assets/intro_playAgain.png").convert_alpha()
            self.playButtonHover = pygame.image.load("Cool_Game_Cuchulainn\\assets/intro_play_inverted.png").convert_alpha()
            self.playAgainButtonHover = pygame.image.load("Cool_Game_Cuchulainn\\assets/intro_playAgain_inverted.png").convert_alpha()
            self.settingsIcon = pygame.image.load("Cool_Game_Cuchulainn\\assets\\settings_icon.png").convert_alpha()
            self.settingsIconHover = pygame.image.load("Cool_Game_Cuchulainn\\assets\\settings_icon_inverted.png").convert_alpha()
            self.settingsText = pygame.image.load("Cool_Game_Cuchulainn\\assets\\settings.png").convert_alpha()

        self.santas = []
        self.presents = []
        self.particles = []
        self.blizzards = [BLIZZARD(0,0,10,True),BLIZZARD(1920,0,10,True),BLIZZARD(0,1080,10,True),BLIZZARD(1920,1080,10,True),
        BLIZZARD(0,0,13),BLIZZARD(1920,0,13),BLIZZARD(0,1080,13),BLIZZARD(1920,1080,13)]

        for i in range(5):
            self.blizzards.append(BLIZZARD(random.randint(0,1920),random.randint(0,1080),random.randint(5,15)))

        self.score = 0

        self.scrollSpeed = 0
        self.scroll = 0
        self.tiles = math.ceil(1920/self.clouds.get_width()) + 1

        self.santa = Santa()

        self.exitButton = pygame.image.load("assets/settings_exit.png").convert_alpha()
        self.exitButtonHover = pygame.image.load("assets/settings_exit_inverted.png").convert_alpha()
        self.exitButtonRect = self.exitButton.get_rect()
        w2, h2 = self.exitButtonRect.size
        self.exitButtonRect.x = int(1920/2-(w2/2))
        self.exitButtonRect.y = 1080-h2-50

        self.introBackground = pygame.image.load("assets/intro_background.png").convert()
        self.playButton = pygame.image.load("assets/intro_play.png").convert_alpha()
        self.playButtonHover = pygame.image.load("assets/intro_play_inverted.png").convert_alpha()
        #Centers the buttons (cannot be a function due the nature the the button hense the sloppy code)
        w, h = pygame.display.get_surface().get_size()

        self.playRect = self.playButton.get_rect()
        w2,h2 = self.playRect.size
        self.playRect.x = int((w/2)-(w2/2))
        self.playRect.y = 700

        self.settings = False
        self.settingsIconRect = self.settingsIcon.get_rect()
        self.settingsIconRect.x = 50
        w2, h2 = self.settingsIconRect.size
        self.settingsIconRect.y = h-h2-50

        self.playAgainRect = self.playAgainButton.get_rect() #defining the play again button
        w2,h2 = self.playAgainRect.size
        self.playAgainRect.x = int((w/2)-(w2/2))
        self.playAgainRect.y = 850

        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # if the game is running
            if self.play == True:
                self.screen.fill((11, 20, 31))

                self.scroll = 0


                # if the background goes off the end of the screen
                if abs(self.scrollSpeed) > self.clouds.get_width():
                    # do not move it
                    self.scrollSpeed = 0

                # draw chimneys
                self.amount_of_frames +=1

                self.timeLeft = self.time - int(self.amount_of_frames/60)

                if self.timeLeft <= 0: #if the timer runs out 
                    self.play = False
                    self.endgame = True #activate the endgame screen on the next frame

                chimney.DrawChimneys(self.screen,self.chimneyspeed)
                
                # check if any keys have been pressed 
                keys = pygame.key.get_pressed()

                # if left has been pressed, updated the 'goleft' variable
                if keys[pygame.K_LEFT]:
                    self.goleft = True
                else:
                    self.goleft = False
                
                # if right has been pressed, updated the 'goright' variable
                if keys[pygame.K_RIGHT]:
                    self.goright = True
                else:
                    self.goright = False

                # if space has been pressed, drop a present
                if keys[pygame.K_SPACE]:
                    # only if there isnt a cooldown
                    if self.drop_cooldown <= 0:
                        self.drop = True
                        self.drop_cooldown = self.max_cooldown
                    else:
                        self.drop = False
                else:
                    self.drop = False
                self.drop_cooldown -= 1 
  
                # if a present can be dropped
                if self.drop == True:
                    present = Present(self.santa.rect.midleft,self.nextColour) # create a new present object
                    self.presents.append(present) # add a new present to the list 
                    self.nextColour = random.choice(["red","green","blue"]) # randomly choose between a colour

                # update present logic
                for i in self.presents:
                    for j in chimney.Chimney_sprite_group:
                        # check if present has collided with chimney
                        if pygame.Rect.colliderect(i.rect, j.rect):
                            # spawn particles
                            particle = Particles(i.rect)
                            self.particles.append(particle)
                            self.score+=1
                            if i.colour == j.colour:
                                self.score += 2 # increase score more
                            i.needRemove = True # remove present from game
                
                #update presents
                for present in self.presents:
                    present.update(self)
                for present in self.presents:
                    present.draw(self.screen)
                for particle in self.particles:
                    particle.update(self.screen, self.chimneyspeed)

                #Text shadow.
                def text_shadow(text_var,colour,x,y):
                    txt = self.font.render(text_var.upper(), True, colour)
                    txt2 = self.font.render(text_var.upper(), True, "GRAY")
                    self.screen.blit(txt2,pygame.Rect(x-2,y-2,72,72)) #3d affect
                    self.screen.blit(txt2,pygame.Rect(x-1,y-1,72,72))
                    self.screen.blit(txt,pygame.Rect(x,y,74,74))

                #Santa stuff
                self.santa.update(Main,self.goleft,self.goright)
                self.santa.draw(self.screen)

                for blizzard in self.blizzards:
                    blizzard.update(self)

                #renders the code
                text_shadow((f"TIME LEFT: {self.timeLeft}S"),"WHITE",3,10)
                text_shadow((f"NEXT COLOUR: {self.nextColour}"),self.nextColour.upper(),3,48)
                text_shadow((f"SCORE: {self.score}"),"WHITE",3,86)

            elif self.endgame == True: # endgame screen
                self.screen.fill([150,0,0]) #fill in the screen with red (change later)
                self.screen.blit(self.playAgainButton, self.playAgainRect) # put the play again button on screen

                def center_text(text,height_already,size=17):
                    w, h = pygame.display.get_surface().get_size()
                    font = pygame.font.SysFont("Courier", size)
                    text = font.render(text, True, "WHITE")
                    text_width = text.get_rect().height
                    text_width += height_already
                    text_rect = text.get_rect(center=(w/2, text_width))
                    self.screen.blit(text, text_rect)
                    return text_width
 
                # if the button is pressed
                if self.playAgainRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.endgame = False    #reset variables
                    self.drop_cooldown = 0
                    self.amount_of_frames = 0
                    self.score = 0
                    self.goleft = False
                    self.goright = False
                    self.nextColour = random.choice(["red","green","blue"])
                    self.santas = []
                    self.presents = []
                    self.santa = Santa()

                elif self.playAgainRect.collidepoint(pygame.mouse.get_pos()):
                    # invert the colour if it is hovered
                    self.screen.blit(self.playAgainButtonHover, self.playAgainRect)

                #renders the text for the end screen
                alright_hight = 5
                for line in lines:
                    alright_hight = center_text(line,alright_hight)
                alright_hight = center_text(f"SCORE:{self.score}",alright_hight,size=100)

                
            elif self.settings == True:
                self.screen.fill([150,0,0])
                self.screen.blit(self.settingsText, (0,0))
                self.screen.blit(self.settingsIcon, self.settingsIconRect)

                self.cooldown -= 1
                #white bars for sliders
                #gui
                pygame.draw.rect(self.screen, (255,255,255) ,self.slideBarOne)
                pygame.draw.rect(self.screen, (255,255,255) ,self.slideBarTwo)
                pygame.draw.rect(self.screen, (255,255,255) ,self.slideBarThree)
                #grey circles

                pygame.draw.rect(self.screen, (181,181,181) ,self.sliderOne)
                pygame.draw.rect(self.screen, (181,181,181) ,self.sliderTwo)
                pygame.draw.rect(self.screen, (181,181,181) ,self.sliderThree)
                sliderarray =[[self.sliderOne,self.slideBarOne,self.time],[self.sliderTwo,self.slideBarTwo,self.max_cooldown],[self.sliderThree,self.slideBarThree,self.chimneyspeed]]
                for slider_count in sliderarray:
                    if slider_count[1].colliderect(pygame.Rect(pygame.mouse.get_pos()[0] - 40,pygame.mouse.get_pos()[1] ,80,1)) and pygame.mouse.get_pressed()[0]:
                        slider_count[0].centery = pygame.mouse.get_pos()[1]
                    slidermultiplier = 6-((slider_count[0].y-396)//81)
                    if slidermultiplier == 7: 
                        slidermultiplier =6
                    if slider_count[0] != self.sliderThree:
                        slidermultiplier = slidermultiplier * 10
                    slider_count[2] = slidermultiplier
                    slider_img = self.font.render(str(slider_count[2]), True, (0,0,0))
                    self.screen.blit(slider_img, (slider_count[0][0]-60, slider_count[0][1]))
                
                self.time = sliderarray[0][2]
                self.max_cooldown =sliderarray[1][2]
                self.chimneyspeed =sliderarray[2][2]

                self.screen.blit(self.exitButton, self.exitButtonRect)
                # if the button is pressed
                if self.exitButtonRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.running = False # ends the game
                elif self.exitButtonRect.collidepoint(pygame.mouse.get_pos()):
                    # invert the colour if it is hovered
                    self.screen.blit(self.exitButtonHover, self.exitButtonRect)

                    


                

                # if the button is pressed
                if self.settingsIconRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    if self.cooldown < 0:
                        self.settings = False # close settings panel
                        self.cooldown = 60
                elif self.settingsIconRect.collidepoint(pygame.mouse.get_pos()):
                    # invert the colour if it is hovered
                    self.screen.blit(self.settingsIconHover, self.settingsIconRect)

            else:
                self.screen.blit(self.introBackground, (0,0))
                self.screen.blit(self.playButton, self.playRect)
                self.screen.blit(self.settingsIcon, self.settingsIconRect)
 
                # if the button is pressed
                if self.playRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.play = True # start the game
                elif self.playRect.collidepoint(pygame.mouse.get_pos()):
                    # invert the colour if it is hovered
                    self.screen.blit(self.playButtonHover, self.playRect)

                self.cooldown -= 1

                # if the button is pressed
                if self.settingsIconRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    if self.cooldown < 0:
                        self.settings = True # open settings panel
                        self.cooldown = 60
                elif self.settingsIconRect.collidepoint(pygame.mouse.get_pos()):
                    # invert the colour if it is hovered
                    self.screen.blit(self.settingsIconHover, self.settingsIconRect)



            pygame.display.flip()

class BLIZZARD:
    def __init__(self,x,y,vel,main:bool = False):
        try:
            self.baseImage = pygame.image.load("assets\\Blizzard2.png").convert_alpha()
        except FileNotFoundError:
            self.baseImage = pygame.image.load("Cool_Game_Cuchulainn\\assets\\Blizzard2.png").convert_alpha()
        self.image = self.baseImage
        self.rotation = 225
        if not main:
            self.rotation += random.randrange(-3,3)
        self.position = (x,y)
        self.rect = pygame.Rect(self.position,[self.image.get_width(),self.image.get_height()])
        self.velocity = pygame.math.Vector2(0,-vel)
        self.velocity = self.velocity.rotate(self.rotation)

    
    def update(self,app):
        self.position += self.velocity
        if self.position[0] >1920:
            self.position[0] -= 1920 + self.rect.width
        elif self.position[0] < 0 - self.rect.width:
            self.position[0] += 1920 + self.rect.width


        if self.position[1] >1080:
            self.position[1] -= 1080 + self.rect.height
        elif self.position[1] < 0 - self.rect.height:
            self.position[1] += 1080 + self.rect.height
        
        

        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        pygame.Surface.blit(app.screen,self.image,self.rect)
        


Main()
pygame.quit()