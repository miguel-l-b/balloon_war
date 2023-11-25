import pygame
from pygame import *
from pygame.locals import *
from entities.shot import Shot
from core.hitbox import Hitbox
from entities.gun import Gun

class Player:  
  def __init__(
    self, 
    name: str, 
    color: pygame.Color, 
    initialCoords = (0, 0), 
    hp: int = 100, 
    gun: Gun = None,
    speed: int = 20,
    size: int = 40
    ):
    self.__alive = True
    self.__hp = hp
    self.__name = name
    self.__color = color
    self.__coords = initialCoords
    self.__size = size
    self.__speed = speed
    self.__hitbox = Hitbox(self.__coords, self.__size)
    self.__gun = gun
    self.__shots = gun.shots
    self.__gun.coords = self.__coords
    
  @property
  def alive(self):
    return self.__alive

  @alive.setter
  def alive(self, newAlive):
    self.__alive = newAlive

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

  @property
  def shots(self):
    return self.__shots
  
  @shots.setter
  def shots(self, newShots):
    self.__shots = newShots

  @property
  def gun(self):
    return self.__gun
  
  @gun.setter
  def gun(self, newGun):
    self.__gun = newGun

  def hit(self, coords) -> bool:
    return self.__hitbox.hit(coords)

  def moveUp(self, distance: int = 0):
    if (distance == 0):
      distance = self.__speed
    self.__coords = (self.__coords[0], self.__coords[1] - distance)
    self.gun.coords = self.__coords
    self.__hitbox.coords = self.__coordssd
  
  def moveDown(self, distance: int = 0):
    if (distance == 0):
      distance = self.__speed
    self.__coords = (self.__coords[0], self.__coords[1] + distance)
    self.gun.coords = self.__coords
    self.__hitbox.coords = self.__coords

  def shoot(self):
    if self.__gun != None:
      self.__gun.shoot()
      
  def removeShot(self, shot: Shot):
    self.__gun.removeShot(shot)

  def reload(self):
    if self.__gun != None:
      self.__gun.reload()
  
  def isInsideLimits(self, screen: Surface, coords = None):
    if (coords == None):
      coords = self.__coords
    return (coords[0] > 0 and
            coords[0] < screen.get_width() and
            coords[1] > 0 and 
            coords[1] < screen.get_height()
            )

  def die(self):
    self.__alive = False
    self.__size = 0
    self.__hitbox = None
    self.__alive = True
    self.__hp = 0
    self.__speed = 0
    self.__gun = None