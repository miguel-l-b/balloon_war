import random
import pygame
from core.entities import Sprite
from core.resolver import ResolverConfig
from core.scene import Scene
import core.types as types

class CloudMove(types.Script):
  def __init__(self, direction, scene: Scene, speed: int):
    super().__init__()
    self.speed = speed
    self.scene = scene
    self.direction = direction

  def setup(self, owner: Sprite):
    self.owner = owner
    self.limits = ResolverConfig.resolve()["window"]["dimension"]
    
  def loop(self, _screen: pygame.Surface, delta_time: float):
    distanceX = self.speed * delta_time
    distanceY =  self.speed * delta_time
    r = random.randint(0, 200)
    if 99 > r and r < 110:
      distanceY *= -0.2
  
    if 110 > r and r < 120:
      distanceY *= 0.2

    if r <= 99 or r >= 120:
      distanceY *= 0
    
    if self.direction == 0:
      self.owner.moving((distanceX, distanceY))
      if self.owner.coords[0] > self.limits[0]:
          self.scene.kill(self.owner.name)
    else:
      self.owner.moving((distanceX, distanceY))
      if self.owner.coords[1] > self.limits[1]:
          self.scene.kill(self.owner.name)