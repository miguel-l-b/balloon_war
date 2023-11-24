from typing import TypedDict
import pygame
from core.resolver import ResolverPath
from typing import TypedDict

class TDimension(TypedDict):
  width: int
  height: int
  rows: int
  columns: int

class SpriteSlicer(object):
    def __init__(self, file_name: str, dimensions: TDimension, stopWithSprite: int = 1):
      self.__file_name = file_name
      self.__dimensions = dimensions
      self.__amount = stopWithSprite
      self.__sprites: list[pygame.Surface] = []
      self.__load()

    def __load(self):
      image = pygame.image.load(ResolverPath.resolve(self.__file_name))
      rows = -1
      columns = -1
      for i in range(self.__amount):
        if columns < self.__dimensions["columns"]-1:
          columns += 1
          if rows == -1:
            rows += 1
        elif rows < self.__dimensions["rows"]-1:
          rows += 1
        else:
          raise Exception("SpriteSlicer: The amount of sprites is greater than the amount of rows and columns.")
        self.__sprites.append(
          image.subsurface(
            pygame.Rect(
              columns * self.__dimensions["width"],
              rows * self.__dimensions["height"],
              self.__dimensions["width"],
              self.__dimensions["height"]
            )
          )
        )
        
    def getAll(self) -> "list[pygame.Surface]":
      return self.__sprites
    
    def get(self, index: int) -> pygame.Surface:
      if(index < 0 or index > len(self.__sprites)-1):
        raise Exception("SpriteSlicer: The index is greater than the amount of sprites.")
      return self.__sprites[index]