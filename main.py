import threading
import pygame
from pygame.locals import *
from core.resolver import ManagerScenes, ResolverConfig, ResolverPath, ResolverScene
from core.scene import Scene, SceneLoader

pygame.init()
pygame.mixer.init()
pygame.display.set_icon(pygame.image.load(ResolverPath.resolve("@assets/icon.png")))
pygame.display.set_caption(ResolverConfig.resolve()["window"]["title"])
screen = pygame.display.set_mode(
  ResolverConfig.resolve()["window"]["dimension"],
  pygame.FULLSCREEN if ResolverConfig.resolve()["window"]["fullScreen"] else 0
)

load = ResolverConfig.resolve()["game"]["loadScene"]
main = ResolverConfig.resolve()["game"]["mainScene"]

if load is not None:
  load_scene: SceneLoader = ResolverScene.handleScene(load, screen)
  thread_load = threading.Thread(target=load_scene.start, name=load_scene.__class__.__name__)
  thread_load.start()
  manager = ManagerScenes(screen)
  load_scene.stop()
  thread_load.join()
  manager.goTo(main)
else:
  ManagerScenes(screen).goTo(main)

pygame.quit()
exit()