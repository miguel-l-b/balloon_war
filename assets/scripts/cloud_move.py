from pygame import Vector2
from core.entities import Entity, Script

class CloudMove(Script):
  def __init__(self):
    super().__init__()

  def setup(self, owner: Entity):
    self.owner = owner

  def loop(self, delta_time):
    self.owner.position += Vector2(0.5, 0) * delta_time
    if self.owner.position.x > 800:
        self.owner.position = Vector2(-200, 0)