import pygame
import core.types as types
from typing import Callable

from pygame import Surface

from core.entities import Entity, Sprite
from core.resolver import ManagerScenes, ResolverScript

TCallback = Callable[[Entity], None]

class BtnStart(types.Script):
  def __init__(self, frameNotHover: types.TFrame, frameHover: types.TFrame):
    self.__frameNotHover = frameNotHover
    self.__frameHover = frameHover

  def setup(self, owner: Entity):
    self._owner = owner
    self.__btnHandler = ResolverScript.getScript("button", self.click, self.hover, self.rollback_hover)
    self.__btnHandler.setup(owner)

  def click(self, owner: Entity):
    ManagerScenes().goTo("game")
  
  def hover(self, owner: Sprite):
    owner.sprite = self.__frameHover

  def rollback_hover(self, owner: Sprite):
    owner.sprite = self.__frameNotHover

  def loop(self, screen: Surface, delta_time: float):
    if pygame.key.get_pressed()[pygame.K_SPACE]:
      self.click(self._owner)
    else:
      self.__btnHandler.loop(screen, delta_time)