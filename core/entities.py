from pygame import Surface
import pygame
from core.resolver import ResolverConfig
from core.sprite import SpriteSlicer

import core.types as types

class Damage:
  def __init__(self, damage: int, damageType: types.EDamageType):
    self.__damage = damage
    self.__damageType = damageType

  @property
  def damage(self):
    return self.__damage
  
  @property
  def damageType(self):
    return self.__damageType
  
  def __eq__(self, other):
    return self.__damageType == other.__damageType
  
  def __str__(self):
    return f"{self.__damage}@{self.__damageType.name}"

class Entity:
  def __init__(self, name: str, coords: tuple):
    self._name = name
    self._coords = coords
    self._delta = ResolverConfig.resolve()["game"]["frameRate"]

  def update(self, screen: Surface):
    pass

  def __str__(self):
    return f"{self.__name}@{self.__coords}"

class Text(Entity):
  def __init__(self, name: str, coords: tuple, text: str, size: int = 20, color: types.TColor = (0, 0, 0), fontFamily: str = "Arial"):
    super().__init__(name, coords)
    self.__text = text
    self.__size = size
    self.__color = color
    self.__fontFamily = fontFamily
  
  @property
  def text(self):
    return self.__text

  @text.setter
  def text(self, newText):
    self.__text = newText

  def update(self, screen: Surface):
    font = pygame.font.SysFont(self.__fontFamily, self.__size)
    text = font.render(self.__text, True, self.__color)
    screen.blit(text, self._coords)

class Sprite(Entity):
  def __init__(self, name: str, coords: tuple, sprite: pygame.Surface):
    super().__init__(name, coords)
    self.__sprite = sprite

  def update(self, screen: Surface):
    screen.blit(self.__sprite, self._coords)

class AnimatedSprite(Entity):
  def __init__(self, name: str, coords: tuple, sprites: SpriteSlicer, fps: int = 10, loop: bool = True, stopWithSprite: int = None, timeToStop: int = None, rollback: bool = False):
    super().__init__(name, coords)
    self.__sprites = sprites.getAll()
    self.__fps = fps
    self.__currentSprite = 0
    self.__timer = 0
    self.__loop = loop
    self.__stopWithSprite = stopWithSprite
    self.__timeToStop = timeToStop
    self.__rollback = rollback

  def update(self, screen: Surface):
      self.__timer += self._delta  # Usando o delta de frame para controlar o tempo

      # Calcula a quantidade de tempo por frame em milissegundos
      time_per_frame = 1000 / self.__fps

      # Verifica se é hora de avançar para o próximo sprite
      if self.__timer >= time_per_frame:
          self.__timer = 0
          self.__currentSprite += 1

          # Verifica se atingiu o último sprite e se deve reiniciar
          if self.__currentSprite >= len(self.__sprites):
              if self.__loop:
                  self.__currentSprite = 0
              elif self.__rollback:
                  self.__currentSprite = len(self.__sprites) - 2

          # Verifica se deve parar a animação com um sprite específico
          if self.__stopWithSprite is not None and self.__currentSprite == self.__stopWithSprite:
              self.__loop = False

          # Verifica se deve parar a animação após um determinado tempo
          if self.__timeToStop is not None and self.__timer >= self.__timeToStop:
              self.__loop = False

      # Desenha o sprite atual na tela
      current_sprite = self.__sprites[self.__currentSprite]
      screen.blit(current_sprite, self._coords)