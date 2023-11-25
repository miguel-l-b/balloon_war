import pygame
from pygame.locals import *
from core.resolver import ResolverConfig, ResolverFile, ResolverPath
import importlib.util

pygame.init()
pygame.mixer.init()
pygame.display.set_icon(pygame.image.load(ResolverPath.resolve("@assets/icon.png")))
pygame.display.set_caption(ResolverConfig.resolve()["window"]["title"])
screen = pygame.display.set_mode(
  ResolverConfig.resolve()["window"]["dimension"],
  pygame.FULLSCREEN if ResolverConfig.resolve()["window"]["fullScreen"] else 0
)
main = ResolverConfig.resolve()["game"]["mainScene"]

for scene in ResolverFile.getAllFilesWithExtension("@scenes", ".py"):
  name_scene = scene.replace(".py", "")
  if name_scene == main:
    path = ResolverPath.resolve(f"@scenes/{scene}")
    try:
      spec = importlib.util.spec_from_file_location(
        name_scene,
        path
      )
      modulo = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(modulo)
      
      getattr(modulo, "start")(screen)
    except ImportError:
      raise ImportError(f"Não foi possível importar o módulo {name_scene} de {path}.")
    except AttributeError:
      raise AttributeError(f"A função start não foi encontrada no módulo {path}.")
    break

pygame.quit()
exit()