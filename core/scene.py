import pygame
from pygame import *

import core.types as types
from core.entities import Entity
from core.resolver import ResolverConfig

class Scene:
  def __init__(self, screen: Surface) -> None:
    self._screen = screen
    self.__objects: list[Entity] = []
    self._clock = pygame.time.Clock()
    self._limitFPS = ResolverConfig.resolve()["game"]["frameRate"]

  def get(self, name: str) -> Entity:
    for obj in self.__objects:
      if obj.name == name:
        return obj
    raise Exception(f"Object with name {name} not found")

  def spawn(self, obj: any):
    for o in self.__objects:
      if o.name == obj.name:
        raise Exception(f"Object with name {obj.name} already exists")
    self.__objects.append(obj)
  
  def kill(self, name: str):
    for obj in self.__objects:
      if obj.name == name:
        self.__objects.remove(obj)
        break

  def __draw(self):
    self._screen.fill(ResolverConfig.resolve()["game"]["colors"]["cyan"])
    zGroups: list[types.zGroup] = []

    for obj in self.__objects:
      if obj.z not in zGroups:
        zGroups.append(obj.z)

    zGroups.sort()

    for zGroup in zGroups:
      for obj in self.__objects:
        if obj.z == zGroup:
          obj.update(self._screen)


  def loop(self):
    while True:
      self.__draw()
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          exit()
      
      self._clock.tick(self._limitFPS)