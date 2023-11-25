import random
from core.sprite import SpriteSlicer
import core.types as types
import pygame
from core.entities import Entity, Sprite
from core.resolver import ResolverConfig, ResolverPath, ResolverScript
from core.scene import Scene


class CloudGenerator(types.Script):
  def __init__(self, scene: Scene, z: "list[types.zGroup]", quantity: int = 5):
    super().__init__()
    self.scene = scene
    self.z = z
    self.quantity = quantity
    self.count = 0

  def setup(self, owner: Entity):
    self.timer = 0
    self.owner = owner
    self.limits = ResolverConfig.resolve()["window"]["dimension"]
    self.sprite = SpriteSlicer(
      ResolverPath.resolve("@sprites/cloud.png"),
      {"width": 60, "height": 24, "rows": 3, "columns": 2},
      5,
      (60 * 2, 24 * 2)
    )
    for i in range(1, self.quantity+1):
      self.generate(random.randint(0, 1))

  def generate(self, direction: int = 0):
    if direction == 0:
      self.scene.spawn(
        Sprite(
          f"cloud_{self.count}",
          (-100, random.randint(0, int(self.limits[1]/3)+50)), 
          self.z[direction],
          self.sprite.get(random.randint(0, self.sprite.amount -1)),
          [
            ResolverScript.getScript("cloud_move", direction, self.scene, random.randint(10, 35))
          ]
        )
      )
    else:
      self.scene.spawn(
        Sprite(
          f"cloud_{self.count}",
          (self.limits[0]+100, random.randint(0, int(self.limits[1]/3)+550)), 
          self.z[direction],
          self.sprite.get(random.randint(0, self.sprite.amount -1)),
          [
            ResolverScript.getScript("cloud_move", direction, self.scene, -random.randint(10, 35))
          ]
        )
      )
    self.count += 1

  def loop(self, _screen: pygame.Surface, delta_time: float):
    self.timer += delta_time
    if self.timer >= random.randint(5, 10):
      self.timer = 0
      self.generate(random.randint(0, 1))
    
    if self.count >= self.quantity**2:
      try:
        self.scene.get("cloud_0")
      except Exception:
        self.count = 0
    print(self.count)
      