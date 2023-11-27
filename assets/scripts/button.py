from typing import Callable
import pygame
from pygame import Surface
from core.entities import Entity
import core.types as types

TCallback = Callable[[Entity], None]

class Button(types.Script):
  def __init__(self, click: TCallback = None, hover: TCallback = None, rollback_hover: TCallback = None):
    self.__click = click
    self.__hover = hover
    self.__rollback_hover = rollback_hover

  def setup(self, owner: Entity):
    self.__owner = owner

  def loop(self, _screen: Surface, _delta_time: float):
    mouse = pygame.mouse.get_pos()
    if self.__owner.rect.collidepoint(mouse):
      if self.__hover is not None:
        self.__hover(self.__owner)
      if pygame.mouse.get_pressed()[0]:
        if self.__click is not None:
          self.__click(self.__owner)
    else:
      if self.__rollback_hover is not None:
        self.__rollback_hover(self.__owner)