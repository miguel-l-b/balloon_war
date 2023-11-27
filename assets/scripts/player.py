import pygame 
import core.types as types
from core.scene import Scene
from core.sprite import SpriteSlicer
from core.entities import Entity, Sprite

# remove this player two and make it a way that you can receive the respective necessary keys to make the movement for each player, or something like that

class PlayerMove(type.Script):
    def __init__(self, scene: Scene, speed: int):
        super().__init__()
        self.scene = scene
        self.speed = speed

    def setup(self, owner: Sprite):
        self.owner = owner
        self.limits = types.ResolverConfig.resolve()["window"]["dimension"]
    
    def loop(self, _screen: pygame.Surface, delta_time: float):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                    
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.__p1.moveUp(self.__gravity)
                if event.key == pygame.K_DOWN:
                    self.p1_direction_up = False

                if event.key == pygame.K_LEFT:
                    if (self.__p1.alive):
                        self.__p1.shoot()
                if event.key == pygame.K_RIGHT:
                    if (self.__p1.alive):
                        self.__p1.reload()

                if event.key == pygame.K_w:
                    self.__p2.moveUp(self.__gravity)
                if event.key == pygame.K_s:
                    self.p2_direction_up = False
                if event.key == pygame.K_d:
                    if (self.__p2.alive):
                        self.__p2.shoot()
                if event.key == pygame.K_a:
                    if (self.__p2.alive):
                        self.__p2.reload()

            
        if (not self.__p1.isInsideLimitsBottom(self.screen)):
            self.__p1.hp -= 15
            self.__p1.moveUp(self.__gravity)
        if (not self.__p2.isInsideLimitsBottom(self.screen)):
            self.__p2.hp -= 15
            self.__p2.moveUp(self.__gravity)

        if self.__p1.is_moving_up:
            self.__p1.moveUp(self.__gravity)
        else:
            self.__p1.moveDown(self.__gravity)

        if self.__p2.is_moving_up:
            self.__p2.moveUp(self.__gravity)
        else:
            self.__p2.moveDown(self.__gravity)