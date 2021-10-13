import sys, pygame
import os

current_path = os.path.dirname(__file__)
IMG = pygame.image.load(os.path.join(current_path, 'galaxiannave.jpg'))
R = IMG.get_rect()
class Nave:
    def __init__(self, x, y, width, limd, limi):
        self.x = x
        self.y = y
        self.width = width
        self.disparo = False
        self.limd = limd
        self.limi = limi

    def draw(self, screen):
        if(self.x > self.limd-self.width):
            self.x = self.limd-self.width
        if(self.x < self.limi):
            self.x = self.limi
        esc = pygame.transform.scale(IMG, (self.width, self.width))
        screen.blit(esc, (self.x, self.y))

##################################################################################

class Bala:
    def __init__(self, x, y, w, l, v):
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        self.vel = v
        self.alive = True

    def actualAlive(self):
        if(self.y<0):
            self.alive = False

    def draw(self, screen, color):
        self.actualAlive()
        if(self.alive):
            self.y -= self.vel
            pygame.draw.rect(screen, color, (self.x, self.y, self.w, self.l))