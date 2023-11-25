import pygame
from pygame import *
from pygame.locals import *
from core.entities import *
from core.resolver import ResolverConfig, ResolverCoords, ResolverPath, ResolverScript
from core.scene import Scene
from core.sprite import SpriteSlicer

class LobbyScene(Scene):
  def __init__(self, screen: Surface) -> None:
    super().__init__(screen)
    self.__sprites: list = [
      SpriteSlicer(
        ResolverPath.resolve("@sprites/title_game.png"),
        {"width": 157, "height": 40, "rows": 5, "columns": 4},
        18,
        (157 * 2, 40 * 2)
      ),
      SpriteSlicer(
        ResolverPath.resolve("@sprites/cloud.png"),
        {"width": 60, "height": 24, "rows": 3, "columns": 2},
        5,
        (60 * 2, 24 * 2)
      )
    ]
    self._objects: list[Entity] = [
      AnimatedSprite(
        "title",
        ResolverCoords.getCoordsWithCenterX(ResolverConfig.resolve()["window"]["dimension"], self.__sprites[0].size),
        self.__sprites[0],
        25,
        rollback=True,
        stopWithSprite=18,
        timeToStop=1
      ),
      Sprite(
        "cloud",
        ResolverCoords.getCoordsWithCenterX(ResolverConfig.resolve()["window"]["dimension"], self.__sprites[1].size),
        self.__sprites[1].get(0),
        [
          {
            "script": ResolverScript.getScript("cloud_move"),
            "data": {
              "speed": 2
            }
          }
        ]
      ),
    ]

def start(screen: Surface):
  pygame.mixer.music.load(ResolverPath.resolve("@audio/music/retro_music_in_game.wav"))
  pygame.mixer.music.set_volume(ResolverConfig.resolve()["game"]["volume"])
  pygame.mixer.music.play(loops=-1)
  LobbyScene(screen).loop()