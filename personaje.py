import pygame
import math
from constantes import *

class Personaje():

    def __init__(self, x, y, frames, gun_image):

        self.frames = frames
        self.frame_actual = 0

        self.rect = self.frames[0].get_rect()
        self.rect.center = (x, y)

        self.velocidad = 5
        self.mirando_derecha = True

        # arma
        self.gun_image = gun_image

        # animación
        self.contador_animacion = 0
        self.velocidad_animacion = 10


    def mover(self):

        keys = pygame.key.get_pressed()
        moviendo = False

        if keys[pygame.K_a]:
            self.rect.x -= self.velocidad
            self.mirando_derecha = False
            moviendo = True

        if keys[pygame.K_d]:
            self.rect.x += self.velocidad
            self.mirando_derecha = True
            moviendo = True

        if keys[pygame.K_w]:
            self.rect.y -= self.velocidad
            moviendo = True

        if keys[pygame.K_s]:
            self.rect.y += self.velocidad
            moviendo = True


        if moviendo:

            self.contador_animacion += 1

            if self.contador_animacion >= self.velocidad_animacion:

                self.contador_animacion = 0
                self.frame_actual += 1

                if self.frame_actual >= len(self.frames):
                    self.frame_actual = 0

        else:
            self.frame_actual = 0


    def dibujar(self, ventana):

        imagen = self.frames[self.frame_actual]

        if not self.mirando_derecha:
            imagen = pygame.transform.flip(imagen, True, False)

        ventana.blit(imagen, self.rect)


        # =====================
        # PISTOLA
        # =====================

        mouse_x, mouse_y = pygame.mouse.get_pos()

        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery

        angulo = math.degrees(math.atan2(dy, dx))


        # elegir sprite del arma
        gun = self.gun_image

        if dx < 0:
            gun = pygame.transform.flip(self.gun_image, False, True)


        arma_rotada = pygame.transform.rotate(gun, -angulo)


        # posicionar arma delante del jugador
        distancia = 25

        offset_x = math.cos(math.radians(angulo)) * distancia
        offset_y = math.sin(math.radians(angulo)) * distancia


        arma_rect = arma_rotada.get_rect(
            center=(
                self.rect.centerx + offset_x,
                self.rect.centery + offset_y + 5
            )
        )

        ventana.blit(arma_rotada, arma_rect)