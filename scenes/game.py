import pygame
from pygame import *
from pygame.locals import *
from core.entities import *
from core.resolver import ResolverConfig, ResolverCoords, ResolverPath, ResolverScript, ResolverVolume
from core.scene import Scene
from core.sprite import SpriteSlicer

class GameScene(Scene):    
  def __init__(self, screen: Surface):
    super().__init__(screen)
    
    zBottom = types.zGroup(-2, "bottom")
    zBM = types.zGroup(-1, "bm")
    zMedium = types.zGroup(0, "medium")
    zTop = types.zGroup(1, "top")

    sprite_orange = SpriteSlicer(
      ResolverPath.resolve("@sprites/balloon_orange.png"),
      {"width": 40, "height": 40, "rows": 8, "columns": 1},
      8,
      (40*2, 40*2)
    )

    sprite_cyan = SpriteSlicer(
      ResolverPath.resolve("@sprites/balloon_cyan.png"),
      {"width": 40, "height": 40, "rows": 8, "columns": 1},
      8,
      (40*2, 40*2)
    )

    self.spawn(
      Entity(
        "cloud_generator",
        (0, 0),
        zBottom,
        script=[
          ResolverScript.getScript("cloud_generator", self, [zBottom, zBM], 4)
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
      AnimatedSprite(
        "player_0",
        ResolverCoords.getCoordsWithCenterY(ResolverCoords.getSizeScreen(), (5, 40)),
        zMedium,
        sprite_cyan,
        fps=15,
        script=[
          ResolverScript.getScript(
            "player_manager",
            self,
            0,
            100,
            {
              "up": pygame.K_w,
              "shoot": pygame.K_d,
              "reload": pygame.K_a
            },
            80,
            3
          )
        ]
      )
    )

    self.spawn(
      AnimatedSprite(
        "player_1",
        ResolverCoords.getCoordsWithCenterY(ResolverCoords.getSizeScreen(), (ResolverCoords.getSizeScreen()[0]-85, 40)),
        zMedium,
        sprite_orange,
        fps=15,
        script=[
          ResolverScript.getScript(
            "player_manager",
            self,
            1,
            100,
            {
              "up": pygame.K_UP,
              "shoot": pygame.K_LEFT,
              "reload": pygame.K_RIGHT
            },
            80,
            3
          )
        ]
      )
    )

    self._backgroundColor = ResolverConfig.resolve()["game"]["colors"]["cyan"]
  def start(self):
    pygame.mixer.music.load(ResolverPath.resolve("@audio/music/retro_music_in_game.wav"))
    pygame.mixer.music.set_volume(ResolverVolume.handleVolume("music"))
    pygame.mixer.music.play(loops=-1)
    super().start()