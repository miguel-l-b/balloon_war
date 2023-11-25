import core.types as types
import pygame

from core.entities import Text


class Fps(types.Script):
  def __init__(self, clock: pygame.time.Clock):
    super().__init__()
    self.clock = clock

  def setup(self, owner: Text):
    self.owner = owner
    
  def loop(self, _screen: pygame.Surface, delta_time: float):
    self.owner.setText = f"FPS: {self.clock.get_fps():.0f}"