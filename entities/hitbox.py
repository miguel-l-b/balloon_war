import pygame 

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