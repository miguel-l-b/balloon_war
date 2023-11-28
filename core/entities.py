from pygame import Surface
import pygame
from core.hitbox import Hitbox
from core.resolver import ResolverConfig
from core.sprite import SpriteSlicer

import core.types as types

class Entity:
  def __init__(self, name: str, coords: types.TCoord, zGroup: types.zGroup, hitbox: types.Hitbox = None, script: "list[types.Script]" = None):
    self._name = name
    self._coords: types.TCoord = coords
    self._z = zGroup
    self._delta = 1/ResolverConfig.resolve()["game"]["frameRate"]
    self._rect: types.TRect = None
    self._script = script
    self._hitbox = hitbox
    if self._script is not None:
      for s in self._script:
        s.setup(self)

  def moving(self, coords: types.TCoord):
    self._coords = (self._coords[0] + coords[0], self._coords[1] + coords[1])
    if self._rect is not None:
      self._rect.x = self._coords[0]
      self._rect.y = self._coords[1]

  @property
  def rect(self) -> types.TRect:
    return self._rect
  
  @property
  def hitbox(self) -> types.Hitbox:
    return self._hitbox

  @property
  def z(self) -> types.zGroup:
    return self._z

  @property
  def name(self) -> str:
    return self._name
  
  @property
  def coords(self) -> types.TCoord:
    return self._coords

  def update(self, screen: Surface):
    if self._script is not None:
      for script in self._script:
        script.loop(screen, self._delta)
    pass

  def __str__(self):
    return f"{self.__name__}#{self._name}@{self._coords}[{self._z}]"


class Text(Entity):
  def __init__(self, name: str, coords: types.TCoord, zGroup: types.zGroup, text: str, size: int = 20, color: types.TColor = (0, 0, 0), fontFamily: str = "Arial", script: "list[types.Script]" = None):
    super().__init__(name, coords, zGroup, None, script)
    self.__text = text
    self.__size = size
    self.__color = color
    self.__fontFamily = fontFamily
  
  @property
  def text(self):
    return self.__text
  
  def __handleText(self):
    return pygame.font.SysFont(self.__fontFamily, self.__size).render(self.__text, True, self.__color)
  @text.setter
  def text(self, newText: str):
    self.__text = newText
    self._hitbox = Hitbox(self.__handleText())

  def update(self, screen: Surface):
    super().update(screen)
    screen.blit(self.__handleText(), self._coords)

class Sprite(Entity):
  def __init__(self, name: str, coords: types.TCoord, ZGroup: types.zGroup, sprite: types.TFrame, hitbox: types.Hitbox = None, script: "list[types.Script]" = None):
    super().__init__(name, coords, ZGroup, hitbox, script)
    self.__sprite = sprite
    self._rect = sprite.get_rect()
    self._rect.x = coords[0]
    self._rect.y = coords[1]

  @property
  def sprite(self) -> types.TFrame:
    return self.__sprite
  
  @sprite.setter
  def sprite(self, newSprite: types.TFrame):
    self.__sprite = newSprite
    self._rect = newSprite.get_rect()
    self._rect.x = self._coords[0]
    self._rect.y = self._coords[1]

  def update(self, screen: Surface):
    super().update(screen)
    screen.blit(self.__sprite, self._rect)

class AnimatedSprite(Entity):
  def __init__(self, name: str, coords: types.TCoord, zGroup: types.zGroup, sprites: SpriteSlicer, fps: int = 10, loop: bool = True, stopWithSprite: int = None, timeToStop: int = None, rollback: bool = False, hitbox: types.Hitbox = None, script: "list[types.Script]" = None):
    super().__init__(name, coords, zGroup, hitbox, script)
    self.__sprites = sprites.getAll()
    self.__fps = fps
    self.__currentSprite = 0
    self.__timer = 0
    self.__loop = loop
    self.__stopWithSprite = stopWithSprite
    self.__timeToStop = timeToStop
    self.__rollback = rollback

  @property
  def sprites(self) -> str:
    return self.__sprites

  def update(self, screen: Surface):
    super().update(screen)
    # Atualiza o timer com base no delta
    self.__timer += self._delta * 1000  # Multiplica por 1000 para converter para milissegundos

    # Calcula o tempo por sprite em milissegundos
    time_per_sprite = 1000 / self.__fps

    # Verifica se é hora de avançar para o próximo sprite
    if self.__timer >= time_per_sprite:
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
    screen.blit(current_sprite, self.coords)
    