import pygame

#HP bar class
class hp():
    def __init__(self,x,y,width,height,maxHP):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = maxHP
        self.maxHP = maxHP

    def draw(self,screen):

        rat = self.hp / self.maxHP
        pygame.draw.rect(screen,(204,0,0),(self.x,self.y,self.width,self.height))
        pygame.draw.rect(screen,(0,255,0),(self.x,self.y,self.width * rat,self.height))
