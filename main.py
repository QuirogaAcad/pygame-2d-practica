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

# escalar todos los sprites
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

clock = pygame.time.Clock()

centro_x = ANCHO_VENTANA // 2
centro_y = ALTO_VENTANA // 2

# ahora pasamos sprites + pistola
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
        # DISPARO CON MOUSE
        # ==============================

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:  # click izquierdo

                mouse_x, mouse_y = pygame.mouse.get_pos()

                dx = mouse_x - Jugador.rect.centerx
                dy = mouse_y - Jugador.rect.centery

                angulo = math.degrees(math.atan2(dy, dx))

                # distancia hasta la punta del arma
                distancia = 35

                spawn_x = Jugador.rect.centerx + math.cos(math.radians(angulo)) * distancia
                spawn_y = Jugador.rect.centery + math.sin(math.radians(angulo)) * distancia

                balas.append(Bala(spawn_x, spawn_y, angulo))

    # mover jugador
    Jugador.mover()

    # mover balas
    for bala in balas:
        bala.mover()

    ventana.fill((0, 0, 0))

    # dibujar jugador
    Jugador.dibujar(ventana)

    # dibujar balas
    for bala in balas:
        bala.dibujar(ventana)

    pygame.display.update()

pygame.quit()