import pygame
from core.entities import Text
from core.resolver import ResolverConfig, ResolverCoords
from core.scene import Scene
from core.types import zGroup


class GameOverScene(Scene):
  def __init__(self, screen):
    super().__init__(screen)

    zTop = zGroup(1, "top")

    self._backgroundColor = ResolverConfig.resolve()["game"]["colors"]["black"]
    self.spawn(
      Text(
        "lbl_title",
        ResolverCoords.getCoordsWithCenter(ResolverCoords.getSizeScreen(), (260, 50)),
        zTop,
        "Game Over",
        50,
        (255, 255, 255)
      )
    )

  def start(self, player):
    self._player = player
    super().start()