import pygame
import math
class Present:
    def __init__(self,pos,colour):
        self.colour = colour

        try:
            self.baseImage = pygame.image.load(f"assets\\{self.colour}_present.png")
        except FileNotFoundError:
            self.baseImage = pygame.image.load(f"Cool_Game_Cuchulainn\\assets\\{self.colour}_present.png")

        self.size = 50
        self.scaleImage = pygame.transform.scale(self.baseImage,(self.size,self.size))
        self.position = (pos)
        self.rect = pygame.Rect(self.position,(self.size,self.size))
        self.velocity = pygame.math.Vector2(0,5)
        self.rotation = 0
        self.velocity = self.velocity.rotate(self.rotation)

        self.needRemove = False

    def update(self,app):
        self.rotation += math.sin(self.position[1]/30) #presents animation

        self.position += self.velocity
        self.rect.center = self.position
        self.image = pygame.transform.rotate(self.scaleImage,self.rotation)

        # if the present goes off the screen
        if self.position[1] >= 1080 :
            self.needRemove = True # remove present

        if self.needRemove == True:
            app.presents.remove(self)
        
    def draw(self, screen):
        try:
            pygame.Surface.blit(screen,self.image,self.rect)
        except:
            pass