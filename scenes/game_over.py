from core.scene import Scene


class GameOverScene(Scene):
  def __init__(self, screen):
    super().__init__(screen)
    pass

  def start(self, player):
    self._player = player
    super().start()