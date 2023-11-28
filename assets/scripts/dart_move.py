import pygame
from core.entities import Entity
from core.resolver import ResolverCoords
from core.scene import Scene
import core.types as types

class DartMove(types.Script):
  def __init__(self, scene: Scene, speed: int, gravity: float, direction: int):
    super().__init__()
    self._speed = speed
    self._gravity = gravity
    self._direction = direction
    self._scene = scene

  def setup(self, owner: Entity):
    self._owner = owner
    self._limits = ResolverCoords.getSizeScreen()
    self._velocity = 0

  def calculateInercie(self, oldVelocity: float, increment: float, delta_time: float):
    increment = -increment if self._direction == 1 else increment
    return oldVelocity + (increment * delta_time)

  def loop(self, _screen: pygame.Surface, delta_time: float):
    self._velocity = self.calculateInercie(self._velocity, self._speed, delta_time)
    self._owner.moving((self._velocity, self._gravity * delta_time))

    print(self._owner.coords[0])
    if self._owner.coords[0] < 0 or self._owner.coords[0] > self._limits[0]:
      self._scene.kill(self._owner)