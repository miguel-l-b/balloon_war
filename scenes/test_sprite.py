import pygame
from pygame import *
from pygame.locals import *
from core.sprite import SpriteSlicer

class TestSpriteScene():
  def __init__(self, screen: Surface) -> None:
    self.screen = screen
    self.sprite = SpriteSlicer("@sprites/balloon_orange.png", {"width": 40, "height": 40, "rows": 11, "columns": 1}, 11)
    self.__vez = 0

  def draw(self):
    self.screen.fill((255, 255, 255))
    self.screen.blit(self.sprite.get(self.__vez), (0, 0))

  def loop(self):
    while True:
      self.draw()
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          exit()

      self.__vez += 1
      if self.__vez > 10:
        self.__vez = 0

      
      pygame.time.Clock().tick(60)
 
def start(screen: Surface):
  TestSpriteScene(screen).loop()
  