import pygame
import core.types as types
from core.resolver import ResolverPath 

class HitboxSprite:
    def __init__(self, path: str, color: "tuple[int, int, int]" = (255, 0, 0), tolerance: int = 0):
        self.__path = ResolverPath().resolve(path)
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
    
    def hit(self, coords: types.TCoord) -> bool:
        pixels = self.hitbox
        for i in range (len(pixels)):
            if (coords[0] == pixels[i][0] and
                coords[1] == pixels[i][1]
                ): return True
        return False

    def __str__(self):
        return f"{self.__path}@{self.__color}"


class Hitbox:
    def __init__(self, coords, size: tuple[int, int]):
        self.__coords = coords
        self.__size = size
        self.__hitbox = pygame.Rect(self.__coords[0], self.__coords[1], self.__size[0], self.__size[1])
    
    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, newCoords):
        self.__coords = newCoords
        self.__hitbox = pygame.Rect(self.__coords[0], self.__coords[1], self.__size[0], self.__size[1])

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, newSize):
        self.__size = newSize
        self.__hitbox = pygame.Rect(self.__coords[0], self.__coords[1], self.__size[0], self.__size[1])

    @property
    def hitbox(self):
        return self.__hitbox

    @hitbox.setter
    def hitbox(self, newHitbox):
        self.__hitbox = newHitbox
    
    def hit(self, coords) -> bool:
        return (((coords[0] == self.__coords[0] - self.__size[0] or 
                  coords[0] == self.__coords[0] + self.__size[0]) and 
                 (coords[1] >= self.__coords[1] - self.__size[1] and 
                  coords[1] <= self.__coords[1] + self.__size[1]))
                or
                ((coords[1] == self.__coords[1] + self.__size[1] or 
                  coords[1] == self.__coords[1] - self.__size[1]) and
                 (coords[0] >= self.__coords[0] - self.__size[0] and
                  coords[0] <= self.__coords[0] + self.__size[0])
                ))