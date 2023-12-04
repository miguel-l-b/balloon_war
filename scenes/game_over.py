import pygame
from core.entities import AnimatedSprite, Sprite, Text
from core.hitbox import Hitbox
from core.resolver import ManagerScenes, ResolverConfig, ResolverCoords, ResolverPath, ResolverScript
from core.scene import Scene
from core.sprite import SpriteSlicer
from core.types import zGroup


class GameOverScene(Scene):
  def __init__(self, screen):
    super().__init__(screen)
    spriteLongButtons = SpriteSlicer(
      ResolverPath.resolve("@sprites/long_buttons.png"),
      {"width": 120, "height": 50, "rows": 1, "columns": 2},
      2,
      (120 * 2, 50 * 2)
    )

    self._zTop = zGroup(1, "top")

    self._backgroundColor = ResolverConfig.resolve()["game"]["colors"]["black"]
    self.spawn(
      Text(
        "lbl_title",
        ResolverCoords.getCoordsWithCenterX(ResolverCoords.getSizeScreen(), (260, 50)),
        self._zTop,
        "Game Over",
        50,
        (255, 255, 255)
      )
    )
    self.spawn(
      Sprite(
        "btn_play",
        (ResolverCoords.getCoordsWithCenter(ResolverCoords.getSizeScreen(), spriteLongButtons.size)),
        self._zTop,
        spriteLongButtons.get(0),
        hitbox=Hitbox(spriteLongButtons.get(0)),
        script=[
          ResolverScript.getScript("btn_start", spriteLongButtons.get(0), spriteLongButtons.get(1))
        ]
      )
    )

  def start(self, player):
    self._player = player
    self.spawn(
      Text(
        "lbl_player",
        ResolverCoords.getCoordsWithCenterX(ResolverCoords.getSizeScreen(), (130, 100)),
        self._zTop,
        f"Player {self._player+1} perdeu",
        20,
        (255, 255, 255)
      )
    )
    ManagerScenes().rebuild("game")
    super().start()