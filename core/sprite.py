import pygame
from core.resolver import ResolverPath
import core.types as types

class SpriteSlicer:
    def __init__(self, file_name: str, dimensions: types.TDimension, stopWithSprite: int = None, resize: types.TSize = None):
      self.__file_name = file_name
      self.__dimensions = dimensions
      if stopWithSprite == None:
        self.__amount = self.__dimensions["rows"] * self.__dimensions["columns"]
      else:
        self.__amount = stopWithSprite
      self.__sprites: list[pygame.Surface] = []
      self.__resize = resize
      self.__load()

    @property
    def amount(self) -> int:
      return self.__amount
    
    @property
    def dimensions(self) -> types.TDimension:
      return {
        "width": self.__resize[0] or self.__dimensions["width"],
        "height": self.__resize[1] or self.__dimensions["height"],
        "rows": self.__dimensions["rows"],
        "columns": self.__dimensions["columns"]
      }

    def __load(self):
      image = pygame.image.load(ResolverPath.resolve(self.__file_name))
      rows = -1
      columns = -1
      for i in range(self.__amount):
          if columns == self.__dimensions["columns"] - 1:
              columns = 0
              rows += 1
          elif columns < self.__dimensions["columns"] - 1:
              columns += 1
              if rows == -1:
                  rows += 1
          elif rows < self.__dimensions["rows"] - 1:
              rows += 1
          else:
              raise Exception("SpriteSlicer: The amount of sprites is greater than or equal to the amount of rows and columns.")
          if self.__resize != None:
            self.__sprites.append(
              pygame.transform.scale(
                image.subsurface(
                    pygame.Rect(
                        columns * self.__dimensions["width"],
                        rows * self.__dimensions["height"],
                        self.__dimensions["width"],
                        self.__dimensions["height"]
                    )
                ),
                self.__resize
              )
            )
          else:
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