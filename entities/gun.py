import pygame
from entities.shot import Shot

class Gun():
    def __init__(
        self, 
        name: str, 
        meg_capacity: int,
        damage: int,
        shoot_cooldown_time: int, 
        reload_cooldown_time: int, 
        bullet_size: tuple[int, int], 
        bullet_image_path: str,
        bullet_color: pygame.Color,
        bullet_speed: int,
        ):
        self.__name = name
        self.__damage = damage
        self.__shoot_cooldown = 0 
        self.__shoot_cooldown_time = shoot_cooldown_time
        self.__reload_cooldown = 0
        self.__reload_cooldown_time = reload_cooldown_time 
        self.__meg_capacity = meg_capacity
        self.__bullets = meg_capacity
        self.__bullet_size = bullet_size
        self.__bullet_image_path = bullet_image_path
        self.__bullet_color = bullet_color
        self.__bullet_speed = bullet_speed
        self.__shots: list[Shot] = []
        self.__coords = (0, 0)

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, newDamage):
        self.__damage = newDamage

    @property
    def shots(self):
        return self.__shots

    @shots.setter
    def shots(self, newShots):
        self.__shots = newShots

    @property
    def bullets(self):
        return self.__bullets

    @bullets.setter
    def bullets(self, newBullets):
        self.__bullets = newBullets

    @property
    def bullet_color(self):
        return self.__bullet_color

    @bullet_color.setter
    def bullet_color(self, newBulletColor):
        self.__bullet_color = newBulletColor

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, newCoords):
        self.__coords = newCoords

    def update(self):
        if self.__shoot_cooldown > 0:
            self.__shoot_cooldown -= 1

        if self.__reload_cooldown > 0:
            self.__reload_cooldown -= 1

    def shoot(self):
        if self.__shoot_cooldown == 0 and self.__reload_cooldown == 0 and self.__bullets > 0:
            self.__shots.append(
                Shot(image_path=self.__bullet_image_path, 
                     color=self.__bullet_color, 
                     initialCoords=self.__coords, 
                     size=self.__bullet_size, 
                     speed=self.__bullet_speed
                    )
            )
            self.__shoot_cooldown = self.__shoot_cooldown_time
            self.__bullets -= 1
    
    def removeShot(self, shot: Shot):
        self.__shots.remove(shot)

    def reload(self):
        if self.__reload_cooldown == 0:
            self.__reload_cooldown = self.__reload_cooldown_time
            self.__bullets = self.__meg_capacity
