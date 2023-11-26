import pygame
import core.types as types
from core.entities import Entity

class ButtonRect(types.Script):
  def __init__(self, hover = None, click = None):
    self._hover = hover
    self._click = click

  def setup(self, owner: Entity):
    self.owner = owner

  def loop(self, screen: types.TFrame, delta: float):
    if self.owner.rect:
      if self._hover is not None:
        self._hover(self.owner)
      if pygame.mouse.get_pressed()[0]:
        if self._click is not None:
          self._click(self.owner)
    pass