import pygame
from pygame import *

from core.entities import Entity
from core.resolver import ResolverConfig

class Scene:
  def __init__(self, screen: Surface) -> None:
    self._screen = screen
    self._limitFPS = ResolverConfig.resolve()["game"]["frameRate"]

  def draw(self):
    self._screen.fill(ResolverConfig.resolve()["game"]["colors"]["cyan"])
    for obj in self._objects:
        obj.update(self._screen)

  def loop(self):
    while True:
      self.draw()
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          exit()
      
      pygame.time.Clock().tick(self._limitFPS)