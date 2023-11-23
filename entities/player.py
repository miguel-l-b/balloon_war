import pygame
from entities.shot import Shot
from pygame.locals import *

class Player():  
  def __init__(self, name: str, color: pygame.Color, initialCoords = (0, 0), hp: int = 100, shape: str = "snake", hitbox = (40, 40)):
    self.__hp = hp
    self.__name = name
    self.__color = color
    self.__coords = initialCoords
    self.__shape = shape
    self.shots = []
    self.__hitbox = pygame.Rect(self.__coords[0], self.__coords[1], hitbox[0], hitbox[1])
  
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
  def hp(self):
    return self.__hp

  @hp.setter
  def hp(self, newHp):
    self.__hp = newHp

  def isInHitBox(self, coords):
    return (coords[0] == self.__coords[0] + 40 or 
            coords[0] == self.__coords[0] - 40 or 
            coords[1] == self.__coords[1] + 40 or 
            coords[1] == self.__coords[1] - 40)

  def moveUp(self, distance):
    self.__coords = (self.__coords[0], self.__coords[1] - distance)
  
  def moveDown(self, distance):
    self.__coords = (self.__coords[0], self.__coords[1] + distance)

  def shoot(self, color: pygame.Color, radius: float = 10, speed: int = 10):
    self.shots.append(Shot(color, self.__coords, radius, speed))