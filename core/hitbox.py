from typing import Union
import pygame
import core.types as types

class Hitbox(types.Hitbox):
    def __init__(self, rect: types.TRect, damage: "list[types.Damage]" = None):
        super().__init__(rect, damage)
    
    def hit(self, hitbox: Union["types.Hitbox", types.TCoord]) -> bool:
        if isinstance(hitbox, types.Hitbox):
            return self._rect.colliderect(hitbox.rect)
        else:
            return self._rect.collidepoint(hitbox)

# class HitboxSprite(types.Hitbox):
#     def __init__(self, path: str or types.TFrame, coord: types.TCoord, damage: "list[types.Damage]" = None):
#         super().__init__(self._load(path), damage)

#     def _load(self, path: str or types.TFrame):
#         if isinstance(path, types.TFrame):
#             self._mask = pygame.mask.from_surface((types.TFrame)(path).convert_alpha())
#         else:
#             self._mask = pygame.mask.from_surface(pygame.image.load(path).convert_alpha())
#         return self._mask.get_rect()
    
#     @property
#     def mask(self) -> types.TMask:
#         return self._mask
    
#     @property
#     def coord(self) -> types.TCoord:
#         return self._coord
    
#     @coord.setter
#     def coord(self, newCoord: types.TCoord):
#         self._coord = newCoord
    
#     def hit(self, hitbox: Union["HitboxSprite", types.Hitbox, types.TCoord]) -> bool:
#         if isinstance(hitbox, HitboxSprite):
#             return self._mask.overlap(hitbox.mask, hitbox.coord)
#         if isinstance(hitbox, types.Hitbox):
#             mask = pygame.mask.from_surface(hitbox.rect)
#             return self._mask.overlap(mask, hitbox.coord)
#         if isinstance(hitbox, types.TCoord):
#             other = pygame.mask.from_surface(pygame.Surface((1, 1)))
#             return self._mask.overlap(other, hitbox)
#         return False