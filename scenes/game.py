import pygame
from pygame import *
from pygame.locals import *
from core.entities import *
from core.resolver import ResolverConfig, ResolverPath, ResolverScript
from core.scene import Scene
from core.sprite import SpriteSlicer

class GameScene(Scene):    
  def __init__(self, screen: Surface):
    super().__init__(screen)
    
    zTop = types.zGroup(1, "top")
    zBottom = types.zGroup(-1, "bottom")
    zMedium = types.zGroup(0, "medium")

    self.spawn(
      Entity(
        "cloud_generator",
        (0, 0),
        zBottom,
        [
          ResolverScript.getScript("cloud_generator", self, [zBottom, zMedium], 10)
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

    self._backgroundColor = ResolverConfig.resolve()["game"]["colors"]["cyan"]
  def start(self):
    pygame.mixer.music.load(ResolverPath.resolve("@audio/music/retro_music_in_game.wav"))
    pygame.mixer.music.set_volume(ResolverConfig.resolve()["game"]["volume"])
    pygame.mixer.music.play(loops=-1)
    super().start()