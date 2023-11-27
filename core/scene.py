import pygame
from pygame import *

import core.types as types
from core.entities import Entity
from core.resolver import ResolverConfig, Logger

  

class Scene(types.Scene):
  def __init__(self, screen: Surface) -> None:
    self._screen = screen
    self._backgroundColor = ResolverConfig.resolve()["game"]["colors"].get("background", (255, 255, 255))
    self.__objects: list[Entity] = []
    self._clock = pygame.time.Clock()
    self._limitFPS = ResolverConfig.resolve()["game"]["frameRate"]
    self._stop = False

  def start(self):
    self.__loop()

  def stop(self):
    self._stop = True

  def get(self, name: str) -> Entity:
    for obj in self.__objects:
      if obj.name == name:
        return obj
    raise Exception(f"Object with name {name} not found")

  def spawn(self, obj: any):
    for o in self.__objects:
      if o.name == obj.name:
        raise Exception(f"Object with name {obj.name} already exists")
    Logger.debug(self.__class__.__name__, f"Spawned {obj.name}")
    self.__objects.append(obj)
  
  def kill(self, name: str):
    for obj in self.__objects:
      if obj.name == name:
        Logger.debug(self.__class__.__name__, f"Killed {obj.name}")
        self.__objects.remove(obj)
        break

  def _draw(self):
    self._screen.fill(self._backgroundColor)
    zGroups: list[types.zGroup] = []

    for obj in self.__objects:
      if obj.z not in zGroups:
        zGroups.append(obj.z)

    zGroups.sort()

    for zGroup in zGroups:
      for obj in self.__objects:
        if obj.z == zGroup:
          obj.update(self._screen)


  def __loop(self):
    while not self._stop:
      self._draw()
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          exit()
      
      self._clock.tick(self._limitFPS)

class SceneLoader(types.Scene):
  def __init__(self, screen: Surface) -> None:
    self._screen = screen
    self._backgroundColor = ResolverConfig.resolve()["game"]["colors"].get("background", (255, 255, 255))
    self.__objects: list[Entity] = []
    self._clock = pygame.time.Clock()
    self._limitFPS = ResolverConfig.resolve()["game"]["frameRate"]
    self._stop = False

  @property
  def isFinished(self):
    return self._isFinished
  
  def stop(self):
    self._stop = True

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

  def _draw(self):
    self._screen.fill(self._backgroundColor)
    zGroups: list[types.zGroup] = []

    for obj in self.__objects:
      if obj.z not in zGroups:
        zGroups.append(obj.z)

    zGroups.sort()

    for zGroup in zGroups:
      for obj in self.__objects:
        if obj.z == zGroup:
          obj.update(self._screen)
  
  def start(self):
    self.__loop()
  
  def __loop(self):
    while not self.isFinished:
      self._draw()
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          exit()
      
      self._clock.tick(self._limitFPS)