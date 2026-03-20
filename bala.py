import pygame
import math

class Bala():

    def __init__(self, x, y, angulo):

        self.x = x
        self.y = y
        self.angulo = angulo

        self.velocidad = 12

    def mover(self):

        self.x += math.cos(math.radians(self.angulo)) * self.velocidad
        self.y += math.sin(math.radians(self.angulo)) * self.velocidad

    def dibujar(self, ventana):

        pygame.draw.circle(ventana, (255, 255, 0), (int(self.x), int(self.y)), 4)