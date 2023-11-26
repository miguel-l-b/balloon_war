from core.entities import Text
from core.resolver import ResolverCoords
from core.scene import SceneLoader
from core.types import zGroup


class LoadScene(SceneLoader):
  def __init__(self, screen):
    super().__init__(screen)
    self._isFinished = False
    self.__timer = 0

    self.spawn(
      Text(
        "txt_load",
        ResolverCoords.getCoordsWithCenter(ResolverCoords.getSizeScreen(), (200, 100)),
        zGroup(1, "top"),
        "Loading...",
        50,
        (0, 0, 0)
      )
    )

  def start(self):
    super().start()

  @property
  def isFinished(self):
    if self._clock.get_time() > 0:
      self.__timer += 1/self._clock.get_time()

    if self.__timer >= 5*100000:
      self._isFinished = True

    return self._isFinished

