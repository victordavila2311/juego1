import sys, pygame, os

current_path = os.path.dirname(__file__)
IMGV = pygame.image.load(os.path.join(current_path, 'alienverde2.jpg'))
IMGM = pygame.image.load(os.path.join(current_path, 'alienmorado.jpg'))
IMGR = pygame.image.load(os.path.join(current_path, 'alienrojo.jpg'))
IMGJ = pygame.image.load(os.path.join(current_path, 'alienjefe.jpg'))

class Enemigo:
    def __init__(self, xo, x, y, w):
        self.xo = xo
        self.x = x
        self.y = y
        self.w = w
        self.volando = False
        self.reversa = False
        self.alive = True

    def draw(self, screen, cambio):
        if(self.x >= self.xo+(5*self.w)):
            self.reversa = True
        if(self.x <= self.xo):
            self.reversa = False
        if self.alive:
            if self.reversa:
                self.x -= cambio
                esc = pygame.transform.scale(IMG, (self.w, self.w))
                screen.blit(esc, (self.x, self.y))
            else:
                self.x += cambio
                esc = pygame.transform.scale(IMG, (self.w, self.w))
                screen.blit(esc, (self.x, self.y))

    def collision(self, other):
        if(other.x >= self.x) and (other.x <= self.x+self.w) and (other.y >= self.y) and (other.y <= self.y+self.w):
            self.alive = False
            other.alive = False

class Morado(Enemigo):
    def __init__(self, xo, x, y, w):
        Enemigo.__init__(self, xo, x, y, w)

    def draw(self, screen, cambio):
        if(self.x >= self.xo+(7*self.w)):
            self.reversa = True
        if(self.x <= self.xo):
            self.reversa = False
        if self.alive:
            if self.reversa:
                self.x -= cambio
                esc = pygame.transform.scale(IMGM, (self.w, self.w))
                screen.blit(esc, (self.x, self.y))
            else:
                self.x += cambio
                esc = pygame.transform.scale(IMGM, (self.w, self.w))
                screen.blit(esc, (self.x, self.y))

class Verde(Enemigo):
    def __init__(self, xo, x, y, w):
        Enemigo.__init__(self, xo, x, y, w)

    def draw(self, screen, cambio):
        if(self.x >= self.xo+(5*self.w)):
            self.reversa = True
        if(self.x <= self.xo):
            self.reversa = False
        if self.alive:
            if self.reversa:
                self.x -= cambio
                esc = pygame.transform.scale(IMGV, (self.w, self.w))
                screen.blit(esc, (self.x, self.y))
            else:
                self.x += cambio
                esc = pygame.transform.scale(IMGV, (self.w, self.w))
                screen.blit(esc, (self.x, self.y))

class Rojo(Enemigo):
    def __init__(self, xo, x, y, w):
        Enemigo.__init__(self, xo, x, y, w)

    def draw(self, screen, cambio):
        if(self.x >= self.xo+(7*self.w)):
            self.reversa = True
        if(self.x <= self.xo):
            self.reversa = False
        if self.alive:
            if self.reversa:
                self.x -= cambio
                esc = pygame.transform.scale(IMGR, (self.w, self.w))
                screen.blit(esc, (self.x, self.y))
            else:
                self.x += cambio
                esc = pygame.transform.scale(IMGR, (self.w, self.w))
                screen.blit(esc, (self.x, self.y))

class Jefe(Enemigo):
    def __init__(self, xo, x, y, w):
        Enemigo.__init__(self, xo, x, y, w)

    def draw(self, screen, cambio):
        if(self.x >= self.xo+(7*self.w)):
            self.reversa = True
        if(self.x <= self.xo):
            self.reversa = False
        if self.alive:
            if self.reversa:
                self.x -= cambio
                esc = pygame.transform.scale(IMGJ, (self.w, self.w))
                screen.blit(esc, (self.x, self.y))
            else:
                self.x += cambio
                esc = pygame.transform.scale(IMGJ, (self.w, self.w))
                screen.blit(esc, (self.x, self.y))