import pygame
from pygame import *
from pygame.locals import *
from core.entities import AnimatedSprite, Entity, Text
from core.resolver import ResolverConfig, ResolverCoords, ResolverPath
from core.sprite import SpriteSlicer

class LobbyScene():
  def __init__(self, screen: Surface) -> None:
    self.__screen = screen
    self.__objects: list = [
      AnimatedSprite(
        "title",
        ResolverCoords.getCoordsWithCenterX(ResolverConfig.resolve()["window"]["dimension"], (157*2, 40*2)),
        SpriteSlicer(ResolverPath.resolve("@sprites/title_game.png"), {"width": 157, "height": 40, "rows": 5, "columns": 4}, 18, (157 * 2, 40 * 2)),
        25,
        rollback=True,
        stopWithSprite=18,
        timeToStop=1
      )
    ]
    self.__limitFPS = ResolverConfig.resolve()["game"]["frameRate"]

  def draw(self):
    self.__screen.fill(ResolverConfig.resolve()["game"]["colors"]["cyan"])
    for obj in self.__objects:
      if(isinstance(obj, Entity)):
        obj.update(self.__screen)

  def loop(self):
    while True:
      self.draw()
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          exit()
      
      pygame.time.Clock().tick(self.__limitFPS)

def start(screen: Surface):
  pygame.mixer.music.load(ResolverPath.resolve("@audio/music/retro_music_in_game.wav"))
  pygame.mixer.music.set_volume(ResolverConfig.resolve()["game"]["volume"])
  pygame.mixer.music.play(loops=-1)
  LobbyScene(screen).loop()