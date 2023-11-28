from core.entities import Text
from core.resolver import ResolverCoords
from core.scene import SceneLoader
from core.types import zGroup


class LoadScene(SceneLoader):
  def __init__(self, screen):
    super().__init__(screen)
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

  @property
  def isFinished(self):
    return self._isFinished

