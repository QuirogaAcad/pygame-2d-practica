import pygame
from constantes import *

class Personaje():

    def __init__(self, x, y, frames):

        self.frames = frames
        self.frame_actual = 0
        self.image = self.frames[self.frame_actual]

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.velocidad = 5
        self.mirando_derecha = True

        # control de animación
        self.contador_animacion = 0
        self.velocidad_animacion = 10


    def mover(self):

        keys = pygame.key.get_pressed()
        moviendo = False

        if keys[pygame.K_a]:  # izquierda
            self.rect.x -= self.velocidad
            self.mirando_derecha = False
            moviendo = True

        if keys[pygame.K_d]:  # derecha
            self.rect.x += self.velocidad
            self.mirando_derecha = True
            moviendo = True

        if keys[pygame.K_w]:  # arriba
            self.rect.y -= self.velocidad
            moviendo = True

        if keys[pygame.K_s]:  # abajo
            self.rect.y += self.velocidad
            moviendo = True


        # animación solo si se mueve
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