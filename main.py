import pygame
from time import sleep
from pygame.locals import *
from entities.player import Player
from entities.shot import Shot
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

      # Agora, você pode usar o módulo normalmente
      modulo.start(screen)
      break

pygame.quit()
exit()