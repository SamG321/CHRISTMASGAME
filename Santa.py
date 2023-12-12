import pygame
import math
class Santa:
    def __init__(self):
        self.baseImage = pygame.image.load("assets/santa.png").convert_alpha()
        self.image = self.baseImage.copy()
        self.rect = self.image.get_rect()
        self.drawRect = self.rect.copy()

        self.sinpos = 0.0   #Variables for santas animation
        self.waveLength = 0.05
        self.waveAmplitude = 2

        self.sinpos = 0.0   #Variables for santas animation
        self.waveLength = 0.05
        self.waveAmplitude = 2

        self.position = pygame.math.Vector2(960, 240)

    def update(self, app, goleft, goright):
        self.rect.center = self.position
        self.drawRect = self.image.get_rect()
        self.drawRect.center = self.rect.center

        # if a key is pressed and santa isn't off the side of the map
        if goleft == True and self.position.x > 433:
            self.rect.centerx -= 10
        if goright == True  and self.position.x < 1485:
            self.rect.centerx += 7

        self.sinpos+=self.waveLength                     #vvv santas animation vvv
        self.position.y = self.rect.centery + round(math.sin(self.sinpos)*self.waveAmplitude)

        self.position.x = self.rect.centerx
        

    def draw(self, screen):
        screen.blit(self.image, self.drawRect)