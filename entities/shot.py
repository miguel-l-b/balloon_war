import pygame
from entities.hitbox import Hitbox
class Shot():
    def __init__(self, color: pygame.color, initialCoords = (0, 0), radius: float = 10, speed: int = 10):
        self.__color = color
        self.__coords = initialCoords
        self.__radius = radius
        self.__speed = speed
        self.__hitbox = Hitbox(self.__coords, self.__radius)

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, newCoords):
        self.__coords = newCoords

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, newColor):
        self.__color = newColor

    @property
    def radius(self):
        return self.__radius

    @radius.setter    
    def radius(self, newRadius):
        self.__radius = newRadius

    @property
    def speed(self):
        return self.__speed

    @speed.setter    
    def speed(self, newSpeed):
        self.__speed = newSpeed

    def hit(self, coords) -> bool:
        return self.__hitbox.hit(coords)

    def moveLeft(self, distance):
        self.__coords = (self.__coords[0] - distance, self.__coords[1])
    
    def moveRight(self, distance):
        self.__coords = (self.__coords[0] + distance, self.__coords[1])