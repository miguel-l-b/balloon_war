import pygame
from pygame import *
from pygame.locals import *
from core.resolver import ResolverConfig
from core.sprite import SpriteAnimation, SpriteSlicer

class TestSpriteScene():
  def __init__(self, screen: Surface) -> None:
    self.screen = screen
    self.sprite = [
      SpriteAnimation(
        SpriteSlicer("@sprites/balloon_orange.png", {"width": 40, "height": 40, "rows": 11, "columns": 1}).getAll(),
        15
      ),
      SpriteAnimation(
        SpriteSlicer("@sprites/balloon_cyan.png", {"width": 40, "height": 40, "rows": 11, "columns": 1}).getAll(),
        15
      ),
      SpriteAnimation(
        SpriteSlicer("@sprites/explode_balloon_orange.png", {"width": 40, "height": 40, "rows": 8, "columns": 1}).getAll(),
        15
      ),
      SpriteAnimation(
        SpriteSlicer("@sprites/explode_balloon_cyan.png", {"width": 40, "height": 40, "rows": 8, "columns": 1}).getAll(),
        15
      ),
      SpriteAnimation(
        SpriteSlicer("@sprites/explode_balloon_orange.png", {"width": 40, "height": 40, "rows": 8, "columns": 1}).getAll(),
        15
      ),
    ]
    self.__limitFPS = ResolverConfig.resolve()["game"]["frameRate"]

  def draw(self):
    self.screen.fill((255, 255, 255))
    for i in self.sprite:
      self.screen.blit(
        pygame.transform.scale(
          i.update(1/self.__limitFPS), (80, 80)
        ),
        (80*self.sprite.index(i), 0)
      )

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
  TestSpriteScene(screen).loop()
  