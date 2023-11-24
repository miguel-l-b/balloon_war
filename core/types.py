from enum import Enum
from typing import NewType, TypedDict


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

TCoord = NewType("TCoord", "tuple[int, int]")
  
TSize = NewType("TSize", "tuple[int, int]")

TColor = NewType("TColor", "tuple[int, int, int]")
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