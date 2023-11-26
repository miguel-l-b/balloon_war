from enum import Enum
from typing import NewType, TypedDict, Type

import pygame

class TSettingsGame(TypedDict):
  frameRate: int
  mainScene: str
  colors: "dict[str, tuple[int, int, int]]"
class TSettingsWindow(TypedDict):
  title: str
  dimension: "tuple[int, int]"
  fullScreen: bool
class TSettings(TypedDict):
  paths: "dict[str, str]"
  window: TSettingsWindow
  game: TSettingsGame

class Script:
  def __init__(self):
    pass

  def setup(self, owner: any):
    pass

  def loop(self, screen: pygame.Surface):
    pass

TFrame = NewType("TFrame", "pygame.Surface")
TCoord = NewType("TCoord", "tuple[int, int]")
TSize = NewType("TSize", "tuple[int, int]")
TColor = NewType("TColor", "tuple[int, int, int]")
TRect = pygame.Rect

class TDimension(TypedDict):
  width: int
  height: int
  rows: int
  columns: int

class EDamageType(Enum):
  AIR = 0
  MELLE = 1
  FIRE = 2
  WATER = 3
  EARTH = 4
  ELECTRIC = 5

class zGroup:
  def __init__(self, z: int, name: str):
    self.__z = z
    self.__name = name

  @property
  def z(self):
    return self.__z
  
  @property
  def name(self):
    return self.__name

  def __lt__(self, other):
    return self.__z < other.__z
  
  def __gt__(self, other):
    return self.__z > other.__z
  
  def __le__(self, other):
    return self.__z <= other.__z
  
  def __ge__(self, other):
    return self.__z >= other.__z

  def __eq__(self, other: "zGroup"):
    if isinstance(other, zGroup):
      return self.__name == other.__name
    return False

  def __str__(self):
    return f"{self.__z}@{self.__name}"
  
class Damage:
  def __init__(self, damage: int, damageType: EDamageType):
    self.__damage = damage
    self.__damageType = damageType

  @property
  def damage(self):
    return self.__damage
  
  @property
  def damageType(self):
    return self.__damageType
  
  def __eq__(self, other):
    return self.__damageType == other.__damageType
  
  def __str__(self):
    return f"{self.__damage}@{self.__damageType.name}"