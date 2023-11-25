import pygame
from pygame import *
from pygame.locals import *
from time import sleep
from pygame.locals import *
from entities.player import Player
from entities.gun import Gun


# pygame.init()
class TestGame():
    def __init__(self, screen: Surface):
        self.screen = screen
        self.__p1_gun = Gun(name="Darts", 
                               meg_capacity=10,
                               damage = 10,
                               shoot_cooldown_time=30, 
                               reload_cooldown_time=100, 
                               bullet_size=10,
                               bullet_color=(43, 65, 194),
                               bullet_speed=2
                               )
        self.__p2_gun = Gun(name="Darts", 
                               meg_capacity=10,
                               damage = 10,
                               shoot_cooldown_time=30, 
                               reload_cooldown_time=100, 
                               bullet_size=10,
                               bullet_color=(128, 25, 41),
                               bullet_speed=2
                               )
        self.__p1 = Player("p1", (43, 65, 194), (450, 50), 100, self.__p1_gun, 5)
        self.__p2 = Player("p2", (128, 25, 41), (50, 450), 100, self.__p2_gun, 5) 

        self.__players = [self.__p1, self.__p2]

        self.__hp_font = pygame.font.SysFont("Courier New", 24)
        self.__bullets_font = pygame.font.SysFont("Courier New", 18)

    def draw(self):
        self.screen.fill((255, 255, 255))
        p1_hp_display = self.__hp_font.render(f"Cyan's HP: {self.__p1.hp}", True, (93, 133, 245))
        p2_hp_display = self.__hp_font.render(f"Oranges's HP: {self.__p2.hp}", True, (222, 119, 51))
        
        p1_bullets_display = self.__bullets_font.render(f"bullets: {self.__p1.gun.bullets}", True, (93, 133, 245))
        p2_bullets_display = self.__bullets_font.render(f"bullets: {self.__p2.gun.bullets}", True, (222, 119, 51))
        
        self.screen.blit(p1_hp_display, (300, 10))
        self.screen.blit(p2_hp_display, (10, 10))
        self.screen.blit(p1_bullets_display, (300, 50))
        self.screen.blit(p2_bullets_display, (10, 50))

        for player in self.__players:
            if (player.hp <= 0):
                player.die()
                self.__players.remove(player)
            else:
                pygame.draw.circle(self.screen, player.color, player.coords, player.size)
        
            for shot in self.__p1.shots:
                # shot collision
                if (self.__p2.alive):
                    if (self.__p2.hit(shot.coords)):
                        self.__p2.hp -= self.__p1.gun.damage
                        self.__p1.removeShot(shot)
                
                if (shot.coords[0] < 0):
                    self.__p1.removeShot(shot)
                    
                else:
                    # replaced by sprite
                    pygame.draw.circle(self.screen, shot.color, shot.coords, shot.radius)
                    shot.coords = (shot.coords[0] - shot.speed, shot.coords[1])

            for shot in self.__p2.shots:
                # shot collision
                if (self.__p1.alive):
                    if (self.__p1.hit(shot.coords)):
                        self.__p1.hp -= self.__p2.gun.damage
                        self.__p2.removeShot(shot)
                
                if (shot.coords[0] > self.screen.get_width()):
                    self.__p2.removeShot(shot)
                    
                else:
                    # replaced by sprite
                    pygame.draw.circle(self.screen, shot.color, shot.coords, shot.radius)
                    shot.coords = (shot.coords[0] + shot.speed, shot.coords[1])
    def loop(self):
        while True:
            self.draw()
            pygame.display.update()
            self.__p1.gun.update()
            self.__p2.gun.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:                    
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if (self.__p1.alive):
                            self.__p1.shoot()
                    if event.key == pygame.K_RIGHT:
                        if (self.__p1.alive):
                            self.__p1.reload()

                    if event.key == pygame.K_d:
                        if (self.__p2.alive):
                            self.__p2.shoot()
                    if event.key == pygame.K_a:
                        if (self.__p2.alive):
                            self.__p2.reload()

            keys = pygame.key.get_pressed()
            if (self.__p1.alive and self.__p1.isInsideLimits(self.screen)):
                if keys[pygame.K_UP]:
                    self.__p1.moveUp()
                if keys[pygame.K_DOWN]:
                    self.__p1.moveDown()

            if (self.__p2.alive and self.__p2.isInsideLimits(self.screen)):
                if keys[pygame.K_w]:
                    self.__p2.moveUp()
                if keys[pygame.K_s]:
                    self.__p2.moveDown() 

            sleep(0.01)
def start(screen: Surface):
    TestGame(screen).loop()