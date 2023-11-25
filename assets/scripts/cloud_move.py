import pygame
from pygame import Vector2
from core.entities import Entity
import core.types as types

class CloudMove(types.Script):
  def __init__(self):
    super().__init__()

  def setup(self, owner: Entity, data: types.TDataScript = None):
    self.owner = owner
    self.data = data

  def loop(self, screen: pygame.Surface, delta_time: float):
    move = Vector2(50, 10) * delta_time
    self.owner.moving((move.x, move.y))