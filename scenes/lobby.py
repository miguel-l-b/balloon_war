import pygame
from pygame import *
from pygame.locals import *
from core.entities import AnimatedSprite, Entity
from core.resolver import ResolverConfig, ResolverCoords, ResolverPath
from core.scene import Scene
from core.sprite import SpriteSlicer

class LobbyScene(Scene):
  def __init__(self, screen: Surface) -> None:
    super().__init__(screen)
    self._objects: list[Entity] = [
      AnimatedSprite(
        "title",
        ResolverCoords.getCoordsWithCenterX(ResolverConfig.resolve()["window"]["dimension"], (157*2, 40*2)),
        SpriteSlicer(
          ResolverPath.resolve("@sprites/title_game.png"),
          {"width": 157, "height": 40, "rows": 5, "columns": 4},
          18,
          (157 * 2, 40 * 2)
        ),
        25,
        rollback=True,
        stopWithSprite=18,
        timeToStop=1
      )
    ]

def start(screen: Surface):
  pygame.mixer.music.load(ResolverPath.resolve("@audio/music/retro_music_in_game.wav"))
  pygame.mixer.music.set_volume(ResolverConfig.resolve()["game"]["volume"])
  pygame.mixer.music.play(loops=-1)
  LobbyScene(screen).loop()