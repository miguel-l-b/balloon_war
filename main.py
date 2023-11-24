import pygame
from core.resolver import ResolverConfig, ResolverFile, ResolverPath
import importlib.util

pygame.init()
pygame.display.set_caption(ResolverConfig.resolve()["window"]["title"])
screen = pygame.display.set_mode(
  ResolverConfig.resolve()["window"]["dimension"],
  pygame.FULLSCREEN if ResolverConfig.resolve()["window"]["fullScreen"] else 0
)
main = ResolverConfig.resolve()["game"]["mainScene"]

for scene in ResolverFile.getAllFilesWithExtension("@scenes", ".py"):
  name_scene = scene.replace(".py", "")
  if name_scene == main:
    spec = importlib.util.spec_from_file_location(
      name_scene,
      ResolverPath.resolve(f"@scenes/{scene}")
    )
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)

    # Agora, você pode usar o módulo normalmente
    modulo.start(screen)
    break

pygame.quit()
exit()