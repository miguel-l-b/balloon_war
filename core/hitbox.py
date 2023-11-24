import pygame
import core.types as types
from core.resolver import ResolverPath 

class HitboxSprite:
    def __init__(self, path: str, color: "tuple[int, int, int]" = (255, 0, 0), tolerance: int = 0):
        self.__path = ResolverPath(path)
        self.__color = color
        self.__tolerance = tolerance

    @property
    def path(self):
        return self.__path
    
    @property
    def color(self):
        return self.__color
    

    @property
    def hitbox(self) -> "list[types.TCoord]":
        pixels = []
        img = pygame.image.load(self.__path)
        for x in range(img.get_width()):
            for y in range(img.get_height()):
                if img.get_at((x, y)) == self.__color:
                    pixels.append((x, y))
        return pixels
    
    def __str__(self):
        return f"{self.__path}@{self.__color}"


class Hitbox:
    def __init__(self, coords, size):
        self.__coords = coords
        self.__size = size
        self.__hitbox = pygame.Rect(self.__coords[0], self.__coords[1], self.__size, self.__size)
    
    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, newCoords):
        self.__coords = newCoords
    
    def hit(self, coords) -> bool:
        return (((coords[0] == self.__coords[0] - self.__size or 
                  coords[0] == self.__coords[0] + self.__size) and 
                 (coords[1] >= self.__coords[1] - self.__size and 
                  coords[1] <= self.__coords[1] + self.__size))
                or
                ((coords[1] == self.__coords[1] + self.__size or 
                  coords[1] == self.__coords[1] - self.__size) and
                 (coords[0] >= self.__coords[0] - self.__size and
                  coords[0] <= self.__coords[0] + self.__size)
                ))