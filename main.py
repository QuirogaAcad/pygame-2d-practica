import pygame
import math
from constantes import *
from personaje import Personaje
from bala import Bala

pygame.init()

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mi juego")

# ==============================
# CARGAR SPRITES DEL PERSONAJE
# ==============================

player_frames = [
    pygame.image.load("assets/images/characters/player/0.png").convert_alpha(),
    pygame.image.load("assets/images/characters/player/1.png").convert_alpha(),
    pygame.image.load("assets/images/characters/player/2.png").convert_alpha()
]

# escalar sprites
for i in range(len(player_frames)):
    player_frames[i] = pygame.transform.scale(
        player_frames[i],
        (
            player_frames[i].get_width() * SCALAPERSONAJE,
            player_frames[i].get_height() * SCALAPERSONAJE
        )
    )

# ==============================
# CARGAR PISTOLA
# ==============================

gun_image = pygame.image.load("assets/images/weapons/gun.png").convert_alpha()
gun_image = pygame.transform.scale(gun_image, (40, 40))

# ==============================
# CARGAR TILES DEL MAPA
# ==============================

tiles = []

for i in range(1, 10):

    tile = pygame.image.load(f"assets/images/tiles/tile_v{i}.png").convert()
    tile = pygame.transform.scale(tile, (64, 64))

    tiles.append(tile)

# ==============================
# CREAR MAPA CON BORDES
# ==============================

MAPA_ANCHO = ANCHO_VENTANA // 64
MAPA_ALTO = ALTO_VENTANA // 64

mapa = []

for y in range(MAPA_ALTO):

    fila = []

    for x in range(MAPA_ANCHO):

        # esquinas
        if x == 0 and y == 0:
            tile = 0

        elif x == MAPA_ANCHO - 1 and y == 0:
            tile = 2

        elif x == 0 and y == MAPA_ALTO - 1:
            tile = 6

        elif x == MAPA_ANCHO - 1 and y == MAPA_ALTO - 1:
            tile = 8

        # bordes
        elif y == 0:
            tile = 1

        elif y == MAPA_ALTO - 1:
            tile = 7

        elif x == 0:
            tile = 3

        elif x == MAPA_ANCHO - 1:
            tile = 5

        # centro
        else:
            tile = 4

        fila.append(tile)

    mapa.append(fila)

clock = pygame.time.Clock()

centro_x = ANCHO_VENTANA // 2
centro_y = ALTO_VENTANA // 2

Jugador = Personaje(centro_x, centro_y, player_frames, gun_image)

# ==============================
# LISTA DE BALAS
# ==============================

balas = []

run = True
while run:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        # ==============================
        # DISPARO
        # ==============================

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_x, mouse_y = pygame.mouse.get_pos()

                dx = mouse_x - Jugador.rect.centerx
                dy = mouse_y - Jugador.rect.centery

                angulo = math.degrees(math.atan2(dy, dx))

                distancia = 35

                spawn_x = Jugador.rect.centerx + math.cos(math.radians(angulo)) * distancia
                spawn_y = Jugador.rect.centery + math.sin(math.radians(angulo)) * distancia

                balas.append(Bala(spawn_x, spawn_y, angulo))

    # ==============================
    # MOVER
    # ==============================

    Jugador.mover()

    for bala in balas:
        bala.mover()

    # ==============================
    # DIBUJAR
    # ==============================

    ventana.fill((0, 0, 0))

    # dibujar mapa
    for y in range(MAPA_ALTO):
        for x in range(MAPA_ANCHO):

            tile = tiles[mapa[y][x]]

            ventana.blit(tile, (x * 64, y * 64))

    # jugador
    Jugador.dibujar(ventana)

    # balas
    for bala in balas:
        bala.dibujar(ventana)

    pygame.display.update()

pygame.quit()