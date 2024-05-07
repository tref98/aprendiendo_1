import pygame
import random
import math
from pygame import mixer

# inicializar pygame
pygame.init()


# crear pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption('Invasion Espacial')
icono = pygame.image.load("astronave.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('starry-night-sky.jpg')

# agrgar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

# variables Jugador
img_jugador = pygame.image.load('nave-espacial.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0


# variables enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8
enemigo_y_aumento = 0


for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('ovni.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(0, 100))
    enemigo_x_cambio.append(1)
    enemigo_y_cambio.append(50)


# variables bala
img_bala = []
bala_x = []
bala_y = []
bala_x_cambio = []
bala_y_cambio = []
bala_visible = {}
cantidad_municion = 100
municion_total = 100


for i in range(cantidad_municion):
    img_bala.append(pygame.image.load('descarga.jpg'))
    bala_x.append(0)
    bala_y.append(1000)
    bala_x_cambio.append(0)
    bala_y_cambio.append(2)
    bala_visible[i] = False


# puntaje
puntaje = 0
puntaje_cambio = 10
fuente = pygame.font.Font('SouthernAire_Personal_Use_Only.ttf', 32)
fuente2 = pygame.font.Font('AQUATIC.ttf', 100)
texto_x = 10
texto_y = 10

# texto final de juego
fuente_final = pygame.font.Font('AQUATIC.ttf', 100)


def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    texto2 = fuente2.render(f'puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto2, (150, 300))
    pantalla.blit(mi_fuente_final, (150, 200))


# funcion mostar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f'puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# funcion bala
def disparar_bala(x, y, bal):
    global bala_visible
    bala_visible[bal] = True
    pantalla.blit(img_bala[bal], (x+27, y+10))


# funcion colicion
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego
se_ejecuta = True
while se_ejecuta:

    # color fondo pantalla
    # pantalla.fill((12, 148, 53))
    # imagen de fondo
    pantalla.blit(fondo, (0, 0))

    # iterar eventos
    for evento in pygame.event.get():
        # evento cerar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            # flecha izquierda
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1.5
            # felcha derecha
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1.5
            # barra espaciadora
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                municion_total -= 1
                if municion_total <0:
                    municion_total = 0
                else:
                    if not bala_visible[municion_total]:
                        bala_x[municion_total] = jugador_x
                        bala_y[municion_total] = jugador_y
                        disparar_bala(bala_x[municion_total], bala_y[municion_total], municion_total)
                        sonido_bala.play()
        # evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # cambio posicion jugador
    jugador_x += jugador_x_cambio

    # cambio posicion enemigo
    enemigo_x += enemigo_x_cambio

    # mantener limite pantalla al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # aumento velocidad enemigos
    if puntaje == puntaje_cambio:
        puntaje_cambio += 10
        enemigo_y_aumento += 0.1

    # modificar ubicacion del enemigo
    for e in range(cantidad_enemigos):

        # fin del juego
        if enemigo_y[e] > 451:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]

        # mantener limite pantalla al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1 + enemigo_y_aumento
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1 - enemigo_y_aumento
            enemigo_y[e] += enemigo_y_cambio[e]
        # colision
        for i in range(cantidad_municion):
            colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x[i], bala_y[i])
            if colision:
                sonido_colision = mixer.Sound('Golpe.mp3')
                sonido_colision.play()
                bala_y[i] = 1000
                bala_visible[i] = False
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(-100, 50)
                municion_total += 1

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # movimiento bala
    for i in range(cantidad_municion):
        if bala_y[i] <= -20:
            bala_y[i] = 1000
            bala_visible[i] = False
            municion_total += 1

        if bala_visible[i]:
            disparar_bala(bala_x[i], bala_y[i], i)
            bala_y[i] -= bala_y_cambio[i]

    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)


# Actualizar los pixeles de la pantalla
    pygame.display.update()
