import pygame
from entities.shot import Shot
from entities.hitbox import Hitbox
from pygame.locals import *

class Player():  
  def __init__(self, name: str, color: pygame.Color, initialCoords = (0, 0), hp: int = 100, size: int = 40, speed: int = 20):
    self.__hp = hp
    self.__name = name
    self.__color = color
    self.__coords = initialCoords
    self.__size = size
    self.__speed = speed
    self.__hitbox = Hitbox(self.__coords, self.__size)
    self.__shots = []
  
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

  @property
  def speed(self):
    return self.__speed

  @speed.setter
  def speed(self, newSpeed):
    self.__speed = newSpeed

  @property
  def shots(self):
    return self.__shots
  
  @shots.setter
  def shots(self, newShots):
    self.__shots = newShots

  def hit(self, coords) -> bool:
    return self.__hitbox.hit(coords)

  def moveUp(self, distance: int = 0):
    if (distance == 0): 
      distance = self.__speed
    self.__coords = (self.__coords[0], self.__coords[1] - distance)
    self.__hitbox.coords = self.__coords
  
  def moveDown(self, distance: int = 0):
    if (distance == 0):
      distance = self.__speed
    self.__coords = (self.__coords[0], self.__coords[1] + distance)
    self.__hitbox.coords = self.__coords

  def shoot(self, color: pygame.Color,  speed: int = 10, radius: float = 10):
    self.__shots.append(Shot(color, self.__coords, radius, speed))
  
  def findShot(self, shot: Shot):
    try:
      return self.__shots.index(shot)
    except:
      return -1