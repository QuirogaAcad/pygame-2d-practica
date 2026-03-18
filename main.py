import pygame
from constantes import *
from personaje import Personaje

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

clock = pygame.time.Clock()

centro_x = ANCHO_VENTANA // 2
centro_y = ALTO_VENTANA // 2

# ahora pasamos la lista de sprites
Jugador = Personaje(centro_x, centro_y, player_frames)

run = True
while run:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Jugador.mover()

    ventana.fill((0, 0, 0))
    Jugador.dibujar(ventana)

    pygame.display.update()

pygame.quit()