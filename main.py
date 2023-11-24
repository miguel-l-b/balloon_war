import pygame
from pygame.locals import *
from core.resolver import ResolverConfig, ResolverFile, ResolverPath
import importlib.util

pygame.init()
screen = pygame.display.set_mode((500, 500))

main = ResolverConfig.resolve()["mainScene"]

for scene in ResolverFile.getAllFiles("@scenes"):
  if scene.endswith(".py"):
    name_scene = scene.replace(".py", "")
    if name_scene == main:
      spec = importlib.util.spec_from_file_location(name_scene, ResolverPath.resolve(f"@scenes/{scene}"))
      modulo = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(modulo)

      modulo.start(screen)
      break

pygame.quit()
exit()