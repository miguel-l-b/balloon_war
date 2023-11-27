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
    image_path: str,
    initialCoords: tuple[int, int],
    hp: int = 100, 
    gun: Gun = None,
    speed: int = 20,
    size:tuple[int, int] = (40, 40)
    ):
    self.__alive = True
    self.__hp = hp
    self.__name = name
    self.__image_path = image_path
    self.__coords = initialCoords
    self.__size = size
    self.__speed = speed

    self.__gun = gun
    self.__shots = gun.shots
    self.__gun.coords = self.__coords
    
    self.__hitbox_coords = (self.__coords[0] + 40, self.__coords[1] + 10)
    self.__hitbox_size = (self.__size[0] + 10, self.__size[1] + 20)
    self.__hitbox = Hitbox(self.__hitbox_coords, self.__hitbox_size)
    
    self.__current_speed_up = 0
    self.__current_speed_down = 0
    self.__is_moving_up = False

  @property
  def name(self): 
    return self.__name
  
  @name.setter
  def name(self, newName):
    self.__name = newName

  @property
  def image_path(self):
    return self.__image_path
  
  @image_path.setter
  def image_path(self, newImagePath):
    self.__image_path = newImagePath

  @property
  def coords(self):
    return self.__coords
  
  @coords.setter
  def coords(self, newCoords):
    self.__coords = newCoords
  
  @property
  def alive(self):
    return self.__alive

  @alive.setter
  def alive(self, newAlive):
    self.__alive = newAlive

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
  def current_speed_up(self):
    return self.__current_speed_up

  @speed.setter
  def current_speed_up(self, newCurrentSpeedUp):
    self.__current_speed_up = newCurrentSpeedUp

  @property
  def current_speed_down(self):
    return self.__current_speed_down

  @speed.setter
  def current_speed_down(self, newCurrentSpeedDown):
    self.__current_speed_down = newCurrentSpeedDown

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

  @property
  def is_moving_up(self):
      return self.__is_moving_up

  @is_moving_up.setter
  def is_moving_up(self, value):
      self.__is_moving_up = value

  @property
  def hitbox(self): 
    return self.__hitbox
  
  @hitbox.setter
  def hitbox(self, newhitbox):
    self.__hitbox = newhitbox
  
  def hit(self, coords) -> bool:
    return self.__hitbox.hit(coords)

  def moveUp(self, gravity: float = 0):
    if self.__current_speed_up == 0 and not self.__is_moving_up:
      self.__is_moving_up = True
      self.__current_speed_up = self.__speed
      self.__current_speed_down = 0
    
    if self.__current_speed_up <= 0 and self.__is_moving_up:
      self.__is_moving_up = False
      self.__current_speed_up = 0
    else:
      self.__current_speed_up -= gravity

    self.__coords = (self.__coords[0], self.__coords[1] - self.__current_speed_up)
    self.gun.coords = self.__coords
    self.__hitbox_coords = (self.__coords[0] + 40, self.__coords[1] + 10)
    self.hitbox.coords = self.__hitbox_coords
  
  def moveDown(self, gravity: float = 0):
    self.__current_speed_down += gravity

    self.__coords = (self.__coords[0], self.__coords[1] + self.__current_speed_down)
    self.gun.coords = self.__coords
    self.__hitbox_coords = (self.__coords[0] + 40, self.__coords[1] + 10)
    self.hitbox.coords = self.__hitbox_coords

  def shoot(self):
    if self.__gun != None:
      self.__gun.shoot()
      
  def removeShot(self, shot: Shot):
    self.__gun.removeShot(shot)

  def reload(self):
    if self.__gun != None:
      self.__gun.reload()
  
  def isInsideLimitsTop(self, screen: Surface, coords = None):
    if (coords == None):
      coords = self.__coords
    return (coords[1] > 0)

  def isInsideLimitsBottom(self, screen: Surface, coords = None):
    if (coords == None):
      coords = self.__coords
    return (coords[1] < screen.get_height())

  def isInsideLimits(self, screen: Surface, coords = None):
    return self.isInsideLimitsTop(screen, coords) and self.isInsideLimitsBottom(screen, coords)

  def die(self):
    self.__alive = False
    self.__size = (0, 0)
    self.__hitbox = None
    self.__alive = True
    self.__hp = 0
    self.__speed = 0
    self.__gun = None