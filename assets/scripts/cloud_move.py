import random
import pygame
from core.entities import Sprite
from core.resolver import ResolverConfig
from core.scene import Scene
import core.types as types

class CloudMove(types.Script):
  def __init__(self, direction, scene: Scene, speed: int):
    super().__init__()
    self.__speed = speed
    self.__scene = scene
    self.__direction = direction

  def setup(self, owner: Sprite):
    self.__owner = owner
    self.__limits = ResolverConfig.resolve()["window"]["dimension"]
    
  def loop(self, _screen: pygame.Surface, delta_time: float):
    distanceX = self.__speed * delta_time
    
    if self.__direction == 0:
      self.__owner.moving((distanceX, 0))
      if self.__owner.coords[0] > self.__limits[0]:
          self.__scene.kill(self.__owner.name)
    else:
      self.__owner.moving((distanceX, 0))
      if self.__owner.coords[1] > self.__limits[1]:
          self.__scene.kill(self.__owner.name)