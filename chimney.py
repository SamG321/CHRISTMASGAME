import pygame
import random
pygame.init()

#List for the chimneys and additionally the rects, with the possible colours
global chimney_list_rect
chimney_list = []
possible_chimney_list = ["blue","green","red"]
amount_of_chimneys = 0

# Class for the sprite which contians the rect, image, colour and height
class ChimneySprite(pygame.sprite.Sprite):
    def __init__(self, place_in_array,amount):
        super().__init__()
        global amount_of_chimneys
        amount_of_chimneys += 1

        self.colour = place_in_array[0]
        self.image = pygame.image.load(("assets/"+place_in_array[0]+"_chimney_top.png"))
        self.rect = self.image.get_rect()
        self.rect.height = 5
        self.height = place_in_array[1]
        self.rect.x = amount_of_chimneys*100 + amount_of_chimneys*((1920 - (amount*100))/amount+1)
        self.rect.y = 1080-(50*self.height)


#This creates the original list and turns them into sprites.
def create_list(amount):
    chimney_list = []
    for x in range(amount):
        chimney_list.append([possible_chimney_list[random.randint(0,len(possible_chimney_list)-1)]])
        chimney_list[x].append(random.randint(1,3))
    global Chimney_sprite_group
    Chimney_sprite_group = pygame.sprite.Group()
    for i in chimney_list:
        Chimney_sprite_group.add(ChimneySprite(i,amount))

#This renders the chimneys and when is not in screen it moves it to the other side
def DrawChimneys(window,chimneyspeed):
    for moving_sprite in Chimney_sprite_group:
        moving_sprite.rect.x = moving_sprite.rect.x - chimneyspeed
        if moving_sprite.rect.x <= -100:
            #thos cjamges tje s[rote tp jave ]
            moving_sprite.colour = random.choice(possible_chimney_list)
            moving_sprite.image = pygame.image.load(("assets/"+moving_sprite.colour+"_chimney_top.png"))
            moving_sprite.rect.x = 1920
            height = random.randint(0,3)
            moving_sprite.rect.y = 1080-(50*moving_sprite.height)
            height = random.randint(0,3)
            moving_sprite.rect.y = 1080-(50*moving_sprite.height)

    Chimney_sprite_group.draw(window)
