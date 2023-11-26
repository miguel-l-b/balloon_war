import pygame
from core.hitbox import Hitbox
class Shot():
    def __init__(
        self,
        image_path: str,
        color: pygame.color,
        initialCoords = (0, 0), 
        size: tuple[int, int] = (10, 10), 
        speed: int = 10
        ):
        self.__image_path = image_path
        self.__color = color
        self.__coords = initialCoords
        self.__size = size
        self.__speed = speed
        self.__hitbox = Hitbox(self.__coords, (self.__size[0], self.__size[1]))

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, newCoords):
        self.__coords = newCoords

    @property
    def image_path(self):
        return self.__image_path

    @image_path.setter
    def image_path(self, newImagePath):
        self.__image_path = newImagePath

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, newColor):
        self.__color = newColor

    @property
    def size(self):
        return self.__size

    @size.setter    
    def size(self, newSize):
        self.__size = newSize

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