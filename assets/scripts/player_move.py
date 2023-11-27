import pygame 
import core.types as types
from core.scene import Scene
from core.entities import Entity
from entities.player import Player

# remove this player two and make it a way that you can receive the respective necessary keys to make the movement for each player, or something like that

class PlayerMove(types.Script):
    def __init__(self, scene: Scene, speed: int, player: Player, keys: types.TKeys, gravity: float, out_of_bounds_damage: int):
        super().__init__()
        self.scene = scene
        self.speed = speed
        self.player = player
        self.keys = keys
        self.gravity = gravity
        self.out_of_bounds_damage = out_of_bounds_damage

    def setup(self, owner: Entity):
        self.owner = owner
        self.limits = types.ResolverConfig.resolve()["window"]["dimension"]
    
    def loop(self, _screen: pygame.Surface, delta_time: float):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                    
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if (self.player.alive):
                    if event.key == self.keys["up"]:
                        self.player.moveUp(self.gravity)
                    if event.key == self.keys["shoot"]:
                        self.player.shoot()
                    if event.key == self.keys["reload"]:
                        self.player.reload()
            
        if (not self.player.isInsideLimitsBottom(self.screen)):
            self.player.hp -= self.out_of_bounds_damage
            self.player.moveUp(self.gravity)
        if (not self.__p2.isInsideLimitsBottom(self.screen)):
            self.__p2.hp -= self.out_of_bounds_damage
            self.__p2.moveUp(self.gravity)

        if self.player.is_moving_up:
            self.player.moveUp(self.gravity)
        else:
            self.player.moveDown(self.gravity)