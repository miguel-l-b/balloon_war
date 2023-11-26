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
    spriteTitle = SpriteSlicer(
      ResolverPath.resolve("@sprites/title_game.png"),
      {"width": 157, "height": 40, "rows": 5, "columns": 4},
      18,
      (157 * 2, 40 * 2)
    )
    spriteLongButtons = SpriteSlicer(
      ResolverPath.resolve("@sprites/long_buttons.png"),
      {"width": 120, "height": 50, "rows": 1, "columns": 2},
      2,
      (120 * 2, 50 * 2)
    )
    
    zTop = types.zGroup(1, "top")
    zBottom = types.zGroup(-1, "bottom")
    zMedium = types.zGroup(0, "medium")

    self.spawn(
      AnimatedSprite(
        "title",
        ResolverCoords.getCoordsWithCenterX(ResolverConfig.resolve()["window"]["dimension"], spriteTitle.size),
        zMedium,
        spriteTitle,
        10,
        rollback=True,
        stopWithSprite=18,
        timeToStop=1
      )
    )
    self.spawn(
      Entity(
        "cloud_generator",
        (0, 0),
        zBottom,
        [
          ResolverScript.getScript("cloud_generator", self, [zBottom, zMedium], 5)
        ]
      )
    )

    self.spawn(
      Text(
        "show_fps",
        (10, 10),
        zTop,
        "FPS: 0",
        10,
        (250, 20, 35),
        script=[
          ResolverScript.getScript("fps", self._clock)
        ]
      )
    )

    self.spawn(
      Sprite(
        "btn_play",
        (ResolverCoords.getCoordsWithCenter(ResolverCoords.getSizeScreen(), spriteLongButtons.size)),
        zTop,
        spriteLongButtons.get(0)
      )
    )


def start(screen: Surface):
  pygame.mixer.music.load(ResolverPath.resolve("@audio/music/retro_music_in_game.wav"))
  pygame.mixer.music.set_volume(ResolverConfig.resolve()["game"]["volume"])
  pygame.mixer.music.play(loops=-1)
  LobbyScene(screen).loop()