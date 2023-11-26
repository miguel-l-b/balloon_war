from pygame import *
from pygame.locals import *
from pygame.locals import *
from core.scene import Scene

class TestGameScene(Scene):
  def __init__(self, screen: Surface):
    pass

# class TestGameScene(Scene):
#     def __init__(self, screen: Surface):
#         super().__init__(screen)
#         self.screen = screen
#         self.__p1_gun = Gun(name="Darts", 
#                                meg_capacity=10,
#                                damage = 10,
#                                shoot_cooldown_time=30, 
#                                reload_cooldown_time=100, 
#                                bullet_size=(45, 45),
#                                bullet_image_path="assets/sprites/darts.png",
#                                bullet_color=(43, 65, 194),
#                                bullet_speed=4
#                                )
#         self.__p2_gun = Gun(name="Darts", 
#                                meg_capacity=10,
#                                damage = 10,
#                                shoot_cooldown_time=30, 
#                                reload_cooldown_time=100, 
#                                bullet_size=(45, 45),
#                                bullet_image_path="assets/sprites/darts.png",
#                                bullet_color=(128, 25, 41),
#                                bullet_speed=4
#                                )
#         self.__p1 = Player("p1", "assets/sprites/balloon_cyan.png", (43, 65, 194), (350, 200), 100, self.__p1_gun, 2.5)
#         self.__p2 = Player("p2", "assets/sprites/balloon_orange.png", (128, 25, 41), (20, 450), 100, self.__p2_gun, 2.5) 

#         self.__players = [self.__p1, self.__p2]

#         self.__hp_font = pygame.font.SysFont("Courier New", 24)
#         self.__bullets_font = pygame.font.SysFont("Courier New", 18)

#         self.__limitFPS = ResolverConfig.resolve()["game"]["frameRate"]

#         self.__gravity = 0.02

#     def start(self):
#         self.loop()

#     def draw(self):
#         self.screen.fill((43, 195, 255))
#         p1_hp_display = self.__hp_font.render(f"Cyan's HP: {self.__p1.hp}", True, (93, 133, 245))
#         p2_hp_display = self.__hp_font.render(f"Oranges's HP: {self.__p2.hp}", True, (222, 119, 51))
        
#         p1_bullets_display = self.__bullets_font.render(f"bullets: {self.__p1.gun.bullets}", True, (93, 133, 245))
#         p2_bullets_display = self.__bullets_font.render(f"bullets: {self.__p2.gun.bullets}", True, (222, 119, 51))
        
#         self.screen.blit(p1_hp_display, (300, 10))
#         self.screen.blit(p2_hp_display, (10, 10))
#         self.screen.blit(p1_bullets_display, (300, 50))
#         self.screen.blit(p2_bullets_display, (10, 50))

#         for player in self.__players:
#             if (player.hp <= 0):
#                 player.die()
#                 self.__players.remove(player)
#             else:
#                 currentSprite = SpriteSlicer(player.image_path, {"width": player.size[0], "height": player.size[1], "rows": 8, "columns": 1}, 1, [120, 120])
#                 self.screen.blit(currentSprite.get(0), (player.coords[0], player.coords[1]))

#         for shot in self.__p1.shots:
#             # shot collision
#             if (self.__p2.alive):
#                 if (self.__p2.hit(shot.coords)):
#                     self.__p2.hp -= self.__p1.gun.damage
#                     self.__p1.removeShot(shot)
            
#             if (shot.coords[0] < 0):
#                 self.__p1.removeShot(shot)
                
#             else:
#                 # replaced by sprite
#                 currentSprite = SpriteSlicer(shot.image_path, {"width": shot.size[0], "height": shot.size[1], "rows": 2, "columns": 1}, 2, [90, 90])
#                 self.screen.blit(currentSprite.get(0), (shot.coords[0], shot.coords[1]))
#                 shot.coords = (shot.coords[0] - shot.speed, shot.coords[1])

#         for shot in self.__p2.shots:
#             # shot collision
#             if (self.__p1.alive):
#                 if (self.__p1.hit(shot.coords)):
#                     self.__p1.hp -= self.__p2.gun.damage
#                     self.__p2.removeShot(shot)
            
#             if (shot.coords[0] > self.screen.get_width()):
#                 self.__p2.removeShot(shot)
                
#             else:
#                 # replaced by sprite
#                 currentSprite = SpriteSlicer(shot.image_path, {"width": shot.size[0], "height": shot.size[1], "rows": 2, "columns": 1}, 2, [90, 90])
#                 self.screen.blit(currentSprite.get(1), (shot.coords[0], shot.coords[1]))
#                 shot.coords = (shot.coords[0] + shot.speed, shot.coords[1])
            
#     def loop(self):
#         while True:
#             self.draw()
#             pygame.display.update()
#             self.__p1.gun.update()
#             self.__p2.gun.update()
            

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:                    
#                     pygame.quit()
#                     exit()
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_UP:
#                         self.__p1.moveUp(self.__gravity)
#                     if event.key == pygame.K_DOWN:
#                         self.p1_direction_up = False

#                     if event.key == pygame.K_LEFT:
#                         if (self.__p1.alive):
#                             self.__p1.shoot()
#                     if event.key == pygame.K_RIGHT:
#                         if (self.__p1.alive):
#                             self.__p1.reload()

#                     if event.key == pygame.K_w:
#                         self.__p2.moveUp(self.__gravity)
#                     if event.key == pygame.K_s:
#                         self.p2_direction_up = False
#                     if event.key == pygame.K_d:
#                         if (self.__p2.alive):
#                             self.__p2.shoot()
#                     if event.key == pygame.K_a:
#                         if (self.__p2.alive):
#                             self.__p2.reload()

            
#             if (not self.__p1.isInsideLimits(self.screen)):
#                 # self.p1_direction_up = not self.p1_direction_up
#                 self.__p1.hp -= 15
#                 self.__p1.moveUp(self.__gravity)
#             if (not self.__p2.isInsideLimits(self.screen)):
#                 self.__p2.hp -= 15
#                 self.__p2.moveUp(self.__gravity)

#             if self.__p1.is_moving_up:
#                 self.__p1.moveUp(self.__gravity)
#             else:
#                 self.__p1.moveDown(self.__gravity)

#             if self.__p2.is_moving_up:
#                 self.__p2.moveUp(self.__gravity)
#             else:
#                 self.__p2.moveDown(self.__gravity)


#             pygame.time.Clock().tick(self.__limitFPS)