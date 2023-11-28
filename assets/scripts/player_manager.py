from typing import TypedDict
import pygame
from core.resolver import ResolverCoords 
import core.types as types
from core.scene import Scene
from core.entities import AnimatedSprite

class TKeys(TypedDict):
    up: int
    shoot: int
    reload: int

class PlayerManager(types.Script):
    def __init__(self, scene: Scene, speed: int, keys: TKeys, gravity: float):
        super().__init__()
        self._scene = scene
        self._speed = speed
        self._keys = keys
        self._gravity = gravity

    def setup(self, owner: AnimatedSprite):
        self._owner = owner
        self._limits = ResolverCoords.getSizeScreen()
        self._timer = 0
        self._velocity = 0
        self._jumpIn = 0

    def calculateInercie(self, oldVelocity: float, increment: float, delta_time: float):
        return oldVelocity + (increment * delta_time)

    def calculateResistanceAir(self, velocity: float, delta_time: float):
        return velocity * (1 - (0.01 * delta_time))

    def loop(self, _screen: pygame.Surface, delta_time: float):
        self._timer += delta_time

        if pygame.key.get_pressed()[self._keys["up"]] and self._timer - self._jumpIn >= 1.5:
            self._jumpIn = self._timer
            self._velocity = -self._speed
        elif self._timer - self._jumpIn <= 0.5:
            self._velocity = -self._speed
        else:
            self._velocity = self.calculateInercie(self._velocity, self._gravity, delta_time)
        self._velocity = self.calculateResistanceAir(self._velocity, delta_time)
        
        self._owner.moving((0, self._velocity * delta_time))