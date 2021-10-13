import sys, pygame
from nave import Nave, Bala
from enemigos import Enemigo, Morado, Verde, Rojo, Jefe
pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
factorvel = 4
nivel = 1
puntaje = 0

pygame.display.set_caption("primer juego")
run = True
contador = 0
actual = 1
negro = 0,0,0
blanco = 255,255,255
azul = 0,0,255
rojo = 255,0,0
verde = 0,255,0
x = size[0]/2
y = size[1]/2
width = 30
speedx = 0
speedy = 0
velalien = 0.2*factorvel
cambio = 0.5*factorvel
cuads = []
bala = Bala(0, 0, 5, 10, cambio+0.7)
bala.alive = False
navewidth = 70
alienwidth = 35
nave = Nave(size[0]/2, size[1]-navewidth, navewidth, size[0], 0)
aliens = []
#se inician los aliens
def generarAliens(aliensarr):
    aliensarr.append(Jefe((6 * alienwidth) + (10 * (3.5)), (6 * alienwidth) + (10 * (3.5)), alienwidth, alienwidth - 10))
    aliensarr.append(Jefe((10 * alienwidth) + (10 * (3.5)), (10 * alienwidth) + (10 * (3.5)), alienwidth, alienwidth - 10))

    for i in range(0, 6):
        aliensarr.append(Rojo((5 * alienwidth) + (10 * (i + 2.5)) + (alienwidth * i),
                           (5 * alienwidth) + (10 * (i + 2.5)) + (alienwidth * i), 2 * alienwidth, alienwidth - 10))

    for i in range(0, 8):
        aliensarr.append(Morado((4 * alienwidth) + (10 * (i + 1.5)) + (alienwidth * i),
                             (4 * alienwidth) + (10 * (i + 1.5)) + (alienwidth * i), 3 * alienwidth, alienwidth - 10))

    for j in range(0, 10):
        for i in range(0, 3):
            aliensarr.append(
                Verde((3 * alienwidth) + (10 * j) + (alienwidth * j), (3 * alienwidth) + (10 * j) + (alienwidth * j),
                      (4 * alienwidth) + (10 * i) + (i * alienwidth), alienwidth))

generarAliens(aliens)
#loop central del juego
def displayText(frase, x,y):
    font = pygame.font.Font('freesansbold.ttf', 15)

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(frase, True, verde, azul)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (x// 2, y // 2)
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    screen.blit(text, (x//2,y//2))

while run:
    screen.fill(negro)
    displayText("Nivel: "+str(nivel),10,10)
    displayText("Puntaje: "+ str(puntaje), 2*x,10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedx = -cambio
            if event.key == pygame.K_RIGHT:
                speedx = cambio
            if event.key == pygame.K_SPACE:
                if(not nave.disparo):
                    bala.x = nave.x+(nave.width/2)-(bala.w/2)
                    bala.y = nave.y-(bala.l)
                    bala.alive = True
                    nave.disparo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                speedx = 0

    nave.x += speedx
    if(not bala.alive):
        nave.disparo = False
        bala.x = 0
        bala.y = 0
    else:
        bala.draw(screen, blanco)
    nave.draw(screen)
    if len(aliens) == 0:
        nivel+=1
        generarAliens(aliens)
    for alien in aliens:
        if not alien.alive:
            aliens.remove(alien)
        alien.draw(screen, velalien)
        if alien.collision(bala):
            puntaje += alien.puntaje
    pygame.display.update()
    #print("puntaje: ",puntaje," Nivel: ",nivel)

pygame.quit()