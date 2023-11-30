from typing import TypedDict
import pygame
from core.hitbox import Hitbox
from core.resolver import ResolverCoords, ResolverScript
from core.sprite import SpriteSlicer 
import core.types as types
from core.scene import Scene
from core.entities import AnimatedSprite, Sprite

class TKeys(TypedDict):
    up: int
    shoot: int
    reload: int

class PlayerManager(types.Script):
    def __init__(self, scene: Scene, num: int, speed: int, keys: TKeys, gravity: float, maxHP: int):
        super().__init__()
        self._num = num
        self._scene = scene
        self._speed = speed
        self._keys = keys
        self._gravity = gravity
        self._maxHP = maxHP

    def setup(self, owner: AnimatedSprite):
        self._owner = owner
        self._ammunitionSprite = SpriteSlicer(
            "@sprites/darts.png",
            {
                "width": 45,
                "height": 45,
                "rows": 2,
                "columns": 1
            },
            2,
            (70, 70)
        )
        self._heartSprite = SpriteSlicer(
            "@sprites/heart.png",
            {
                "width": 25,
                "height": 25,
                "rows": 3,
                "columns": 1
            },
            3
        )
        self._limits = ResolverCoords.getSizeScreen()
        self._ammunition = 10
        self._timer = 0
        self._velocity = 0
        self._jumpIn = 0
        self._shotIn = 0
        self._reloadIn = 0
        self._reloaded = False
        self._hp = self._maxHP
        self.handleHP()

    def handleHP(self):
        for i in range(0, self._hp):
            self._scene.spawn(
                Sprite(
                    f"hp-{i}#{self._num}",
                    (self._owner.coords[0]+(30*i), 50),
                    self._owner.z,
                    self._heartSprite.get(0),
                    hitbox=Hitbox(self._heartSprite.get(0).get_rect()),
                )
            )
        for i in range(self._hp, self._maxHP):
            self._scene.kill(f"hp-{i}#{self._num}")
            self._scene.spawn(
                Sprite(
                    f"hp-{i}#{self._num}_ded",
                    (self._owner.coords[0]+(30*i), 50),
                    self._owner.z,
                    self._heartSprite.get(2),
                    hitbox=Hitbox(self._heartSprite.get(2).get_rect()),
                )
            )

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

        if pygame.key.get_pressed()[self._keys["shoot"]] and self._ammunition > 0 and self._timer - self._shotIn >= 0.5:
            self._shotIn = self._timer
            self._scene.spawn(
                Sprite(
                    f"dart_{self._ammunition}#{self._num}",
                    (self._owner.coords[0]+(80 if self._num == 0 else -80), self._owner.coords[1]),
                    self._owner.z,
                    self._ammunitionSprite.get(self._num),
                    hitbox=Hitbox(self._ammunitionSprite.get(0).get_rect()),
                    script=[
                        ResolverScript.getScript("dart_move", self._scene, 5, 10, self._num)
                    ]
                )
            )
            self._ammunition = self._ammunition - 1

        
        elif pygame.key.get_pressed()[self._keys["reload"]] and self._ammunition == 0:
            self._reloadIn = self._timer
            self._reloaded = True

        if self._reloaded and self._timer - self._reloadIn >= 0.3:
            self._reloaded = False
            self._ammunition = 10


        if self._owner.coords[1] >= 0 and self._owner.coords[1] >= self._limits[1]:
            self._owner.moving((0, -self._owner.coords[1]))
            self._velocity = 0
            self._hp -= 1

        for obj in self._scene.onCollision(self._owner):
            if obj.name.startswith("dart") and obj.name.split("#")[1] != str(self._num):
                self._hp = self._hp - 1
                self._scene.kill(obj.name)
                self.handleHP()

        self._owner.moving((0, self._velocity * delta_time))
        self.handleHP()